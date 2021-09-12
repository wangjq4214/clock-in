import requests
import json
import os
from data import geo_api_info, info_url, login_url, save_url

def split_data(data_str):
    data_dict = dict()
    for line in data_str.split("\n"):
        if line:
            data_dict[line.split(":")[0].strip()] = line.split(":")[1].strip()
    return data_dict

def task(username, password, login_header, info_header, save_data, SendKey):
    session = requests.session()
    from_data = {
        'username': username,
        'password': password
    }
    try:
        response = session.post(login_url, headers=login_header, data=from_data)
        message = dict(json.loads(response.text))["m"]
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
            print(info_data)
            response = session.post(save_url, headers=info_header, data=save_data)
            print(response.text)
            message = message + '\n' + dict(json.loads(response.text))["m"] + '\n'
    except Exception as e:
        message = "打卡失败！\n" + e
    finally:
        send_result_to_wechat(message, SendKey)
    session.close()


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
