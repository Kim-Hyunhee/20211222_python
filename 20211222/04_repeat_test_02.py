num = int(input('총 합을 구할 숫자 : '))

result = 0

# 정석 풀이 1 => for를 이용해서 반복 누적 합산
# 장점 : 코드 이해가 쉽다
# 단점 : 연산 횟수가 많아진다 => 계산이 오래 걸릴 소지가 있다.

for i in range(1,num+1):
    result = result + i

print(f'총 합 : {result}')


# 수학적 풀이 2 => 1 ~ n 까지의 총합? 공식 존재 => n * (n+1) / 2
# 장점 : 반복 X 연산 3번만에 결과 도출 => 속도가 빠르다
# 단점 : 코드 이해가 어렵다

result = num * (num+1) / 2

print(f'총 합 : {result}')