import json
import requests
import warnings
warnings.filterwarnings("ignore")

def tranlate(source, direction):
    url = "http://api.interpreter.caiyunai.com/v1/translator"

    # WARNING, this token is a test token for new developers,
    # and it should be replaced by your token
    token = "9cn3ii2ayv8u1umcp032"

    payload = {
        "source": source,
        "trans_type": direction,
        "request_id": "demo",
        "detect": True,
    }

    headers = {
        "content-type": "application/json",
        "x-authorization": "token " + token,
    }

    response = requests.request(
        "POST", url, data=json.dumps(payload), headers=headers)

    return json.loads(response.text)["target"]


def oneRequre(transmod):

    str = input().strip()
    source = [str]
    target = tranlate(source, transmod)
    for i in target:
        print('\033[31m >\033[0m'+i+'\n\n')


transmod = 'auto2zh'
print('初始化,默认'+'\033[31m auto2zh\033[0m')
print('是否更换翻译方向(Y/y)？')
i = input()
if i == 'y' or i == 'Y':
    print("\033[32m 1.zh2en\033[0m")
    print("\033[35m 2.zh2ja\033[0m")
    print('请输入序号：')
    i = input()
    if i == '1':
        transmod = 'zh2en'
    else:
        transmod = 'zh2ja'
        
print('当前为：'+transmod+'\n\n')
while True:
    print('\033[31m >>>\033[0m', end='')
    oneRequre(transmod)
