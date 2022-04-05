#!/bin/bash

# 没有驱动可使用一下代码下载
# LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
# wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip
# unzip chromedriver_linux64.zip
# echo "配置执行权限"
# chmod +x chromedriver
# echo "移动到 /usr/bin/"
# sudo mv chromedriver /usr/bin/
#

# 最好是全路径
python main.py [学号] [密码] >> ./log.log


cat log.log | mail -s "自动健康上报日志" xxx@xx.com