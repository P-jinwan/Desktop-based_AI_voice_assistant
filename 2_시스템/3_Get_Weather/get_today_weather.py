#!/usr/bin/env python
# coding: utf-8

# In[14]:


def TodayWeather() :    
    ############################## ▼패키지 임포트▼ ##############################
    import requests
    from bs4 import BeautifulSoup as bs
    ############################## ▲패키지 임포트▲ ##############################

    ############################## ▼날씨 리뷰 기능 실행▼ ##############################
    # 네이버의 '오늘 날씨'를 검색한 위치에서 시작합니다.
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=2&acq=%EC%98%A4%EB%8A%98+%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EC%98%A4%EB%8A%98+%EB%82%A0%EC%94%A8'
    
    # url에 저장된 주소의 HTML 정보를 가져옵니다.
    response = requests.get(url)
    
    # 상태 코드가 200번이면 크롤링을 진행합니다.(상태 코드 참고: https://developer.mozilla.org/ko/docs/Web/HTTP/Status)
    if response.status_code == 200 :
        # response 변수에 저장된 HTML 정보를 텍스트 형태로 가져옵니다.
        html = response.text               
        # 크롤링을 진행할 파서 객체를 생성합니다.
        soup = bs(html, 'html.parser') 
        # 지역명을 크롤링합니다.
        area_name = soup.select_one('#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.top_wrap > div.title_area._area_panel > h2.title').get_text()
        # 맑은지 흐린지 대략적인 날씨 상황을 가져옵니다.
        weather = soup.select_one('#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > p > span.weather.before_slash').get_text()
        # 최저 기온을 가져옵니다.
        lowest = soup.select_one('#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.content_area > div.inner > div > div.list_box._weekly_weather > ul > li:nth-child(1) > div > div.cell_temperature > span > span.lowest').get_text()
        # 최고 기온을 가져옵니다.
        highest = soup.select_one('#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.content_area > div.inner > div > div.list_box._weekly_weather > ul > li:nth-child(1) > div > div.cell_temperature > span > span.highest').get_text()
        # 현재 기온을 가져옵니다.
        present = soup.select_one('#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.weather_graphic > div.temperature_text > strong').get_text()
    # 연결이 제대로 되지 않는다면 상태 코드를 출력하고 크롤링을 하지 않습니다.
    else : 
        print(response.status_code)
    
    # TTS에 넘길 문장을 작성합니다.
    text = ('오늘 {0} 날씨는 {1}이며, {2}은 {3}, {4}은 {5}, {6}는 {7}입니다.'.format(area_name, weather, lowest[:4],
                                                                                    lowest[5:], highest[:4], highest[5:],
                                                                                    present[:5], present[5:]))    
    ############################## ▲날씨 리뷰 기능 실행▲ ##############################
    return text

