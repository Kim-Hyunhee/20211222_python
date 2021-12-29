num = int(input( '제곱될 숫자 입력 :'))


# 2 => 3 * 3
# 5 => 3 * 3 * 3 * 3 * 3   => 입력한 숫자만큼 횟수로 반복

# 곱셈은 0으로 출발하면 반복적으로 0 을 곱하게됨
# 1부터 출발
result = 1

# 정석 풀이 반복문 직접 작성

for i in range(num):
    result = result * 3


# 검색 풀이 파이썬 내장 함수 활용

result = pow(3, num)

   
print(result)
    
