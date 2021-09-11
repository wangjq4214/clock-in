from util import split_data, task, parse_info
from header import info_header, login_header
from data import save_data_str
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from time import sleep

if __name__ == "__main__":
    login_header = split_data(login_header)
    info_header = split_data(info_header)
    save_data = split_data(save_data_str)
    flag = 0
    # 多线程处理
    while True:
        if datetime.now().hour == 17 and flag == 0:
            with ThreadPoolExecutor(max_workers=10) as executor:
                for username, password, SendKey in parse_info():
                    if username and password:
                        executor.submit(task, username, password, login_header, info_header, save_data, SendKey)
                flag = 1
        else:
            if datetime.now().hour != 17:
                flag = 0
            sleep(10)
