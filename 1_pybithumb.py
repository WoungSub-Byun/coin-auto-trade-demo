import datetime
import pybithumb

# ticker: 주식에서 각 종목에 6자리 고유번호를 붙이는 것처럼 붙인 고유 번호
# - 3자리 이상의 대문자
# - ex) Bitcoin: BTC

# 1.
# get_tickers
# - 현재 빗썸거래소에서 거래되고 있는 모든 가상화폐의 목록
# - return: list
tickers = pybithumb.get_tickers()
print("현재 빗썸에서 거래되고 있는 가상화폐들: {}".format(tickers))
print("현재 빗썸에서 거래되고 있는 가상화폐의 수: {}개".format(len(tickers)))

# 2.
# get_current_price(*ticker)
# - 특정 가상화폐의 현재가 반환
# - return: float
price = pybithumb.get_current_price("BTC")
print(price)

# 현재 빗썸에서 거래되고 있는 화폐들의 현재가 모두 출력
# num = 0
# for ticker in tickers:
#     if num > 20:
#         time.sleep(1)
#         num = 0
#     price = pybithumb.get_current_price(ticker) # 초당 20회 제한
#     print("{}의 현재가: {}원".format(ticker, price))
#     num += 1

# 3.
# .get_market_detail(*ticker)
# - 가상화폐의 최근 24시간동안의 저가, 고가, 거래금액, 거래량을 반환
# - return: tuple
detail = pybithumb.get_market_detail("BTC")
print("<최근 24시간 내의 Bitcoin 정보> \n 저가: {}원\n 고가: {}원\n 거래금액: {}원\n 거래량: {}원".format(format(detail[0], ','), format(detail[1], ','), format(detail[2], ','), format(detail[3], ',')))

# 현재 빗썸에서 거래되고 있는 화폐들의 디테일 정보들 모두 출력
# for ticker in tickers:
#     detail = pybithumb.get_market_detail(ticker)
#     print("<최근 24시간 내의 {} 정보> \n 저가: {}원\n 고가: {}원\n 거래금액: {}원\n 거래량: {}원".format(ticker, format(detail[0], ','),
#                                                                                        format(detail[1], ','),
#                                                                                        format(detail[2], ','),
#                                                                                        format(detail[3], ',')))

# 매도 호가(ask): 가상화폐를 팔고자 하는 사람이 제시한 가격과 수량
# 매수 호가(bid): 가상화폐를 사고자 하는 사람이 제시한 가격과 수량
# * 매도호가 > 매수 호가
# - 구매자와 판매자 모두 이윤을 남기려고 하기 때문에
#   평균적으로 판매가격(매도호가)은 구매가격(매수호가)보다 높습니다.

# 4.
# .get_order_book()
# - 호가 정보
# - return: Dictionary
# - keys: ['timestamp', 'payment_currency', 'order_currency', 'bids', 'asks']
# - timestamp(ms) : 조회한 시간 timestamp 출력
# - payment_currency: 현재 거래 시에 사용된 화폐
order_book: dict = pybithumb.get_orderbook("BTC")
print(list(order_book.keys()))
print(order_book)
print(datetime.datetime.fromtimestamp(int(order_book["timestamp"])/1000))

# 5.
# .get_current_price(*ticker)
# - 빗썸에서 거래되는 모든 가상화폐에 대한 현재가 조회
# - * 모든 가상화폐의 현재가 조회 => get_current_price("ALL")
btc_price = pybithumb.get_current_price("BTC")
print(btc_price)

all = pybithumb.get_current_price("ALL")
for k, v in all.items():
    print(k, v)

# - return value
# opening_price	최근 24시간 내 시작 거래금액
# closing_price	최근 24시간 내 마지막 거래금액
# min_price 최근	24시 간 내 최저 거래금액
# max_price 최근	24시 간 내 최고 거래금액
# average_price	최근 24시간 내 평균 거래금액
# units_traded	최근 24시간 내 Currency 거래량
# volume_1day	최근 1일간 Currency 거래량
# volume_7day	최근 7일간 Currency 거래량
# buy_price	거래 대기건 최고 구매가
# sell_price	거래 대기건 최소 판매가
# 24H_fluctate	24시간 변동금액
# 24H_fluctate_rate	24시간 변동률
