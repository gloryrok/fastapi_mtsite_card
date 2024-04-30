#kakao api를 사용하여 나에게 톡 보내기
# 1. kakao developer 설정
# 2. 인증 코드 요청 -> 카카오 서버  -> 인증 코드 전달
# 3. 인증 코드를 사용하여 토큰 발급
# 4. 토큰을 사용하여 나에게 메세지 보내기
#  인증 코드는 1회성 토큰 발급 받음과 동시에 효력x

# 카카오 API 용어
#  인증코드 : 1회성, 토큰(Access, Refresh)
#  Access 토큰 : 카카오 api서비스를 이용할 때 사용
#  Refresh 토큰 : Access 토큰을 재발급 받기 위해 사용
#  생명주기 : 인증코드(1회), Access(6시간), Refresh(2달)
#  Refresh Token은 발급받고 1달 후 부터 재발급 가능
#  Access와 Refresh woqkfrmq qkesms zhemsms ehddlf
#  ㄴ재발급 코드 : Refresh 발급 받은지 1달 미만, Access 토큰만 재발급해서 리턴
#  ㄴ재발급 코드 : Refresh 발급 받은지 1달 이상, Access 토큰과 Refresh 토큰 재발급해서 리턴


# 카카오 API 사용방법
# 1. kakao developer 사이트에서 " 권한 허용 및 동의"
# 2. 웹브라우저 URL을 통해서 인증 코드 발급
# 3. 인증코드 사용해서 토큰(Acess, Refresh) 발급
# 4. Access 사용해서 서비스 이용
# 5. 1달에 한 번씩 Refresh 토큰 재발급 스케쥴링



import requests
import json


url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "clinedt_id" : "c77b6f404966d8a30d2c29ff2329eef6",                   #RESTAPI KEY
    "redirect_url" : "http://127.0.0.1:8000",
    "code":"bU7mZUvs4TmbksAIStPzrzJEGkfPpPwduALD150CmFtLXfGqLogwC4e9FLIKKiVPAAABjyzU3nWGtS2__sNdBQ"                      #인증토큰을 발급 받아서 나온 코드를 복사
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

access_tokens = ""
msg_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {
    "Authorization": "Bearer " + access_tokens
}
msg_data = {
    "template_object":json.dumps({
        "object_type": "text",
        "text": "카카오톡 테스트",
        "link":{"mobile_web_url":"https://www.naver.com"}
    })
} 
response = requests.post(msg_url, headers=headers, data=msg_data)

