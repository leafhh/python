import pyupbit

access = "j7MQ50muhm12e3Cj4jZkP8oag6rixxcskKux6269 "          # 본인 값으로 변경
secret = "cEErJUv1LzJmkswjjHOgWNWRP4qW4nEoEYzP4ZlP"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
