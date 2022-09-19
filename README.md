# 支持多线程的北航每日打卡脚本

## 运行环境

1、需要python3(建议用python3.8)和requests库

2、安装requests库

```# pip install requests```

## 修改配置文件

1、在```user_info.txt```文件中填入学号和密码，可填入多名学生的信息，若需要微信推送，第三列(可选)需要填入server酱的SendKey（见官网 [https://sct.ftqq.com/](https://sct.ftqq.com/)）；

2、地理信息保存在```data.py```的```geo_api_info```中，默认使用了校园路校区的地理位置；

3、如果要把位置改成沙河校区，在```data.py```中把```geo_api_info```注释，再把下面沙河校区的```geo_api_info```解除注释。

## 运行

```main.py```中设置每日17点执行打卡任务，也可以在```mian.py```中将17改成其他时间

1、Windows运行（不可关闭程序）

```# python main.py```

2、Linux系统后台运行

```# nohup python -u main.py > log.txt 2>&1 &```
