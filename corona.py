
# Step 1. 필요한 모듈과 라이브러리를 import 합니다

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys

import math
import numpy
import pandas as pd
from pandas import read_csv
from selenium.webdriver.support.ui import Select
from matplotlib import pyplot
import chardet

#폰트 깨짐
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# Step 3. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
path = "c:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=')
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
search_cnt_1 = soup.find('div', 'rpsam_graph')

print('******************COVID-19 검색***********************')
print()
full = str(input(''' 
코로나 검색하고 싶은 사항을 입력하세요.
1. 전국 코로나 현황 / 2. 전국 지역별 비율 / 3. 표로 추출하기 / 4. 나가기

숫자를 입력하세요. : '''))

# 무한루프 이용
while True:
    if full == '1':
            number = int(input('''
** 지역 선택 **
1. 서울 2. 부산 3. 대구 4. 인천 5. 광주 6. 대전
7. 울산 8. 세종 9. 경기 10. 강원 11. 충북 12. 충남
13. 전북 14. 전남 15. 경북 16. 경남 17. 제주 18. 검역
19. 돌아가기

숫자를 입력하세요 : '''))
            print()

            if number == 1 :
                result = soup.select_one('button:nth-of-type(1)')
                result1 = soup.select_one('button:nth-of-type(1) span.name')
                result2 = soup.select_one('button:nth-of-type(1) span.num')
                result3 = soup.select_one('button:nth-of-type(1) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)

            elif number == 2 :
                result = soup.select_one('button:nth-of-type(2)')
                result1 = soup.select_one('button:nth-of-type(2) span.name')
                result2 = soup.select_one('button:nth-of-type(2) span.num')
                result3 = soup.select_one('button:nth-of-type(2) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)

            elif number == 3 :
                result = soup.select_one('button:nth-of-type(3)')
                result1 = soup.select_one('button:nth-of-type(3) span.name')
                result2 = soup.select_one('button:nth-of-type(3) span.num')
                result3 = soup.select_one('button:nth-of-type(3) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 4 :
                result = soup.select_one('button:nth-of-type(4)')
                result1 = soup.select_one('button:nth-of-type(4) span.name')
                result2 = soup.select_one('button:nth-of-type(4) span.num')
                result3 = soup.select_one('button:nth-of-type(4) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 5 :
                result = soup.select_one('button:nth-of-type(5)')
                result1 = soup.select_one('button:nth-of-type(5) span.name')
                result2 = soup.select_one('button:nth-of-type(5) span.num')
                result3 = soup.select_one('button:nth-of-type(5) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 6 :
                result = soup.select_one('button:nth-of-type(6)')
                result1 = soup.select_one('button:nth-of-type(6) span.name')
                result2 = soup.select_one('button:nth-of-type(6) span.num')
                result3 = soup.select_one('button:nth-of-type(6) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 7 :
                result = soup.select_one('button:nth-of-type(7)')
                result1 = soup.select_one('button:nth-of-type(7) span.name')
                result2 = soup.select_one('button:nth-of-type(7) span.num')
                result3 = soup.select_one('button:nth-of-type(7) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 8 :
                result = soup.select_one('button:nth-of-type(8)')
                result1 = soup.select_one('button:nth-of-type(8) span.name')
                result2 = soup.select_one('button:nth-of-type(8) span.num')
                result3 = soup.select_one('button:nth-of-type(8) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 9 :
                result = soup.select_one('button:nth-of-type(9)')
                result1 = soup.select_one('button:nth-of-type(9) span.name')
                result2 = soup.select_one('button:nth-of-type(9) span.num')
                result3 = soup.select_one('button:nth-of-type(9) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 10 :
                result = soup.select_one('button:nth-of-type(10)')
                result1 = soup.select_one('button:nth-of-type(10) span.name')
                result2 = soup.select_one('button:nth-of-type(10) span.num')
                result3 = soup.select_one('button:nth-of-type(10) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 11 :
                result = soup.select_one('button:nth-of-type(11)')
                result1 = soup.select_one('button:nth-of-type(11) span.name')
                result2 = soup.select_one('button:nth-of-type(11) span.num')
                result3 = soup.select_one('button:nth-of-type(11) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 12 :
                result = soup.select_one('button:nth-of-type(12)')
                result1 = soup.select_one('button:nth-of-type(12) span.name')
                result2 = soup.select_one('button:nth-of-type(12) span.num')
                result3 = soup.select_one('button:nth-of-type(12) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 13 :
                result = soup.select_one('button:nth-of-type(13)')
                result1 = soup.select_one('button:nth-of-type(13) span.name')
                result2 = soup.select_one('button:nth-of-type(13) span.num')
                result3 = soup.select_one('button:nth-of-type(13) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 14 :
                result = soup.select_one('button:nth-of-type(14)')
                result1 = soup.select_one('button:nth-of-type(14) span.name')
                result2 = soup.select_one('button:nth-of-type(14) span.num')
                result3 = soup.select_one('button:nth-of-type(14) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 15 :
                result = soup.select_one('button:nth-of-type(15)')
                result1 = soup.select_one('button:nth-of-type(15) span.name')
                result2 = soup.select_one('button:nth-of-type(15) span.num')
                result3 = soup.select_one('button:nth-of-type(15) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 16 :
                result = soup.select_one('button:nth-of-type(16)')
                result1 = soup.select_one('button:nth-of-type(16) span.name')
                result2 = soup.select_one('button:nth-of-type(16) span.num')
                result3 = soup.select_one('button:nth-of-type(16) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 17 :
                result = soup.select_one('button:nth-of-type(17)')
                result1 = soup.select_one('button:nth-of-type(17) span.name')
                result2 = soup.select_one('button:nth-of-type(17) span.num')
                result3 = soup.select_one('button:nth-of-type(17) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 18 :
                result = soup.select_one('button:nth-of-type(18)')
                result1 = soup.select_one('button:nth-of-type(18) span.name')
                result2 = soup.select_one('button:nth-of-type(18) span.num')
                result3 = soup.select_one('button:nth-of-type(18) span.before')
                result_1 = str('지역 : '+result1.text) + '\n' + str('확진자수 : '+result2.text) +'\n' + str('추가 확진자수 : '+result3.text)
                print(result_1)
            elif number == 19 :
                print()
                full = str(input(''' 
코로나 검색하고 싶은 사항을 입력하세요.
1.전국 코로나 현황 / 2.전국 지역별 비율 / 3. 표로 추출하기 / 4. 나가기

숫자를 입력하세요. : '''))

            else:
                print()
                re = str(input('다시 검색하시겠습니까? (y,n) : '))
                if re == 'y' or re == 'Y':
                    number = int(input('''
** 지역 선택 **
1. 서울 2. 부산 3. 대구 4. 인천 5. 광주 6. 대전
7. 울산 8. 세종 9. 경기 10. 강원 11. 충북 12. 충남
13. 전북 14. 전남 15. 경북 16. 경남 17. 제주 18. 검역
19. 돌아가기 

숫자를 입력하세요 : '''))
                else :
                    print()
                    print('다시 실행하세요.')
                    break


    if full == '2':
        # Step 3. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        allcity_1 = soup.select_one('.allcity_info1')
        allcity_2 = soup.select_one('.allcity_info2')
        allcity_3 = soup.select_one('.allcity_info3')
        allcity_4 = soup.select_one('.allcity_info4')
        allcity_5 = soup.select_one('.allcity_info5')
        allcity_all = str('**전국 현황**') + '\n' + str(allcity_1.text) + '\n' + str(allcity_2.text) + '\n' + str(
            allcity_3.text) + '\n' + str(allcity_4.text) + '\n' + str(allcity_5.text) + '\n'
        # print(allcity_all)

        allcity1 = soup.select('div ul li div span.tit')[0]
        allcity2 = soup.select('div ul li div span.num')[0]

        # print(allcity1.text +' : '+allcity2.text + '명')

        allcity3 = soup.select_one('div ul li div span.sub_tit')
        allcity4 = soup.select_one('div ul li div span.sub_num')

        # print(allcity3.text +' : '+allcity4.text + '명')

        allcity5 = soup.select('div ul li div span.tit')[1]
        allcity6 = soup.select('div ul li div span.num')[1]

        # print(allcity5.text +' : '+allcity6.text + '명')

        allcity7 = soup.select('div ul li div span.tit')[2]
        allcity8 = soup.select('div ul li div span.num')[2]

        # print(allcity7.text +' : '+allcity8.text + '명')

        allcity9 = soup.select('div ul li div span.tit')[3]
        allcity10 = soup.select('div ul li div span.num')[3]

        # print(allcity9.text +' : '+allcity10.text + '명')

        allcity11 = soup.select('div ul li div span.sub_tit')[1]
        allcity12 = soup.select('div ul li div span.num')[4]

        # print(allcity11.text +' : '+allcity12.text + '명')

        allcity__all = '\n' + str(allcity1.text + ' : ' + allcity2.text + '명') + '\n' + str(
            allcity3.text + ' : ' + allcity4.text + '명') + '\n' + str(
            allcity5.text + ' : ' + allcity6.text + '명') + '\n' + str(
            allcity7.text + ' : ' + allcity8.text + '명') + '\n' + str(
            allcity9.text + ' : ' + allcity10.text + '명') + '\n' + str(allcity11.text + ' : ' + allcity12.text + '명')
        allcity = str(allcity_all) + str(allcity__all)
        print()
        print(allcity)
        print()

        re = str(input('다시 검색하시겠습니까? (y,n) : '))
        if re == 'y' or 'Y':
            print()
            full = str(input(''' 
코로나 검색하고 싶은 사항을 입력하세요.
1. 전국 코로나 현황 / 2. 전국 지역별 비율 / 3. 표로 추출하기 / 4. 나가기

숫자를 입력하세요. : '''))
        else:
            print()
            print('다시 실행하세요.')
            break

    if full == '3':
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        # 현재 페이지에서 table 태그 모두 선택하기
        tables = soup.select('table')

        # 하나의 테이블 태그 선택하기
        table = tables[0]

        # 테이블 html 정보를 문자열로 변경하기
        table_html = str(table)

        # 판다스의 read_html 로 테이블 정보 읽기
        table_df_list = pd.read_html(table_html)

        # 데이터프레임 선택하기
        table_df = table_df_list[0]
        #print(table_df)
        #print(table_df[])
        #counting = table_df['확진환자']
        #print(type(counting))

        #print(table_df['시도명'])

        table_df2 = table_df['확진환자 (명)']
        table_df3 = table_df2['확진환자']
        #table_df5 = pd.DataFrame(table_df)
        #table_df4 = pd.DataFrame(table_df3)
        #print(df)
        table_df4 = table_df3[1:19]
        table_df4.index = ['서울','부산','대구','인천','광주','대전','울산','세종','경기','강원','충북','충남','전북','전남','경북','경남','제주','검역']
        table_df4.index.names = ['지역명']
        #print(table_df4)

        table_df5 = pd.DataFrame(table_df4)
        print(table_df5)


        xpos = numpy.arange(len(table_df4.index))
        xtext = list(table_df4.index)
        table_df4.plot.barh(color='#3988f7', rot=0, width=0.7)
        pyplot.grid()
        pyplot.legend()
        pyplot.title("시도 별 확진자 수")
        pyplot.ylabel("지역 명")
        pyplot.xlabel("확진자 수")
        pyplot.yticks(xpos, xtext)
        pyplot.xlim(0, 7000)

        # 그래프에 텍스트 표시하기
        # 그래프에 표시되는 실 데이터는 y축 좌표를 의미하고, x축은 0부터 시작하는 좌표값을 갖는다.
        for x, y in enumerate(list(table_df4)):
            txt = "%d명" % y
            pyplot.text(y, x, txt, fontsize=12, color='#207bfa',
                        horizontalalignment='left', verticalalignment='center')
        pyplot.show()

        print()
        exinp = input('엑셀로 저장하시겠습니까? (y/n) : ')

        if exinp =='y':
            exinp1 = input('엑셀 파일 명을 입력하세요.(ex: test_) : ')
            table_df.to_excel("%s1.xlsx" % exinp1)
            table_df4.to_excel("%s2.xlsx" % exinp1)
            print('파일 저장 완료')

        else :
            re = str(input('종료 하시겠습니까? (y,n) : '))
            if re =='n':
                full = str(input(''' 
코로나 검색하고 싶은 사항을 입력하세요.
1. 전국 코로나 현황 / 2. 전국 지역별 비율 / 3. 표로 추출하기 / 4. 나가기

숫자를 입력하세요. : '''))
            else:
                break


    if full == '4':
        re = str(input('종료 하시겠습니까? (y,n) : '))
        if re == 'Y' or 'y':
            break
        else:
            full = str(input(''' 
코로나 검색하고 싶은 사항을 입력하세요.
1. 전국 코로나 현황 / 2. 전국 지역별 비율 / 3. 표로 추출하기 / 4. 나가기

숫자를 입력하세요. : '''))