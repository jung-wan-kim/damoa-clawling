from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyperclip
import pyautogui
import time, os

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# service = Service(executable_path="bin/chromedriver_for_mac")
driver = webdriver.Chrome('/Users/jung-wankim/Downloads/chromedriver')
# driver = webdriver.Chrome('/Users/jung-wankim/Downloads/chromedriver')


# 인증번호 호출
def phoneAuth():
    # 브라우저 꺼짐 방지
    # 보험다모아 이동
    driver.implicitly_wait(3)
    driver.maximize_window()

    driver.get("https://e-insmarket.or.kr/")
    # driver.execute_script("window.open('https://e-insmarket.or.kr/','_blank');");

    # driver.add_cookie({"name": "key"})
    original_window = driver.current_window_handle

    print('original_window', original_window)

    return original_window

def updateSerInfo(windowId, userName):

    driver.switch_to.window(windowId)
    # 운전자 보험 이동하기
    time.sleep(3)
    driver.execute_script("fnGoAimtRealIntro()")

    # 정보동의
    time.sleep(3)
    driver.execute_script("allTermAgree()")

    # 휴대폰 인증
    time.sleep(2)
    driver.execute_script("submitForm1('mobile')")

    # 휴대폰인증 정보동의
    time.sleep(2)
    driver.execute_script('allAgreeTerms()')

    # 이름
    time.sleep(2)
    auth_name = driver.find_element(By.NAME, 'authName')
    auth_name.click()
    pyperclip.copy(userName)
    # pyautogui.hotkey('command', 'v')
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')



    # 성별

    sex = driver.find_element(By.ID, 'sexM')
    sex.click()

    # 주민등록번호

    # 통신사

    #  휴대폰번호


    #  확인버튼


    # driver.switch_to.window(uselessWindows[-1])
    # driver.close()
    # driver.switch_to.window(uselessWindows[0])

    # driver.implicitly_wait(1)
    # driver.execute_script("fnGoAimtRealIntro()")
