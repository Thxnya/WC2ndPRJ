import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
from datetime import datetime

def crawling():
    # 1~10페이지까지 날짜와 환율 모두 가져오기
    # 빈 리스트 생성
    date_lst = []
    exchange_lst = []

    # 환율정보 1~5페이지 크롤링
    for p in range(1,6):
        url = f'https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW&page={p}'

        html = requests.get(url)

        soup = bs(html.text, 'html.parser')

        for i in range(10):
            date_lst.append(soup.select('.date')[i].text)

        for j in range(0,19,2):
            exchange_lst.append(soup.select('.num')[j].text.replace(',', ''))

    date_lst.reverse()
    exchange_lst.reverse()

    exchange_lst = list(map(float, exchange_lst))

    df = pd.DataFrame({'date' : date_lst, 'exchange' : exchange_lst})

    return df

def graph(df):
    # 그래프 크기 지정하기 = 너비, 높이
    plt.rcParams['figure.figsize'] = (16,4)
    # 선의 두께 지정
    plt.rcParams['lines.linewidth'] = 2

    # 데이터 넣기
    plt.plot(df['date'], df['exchange'])

    # 축 labeling
    grp_date = [df['date'][x] for x in range(5, len(df['date']), 5)]
    grp_exchanges = list(plt.gca().get_yticks())
    plt.xticks(grp_date, [datetime.strptime(d, '%Y.%m.%d').strftime('%b %d') for d in grp_date])
    plt.yticks(grp_exchanges, [f'{e:,.0f}' for e in grp_exchanges])

    plt.gca().tick_params(colors='#EEEEEE', labelcolor='black')

    # 범위지정
    plt.xlim(df['date'].iloc[0], df['date'].iloc[-1])

    # 그래프 내에 그리드선 표시하기
    plt.grid(True, color='#EEEEEE')

    # 테두리 제거
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)

    plt.savefig('./static/img/grp.png')