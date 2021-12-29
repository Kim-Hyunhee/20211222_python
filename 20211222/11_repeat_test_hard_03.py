num = int(input('정수 입력 : '))

# 소수가 맞는지 아닌지 판별 결과를 저장할 변수
is_prime_num = True      # 2 ~ 입력숫자 직전까지 나눠떨어지는 숫자 발견 => 아니라고 말 바꿈

divide_num = 0

for i in range(2, num):
    # 입력한 숫자 % 1 == 0? 나눠지는 숫자 발견 => 더 이상 소수가 아니다.
    
    if num % i == 0:
        # 한 번이라도 들어오면 소수가 아님 => 결론 났으면 더 반복할 필요가 없다.
        is_prime_num = False
        # 왜 소수가 아닌지 나눠 떨어진 숫자 i를 보관해두자
        divide_num = i
        
        # 하나 찾는 순간 반복 종료
        break
        
# is_prime_num 변수가 True로 유지되어 있으면? 한 번도 나눠 떨어진 적이 없다.

if is_prime_num :
    print(f'{num}는 소수가 맞습니다.')
else:
    print(f'{num}는 소수가 아닙니다.')
    print(f'{divide_num}으로 나눠떨어집니다.')
    


# 추가 문제 => 입력 받은 숫자까지의 제일 큰 소수?

# ex. 33 소수? 아니면 32 소수? 아니면 31 소수? ... 2 소수? 무조건 OK.
num = int(input('정수 입력 : '))
largest_prime_num = 0

for i in range(num, 1, -1):
    
    # 각 i가 소수가 맞는가? 맞다면 마지막에 별도로 출력 => largest_prime_num에 담아두자
    # 나눠 떨어지는 숫자만 담아보자
    divide_num = 0  # 끝까지 0으로 유지되면 한 번도 나눠지지 않은 (소수가 맞다)
    
    for j in range(2, i):   # 매번 반복되는 i가 소수가 맞는지 검사하는 for
        if i % j == 0:
            # 나눠지는 숫자 발견!
            divide_num = j
            break
        
    # divide_num이 0인가? 소수를 찾아냈다!  => 제일 큰 소수 발견, i for문도 종료
    if divide_num ==0:
        largest_prime_num = i
        break
    

# 제일 큰 걸로 판명된 소수 출력
print(f'입력한 {num}까지의 제일 큰 소수 : {largest_prime_num}')

        
    