# AutoNEUHealthReport

## 使用方法

### 1 crontab定时任务

在cmd.sh 填写好账号密码

#### crontab参考代码

```
crontab -l

30  1 * * * sh /home/projects/AutoNEUHealthReport/cmd.sh >> /home/projects/AutoNEUHealthReport/log.log
```

#### crontab相关教程
`crontab -l `

`crontab -e`

```
[root@VM-8-12-centos AutoNEUHealthReport]# service crond --help
Usage: service < option > | --status-all | [ service_name [ command | --full-restart ] ]
```
### 2 使用GitHub的Action

这个方法可以白嫖github的服务器帮你上报

action配置文件在.github/workflows中已经写好

需要使用者先fork项目 然后在 settings->Secrets->Actions 配置环境变量(写好你的账号密码)；再开启action任务

## 谷歌驱动下载地址

进入驱动网址：

http://npm.taobao.org/mirrors/chromedriver

下载对应版本的谷歌驱动