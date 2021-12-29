
# 561 => 56으로 변환 (10으로 나눈 몫이 얼마? // : 몫 구하기)  => 1의 자리?
num = 7
i = 1

count = 0

while True:
    # num의 십의 자리가 6인가?
    if ((num // 10) % 10) == 6 :
        
        count = count + 1
        if count ==2:
            break
        
    i = i + 1
    num = 7 * i

print(num)    