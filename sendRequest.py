import requests
import logging

class sendRequest:
    def __init__(self, url, serviceKey, logging_level=logging.INFO):
        self.url = url
        self.serviceKey = serviceKey
        self.logging = logging.getLogger(__name__)
        self.logging.setLevel(logging_level)

    def setURL(self, url):
        self.url = url

    def _sendGetRequest(self, params):
        response = requests.get(self.url, params=params)
        self.logging.info("sendGetRequest: %s", response)
        return response

    def sendGetRequest(self, params):
        #params 에 LAWD_CD, DEAL_YMD 유무 확인
        if "LAWD_CD" not in params:
            self.logging.error("sendGetRequest: LAWD_CD is not in params")
            return None
        if "DEAL_YMD" not in params:
            self.logging.error("sendGetRequest: DEAL_YMD is not in params")
            return None

        params["serviceKey"] = self.serviceKey
        self.logging.info("sendGetRequest: %s", params)
        return self._sendGetRequest(params)



# main 문 실행
if __name__ == "__main__":
    # 로깅 설정
    logging.basicConfig(level=logging.INFO)
    # 인스턴스 생성
    urlAddress = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade"
    serviceKey = "bFYmAkU3nFuv7MLgqjMAMr3aQk6p0vhZ5vVhLiP9FNjU1BRq42Xp9Z8VtFZ7CEOAue71mmjc44GZsDrIW5fjbQ=="
    sendRequest = sendRequest(urlAddress, serviceKey)
    # 파라미터 생성
    params = {
        "LAWD_CD": "11110",
        "DEAL_YMD": "201512"
    }
    # 요청
    response = sendRequest.sendGetRequest(params)
    # 응답
    print(response.text)