import requests
import os

"""
bjtu校园网登录
获取信息(打开开发者工具，登录抓包后，查看 "login?..." 的标头与载荷):
url: 发送请求的地址
header: 请求头
data: 请求信息(载荷)
"""

url = 'http://10.10.42.3'  # 校园网登录的url
message_path = 'connect_message.txt'  # 用于储存账号密码


def connect(user: str, password: str):
    """发送post请求连接校园网"""

    # 请求头
    header = {
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': '10.10.42.3',
        'Referer': 'http://10.10.42.3/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

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

    # 发送请求并打印状态码
    response = requests.post(url, data, headers=header).status_code
    print(f'Status Code: {response}')


if __name__ == '__main__':

    if os.path.exists(message_path):
        with open(message_path, 'r') as f_r:
            lines = f_r.readlines()
            user = str(lines[0].strip())
            password = str(lines[1].strip())
    else:
        user = input('请输入账号: ')
        password = input('请输入密码: ')

        save_code = input('是否保存密码[y/n](默认y): ')

        if save_code == 'y' or save_code == '':
            with open(message_path, 'w') as f_w:
                f_w.write(user + '\n' + password)

    print(f'重新设置账号密码，删除或修改\'{message_path}\'文件')
    connect(user=user, password=password)
