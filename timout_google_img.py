import threading
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request



search = "indoor fire"
driver = webdriver.Chrome('C:/chrome/chromedriver.exe')
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys(search)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 3
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
SAVE_FLAG = False
def timeout(limit_time):
    start = time.time()
    print(time.time() - start , "timer start.")
    remain = 0
    while True:
        if remain != (int)(time.time() - start) and remain%10==0 : print(limit_time - remain)
        remain = (int)(time.time() - start)
        if time.time() - start > limit_time or SAVE_FLAG:
            raise Exception('timeout. or image saved.')



while True: #검색 결과들을 스크롤해서 미리 로딩해둠.
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 0
# timer = Process(target=timeout, args=(50,))
for image in images:
    SAVE_FLAG = False
    timer = threading.Thread(target=timeout, args=(30,))
    try:
        image.click()
        time.sleep(3)
        timer.start()
        #이미지의 XPath 를 붙여넣기 해준다. >> F12 를 눌러서 페이지 소스의 Element에서 찾아보면됨.
        imgUrl = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute("src")
        urllib.request.urlretrieve(imgUrl, "images/"+ search + "_{0:04}".format(count) + ".jpg") #저장할 이미지의 경로 지정
        print('Save images : ', "images/"+ search + "_{0:04}".format(count) + ".jpg")
        SAVE_FLAG = True
        count += 1
        if timer.is_alive():
            timer.join()
    except Exception as e:
        if timer.is_alive():
            timer.join()
        pass
print('driver end. Total images : ', count)
driver.close()