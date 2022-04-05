# coding=UTF-8
import os.path

from selenium import webdriver
import time
import platform
import datetime
import sys

from selenium.webdriver.common.by import By

"""
AutoNEUHealthReport 教学
https://www.jianshu.com/p/1b63c5f3c98e 
无界面
https://blog.csdn.net/weixin_41782332/article/details/81484769 
"""
chrome_options = webdriver.ChromeOptions()
MY_XPATH = [
    '//*[@id="app"]/main/div/form/div[1]/table/tbody/tr/td[1]/div/div/div/label[1]/span[2]',
    '//*[@id="app"]/main/div/form/div[3]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]/span[2]',
    '//*[@id="app"]/main/div/form/div[4]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]/span[2]',
    '//*[@id="app"]/main/div/form/div[6]/button'
]

# python main.py <账号> <密码>
ID = sys.argv[1]
PASSWORD = sys.argv[2]

current_dir = os.path.dirname(os.path.abspath(__file__))


def printLog(msg):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + msg)


if __name__ == '__main__':
    printLog("ID为: " + ID + "的同学你好！现在开始给您健康上报了。")

    printLog("开始注册驱动")

    if platform.system() == 'Linux':
        engine = current_dir + '/chromedriver'
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')  # 在centOS 需要这样设置
        # printLog('chromedriver path: /user/bin/chromedriver')
        # driver = webdriver.Chrome('/user/bin/chromedriver', options=chrome_options)
    else:
        engine = current_dir + r'\chromedriver.exe'
    printLog('chromedriver path: ' + engine)
    driver = webdriver.Chrome(engine, options=chrome_options)


    # 登录
    printLog("开始进入登录页面")
    driver.get('https://e-report.neu.edu.cn/')
    driver.find_element(by=By.ID, value='un').send_keys(ID)
    time.sleep(1.5)
    driver.find_element(by=By.ID, value='pd').send_keys(PASSWORD)
    time.sleep(1.5)
    driver.find_element(by=By.ID, value='index_login_btn').click()
    printLog("登录完成")
    time.sleep(1.5)
    printLog("开始进入报表页面")
    # 找到搜索按钮
    driver.find_element(by=By.XPATH, value=MY_XPATH[0]).click()
    time.sleep(1.5)
    driver.find_element(by=By.XPATH, value=MY_XPATH[1]).click()
    time.sleep(1.5)
    driver.find_element(by=By.XPATH, value=MY_XPATH[2]).click()
    time.sleep(1.5)
    driver.find_element(by=By.XPATH, value=MY_XPATH[3]).click()
    time.sleep(1.5)
    printLog("填报完成")

    # 检查填表是否成功
    driver.get('https://e-report.neu.edu.cn/calendar')
    time.sleep(1.5)
    text = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/h2').text
    if text == '已签到':
        printLog("填报成功")
    else:
        printLog("填报失败！！！！！！！")
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ' 文本为:  ', text)
    time.sleep(1.5)

    # 填报温度
    driver.get('https://e-report.neu.edu.cn/inspection/items/1/records/create')
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/form/div[5]/input').click()
    time.sleep(1.5)
    printLog("晨检完成")
    driver.get('https://e-report.neu.edu.cn/inspection/items/2/records/create')
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/form/div[5]/input').click()
    time.sleep(1.5)
    printLog("中检完成")

    driver.get('https://e-report.neu.edu.cn/inspection/items/3/records/create')
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/form/div[5]/input').click()
    time.sleep(1.5)
    printLog("晚检完成")


    # 检查填表是否成功
    driver.get('https://e-report.neu.edu.cn/inspection/items')
    printLog("检查填报温度")
    text = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[1]/div/div/p').text
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ' 文本为:  ', text)
    text = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[2]/div/div/p').text
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ' 文本为:  ', text)
    text = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div[3]/div/div/p').text
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ' 文本为:  ', text)

    time.sleep(1.5)
    driver.quit()  # 记得关闭浏览器否则服务器内存会被占满
    printLog("chrome关闭成功")
