import pyupbit
import numpy as np

# OHLCV(시가, 고가, 저가, 종가, 거래량 대한데이터 )
df = pyupbit.get_ohlcv("KRW-BTC", count=240)  # 비트코인을 7일간에

# 변동폭 *k 계산 고가-저가 *k
df['range'] = (df['high'] - df['low']) * 0.4
df['target'] = df['open'] + df['range'].shift(1)

# ror(수익률)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

# 누적 수익률
df['hpr'] = df['ror'].cumprod()

# draw down 계산
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# MDD 계산
print("MDD(%): ", df['dd'].max())

# 엑셀 출력
df.to_excel("dd.xlsx")
