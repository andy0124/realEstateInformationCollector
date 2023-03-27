import sendRequest
import xml.etree.ElementTree as ET
from openpyxl import Workbook
import logging
import datetime

# main 문 실행
if __name__ == "__main__":
    # 로그 info로 설정
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # 인스턴스 생성
    urlAddress = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade"
    serviceKey = "bFYmAkU3nFuv7MLgqjMAMr3aQk6p0vhZ5vVhLiP9FNjU1BRq42Xp9Z8VtFZ7CEOAue71mmjc44GZsDrIW5fjbQ=="
    sendRequest = sendRequest.sendRequest(urlAddress, serviceKey)
    # 파라미터 생성
    # params = {
    #     "LAWD_CD": "11110",
    #     "DEAL_YMD": "201512"
    # }

    # LAWD_CD 리스트
    LAWD_CD = ["11110", "11140", "11170", "11200", "11215", "11230", "11260", "11290", "11305", "11320", "11350",
               "11380", "11410", "11440", "11470", "11500", "11530", "11545", "11560", "11590", "11620", "11650",
               "11680", "11710", "11740"]
    # LAWD_CD 지역명 리스트
    LAWD_CD_NAME = ["종로구", "중구", "용산구", "성동구", "광진구", "동대문구", "중랑구", "성북구", "강북구", "도봉구", "노원구", "은평구", "서대문구", "마포구",
                    "양천구", "강서구", "구로구", "금천구", "영등포구", "동작구", "관악구", "서초구", "강남구", "송파구", "강동구"]
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2023, 3, 1)
    isError = False

    while start_date < end_date:
        # print(start_date.strftime("%Y%m"))
        if isError:
            logger.warn("Last Data - YEAR MONTH : {}".format(start_date.strftime("%Y%m")))
            break
        current_date = start_date.strftime("%Y%m")
        print("type of current_date : ", type(current_date))
        logger.info("YEAR MONTH : %s", current_date)
        params = dict()
        params["DEAL_YMD"] = start_date.strftime("%Y%m")



        for idx, i in enumerate(LAWD_CD):
            params["LAWD_CD"] = i
            logger.info("LAWD_CD : %s, 지역명 : %s", i, LAWD_CD_NAME[idx])
            response = sendRequest.sendGetRequest(params)
            if response.status_code != 200:
                logger.warn("Error occured. Stop the program")
                logger.warn("Last Data - Area Code : {}".format(LAWD_CD_NAME[idx]))
                isError = True
                break
            # 응답
            logger.info("response : %d", response.status_code)
            # xml 형태의 response를 엑셀로 저장

            with open("data\\Apartment_price_{}_{}.xml".format(start_date.strftime("%Y%m"),LAWD_CD_NAME[idx]), "w", encoding="utf-8") as f:
                f.write(response.text)


        # 월 증가
        temp_month = start_date.month + 1
        if start_date.month == 12:
            start_date = start_date.replace(year=start_date.year + 1, month=1)
        else:
            start_date = start_date.replace(month=start_date.month + 1)
