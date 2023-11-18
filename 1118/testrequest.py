import requests

HOST = 'http://localhost:8000'
LOGIN_URL = HOST + '/account/login/'

# 사용자가 본 HTML파일에 입력 form에서 입력한 데이터
LOGIN_INFO = {
    "email": "donghu@naver.com",
    "password": "donghu1234",
}

# POST 요청 보내기
response = requests.post(LOGIN_URL, data=LOGIN_INFO)
token = response.json()['access_token']

# case1: token이 정상적인 경우
print('정상적인 token')

# 로그인한 사용자만 들어갈 수 있는 URL에 접속
# headers에 token을 넣어서 전송
header = {
    'Authorization': 'Bearer ' + token
}

data = {
    'title': '제목',
    'content': '내용',
    'author': 1
}

res = requests.get(HOST + '/account/profile/', headers=header, data=data)
print(res.status_code)
print(res.text)

# case2: token이 변조된 경우
print('변조된 token')
token_modified = 'worngtoken'

header = {
    'Authorization': 'Bearer ' + token_modified
}

res = requests.get(HOST + '/account/profile/', headers=header, data=data)
print(res.status_code)
print(res.text)