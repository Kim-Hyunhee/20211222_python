
my_money = 1000

rate = float(input('연 수익률 입력 : '))

# 몇 년 후에 2배가 되는가?
year = 0   # 0년에서 시작. 1년 지날 때마다 이자를 받는다.

while True:
    # 1년 지났다고 명시
    year = year + 1
    
    # 내 돈에 이자율 적용 => 자산 증식
    my_money = my_money * (1 + rate  / 100)
    
    # 내 돈이 얼마가 되었는가?
    print(f'{year}년차 자산 : {my_money}')
    
    # 가진 돈이 2배가 되었는가? 내 돈이 2천 이상인가?
    if my_money >= 2000:
        break

# 몇 년 만에 2배를 넘었나?
print(f'{year}년 만에 2배를 넘었습니다.')