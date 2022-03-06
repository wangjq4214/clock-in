import requests
import json
import os
from data import geo_api_info, info_url, login_url, save_url, all_try_times
import time

def split_data(data_str):
    data_dict = dict()
    for line in data_str.split("\n"):
        if line:
            data_dict[line.split(":")[0].strip()] = line.split(":")[1].strip()
    return data_dict


def execution(session, username, form_data, login_header, info_header, save_data, message=[]):
    response = session.post(login_url, headers=login_header, data=form_data)
    res_json = dict(json.loads(response.text))
    message_login = username + ": " + ("登录成功！" if int(res_json["e"]) == 0 else res_json["m"])
    message.append(time.strftime(r'(%Y/%m/%d %H:%M:%S)',time.localtime(time.time())) + message_login)
    if response.status_code == 200:
        # 获取信息
        response = session.get(info_url, headers=info_header)
        info_data = dict(json.loads(response.text))
        # 设置打卡信息
        save_data["geo_api_info"] = geo_api_info
        save_data["realname"] = info_data["d"]["uinfo"]["realname"]
        save_data["number"] = info_data["d"]["uinfo"]["role"]["number"]
        save_data["uid"] = info_data["d"]["info"]["uid"]
        save_data["created"] = info_data["d"]["info"]["created"]
        save_data["date"] = info_data["d"]["info"]["date"]
        save_data["id"] = info_data["d"]["info"]["id"]
        # 发送打卡请求
        response = session.post(save_url, headers=info_header, data=save_data)
        res_json = dict(json.loads(response.text))
        message_daka = username + ": " + ("打卡成功！" if int(res_json["e"]) == 0 else res_json["m"])
        message.append(time.strftime(r'(%Y/%m/%d %H:%M:%S)',time.localtime(time.time())) + message_daka)
        # message += message_login + "\n\n" + message_daka


def task(username, password, login_header, info_header, save_data, SendKey):
    form_data = {
        'username': username,
        'password': password
    }
    message = []
    try_times = 0
    success = False
    while try_times <= all_try_times and not success:
        try:
            session = requests.session()
            execution(session, username, form_data, login_header, info_header, save_data, message)
            success = True
        except Exception as e:
            try_times += 1
            message.append(time.strftime(r'(%Y/%m/%d %H:%M:%S)',time.localtime(time.time())) + username+": 打卡失败！ Exception: " + str(e))
            if try_times <= all_try_times:
                message.append(time.strftime(r'(%Y/%m/%d %H:%M:%S)',time.localtime(time.time())) + username+": 正在重新尝试，第{}次/共{}次".format(try_times, all_try_times))
            else:
                message.append(time.strftime(r'(%Y/%m/%d %H:%M:%S)',time.localtime(time.time())) + username+": 请手动打卡！")
        finally:
            session.close()
    message = "\n".join(message)
    print(message)
    send_result_to_wechat(message, SendKey)


def parse_info():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(BASE_DIR, "user_info.txt"), "r", encoding="utf-8") as f:
        for line in f.readlines():
            if not line.startswith("#"):
                line = line.replace("\n", "").strip()
                if len(line.split(" ")) == 3:
                    yield line.split(" ")[0].strip(), line.split(" ")[1].strip(), line.split(" ")[2].strip()
                elif len(line.split(" ")) == 2:
                    yield line.split(" ")[0].strip(), line.split(" ")[1].strip(), None


def send_result_to_wechat(message, SendKey):
    send_data = {
        "title": "每日打卡",
        "desp": message
    }
    if SendKey:
        send_url = "https://sctapi.ftqq.com/"+SendKey+".send"
        requests.post(send_url, data=send_data)
