#!/bin/bash
# 最好是全路径
python main.py [学号] [密码] >> ./log.log


cat log.log | mail -s "自动健康上报日志" xxx@xx.com