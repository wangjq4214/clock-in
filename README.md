# 支持多线程的北航每日打卡脚本
## 运行环境
1、需要python3(建议用python3.8)和requests库

2、安装requests库

```# pip install requests```
## 修改配置文件
1、在user_info.txt文件中填入学号和密码，可填入多名学生的信息，若需要微信推送，第三列(可选)需要填入server酱的SendKey（见官网 [https://sct.ftqq.com/](https://sct.ftqq.com/)）

2、地理信息保存在data.py的geo_api_info中，默认使用了校内的地理位置，可以不修改

## 运行
1、本地运行（不可关闭程序）

```# python main.py```

2、Linux服务器后台运行

```# nohup python -u main.py > log.txt 2>&1 &```