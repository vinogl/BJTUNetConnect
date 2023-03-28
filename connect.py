import requests
import os
from bs4 import BeautifulSoup
import time

"""
bjtu校园网登录
获取信息(打开开发者工具，登录抓包后，查看 "login?..." 的标头与载荷):
url: 发送请求的地址
header: 请求头
data: 请求信息(载荷)
"""

url = 'http://10.10.42.3'  # 校园网登录的url
message_path = 'connect_message.txt'  # 用于储存账号密码
logo_path = 'Logo/logo.txt'


def connect(user: str, password: str):
    """发送post请求连接校园网"""

    # 请求信息
    data = {
        'DDDDD': user,
        'upass': password,
        '0MKKey': '123456',
        'R1': '0',
        'R3': '0',
        'R6': '0',
        'para': '00',
    }

    try:
        response = requests.post(url, data)  # 发送请求
    except:
        return '未接入校园网！'

    return BeautifulSoup(response.content, 'html.parser').title.string  # 返回响应html中的title标签值


if __name__ == '__main__':
    # 打印logo
    with open(logo_path, 'r') as f:
        print(f.read())

    if os.path.exists(message_path):
        """判断是否存在保存的登录信息"""
        # 若存在保存的登录信息，直接读取
        with open(message_path, 'r') as f_r:
            lines = f_r.readlines()
            user = str(lines[0].strip())
            password = str(lines[1].strip())
    else:
        # 若不存在保存的登录信息，手动输入
        user = input('请输入账号: ')
        password = input('请输入密码: ')
        save_code = input('是否保存密码[y/n](默认y): ')

        if save_code == 'y' or save_code == '':
            """保存登录信息"""
            with open(message_path, 'w') as f_w:
                f_w.write(user + '\n' + password)

    connect_info = connect(user=user, password=password)
    if connect_info == '认证成功页':
        """判断是否连接成功"""
        print('\n%s\n\n连接成功！' % connect_info)
    else:
        print('\n%s\n\n连接失败！' % connect_info)

    time.sleep(2)
