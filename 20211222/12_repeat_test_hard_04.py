num = int(input('숫자 입력 :'))

# num에는 몇자리? 알기 어렵다.

result = 0    #합산 결과를 저장할 변수

while True:
    # 일의 자리를 추출 => 합산
    
    # 일의 자리 추출 => 10으로 나눈 나머지 : 일의 자리
    last_digit = num % 10
    
    result = result + last_digit
    
    # 54321 => 1 더함 : 54321 => 5432로 변경 => 마지막 자리는 제거하자 => 54321 / 10의 몫? 5432
    num = num // 10
    
    # 마지막자리 제거한 num이 0이라면? 무한 반복 탈출
    if num == 0:
        break

print(result)        


num_str = input("숫자 입력 : ")

# str => len(str)  :  몇 글자인지
# str => str[0]  :  맨 앞 글자  [index]  => 해당 위치 글자


result = 0
for i in range(len(num_str)):
    digit = int(num_str[i])  # str 각 자리 => int로 변환 => 합산만 해주면 끝
    result = result + digit
    
print(result)
    
    