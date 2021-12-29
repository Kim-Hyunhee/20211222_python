# # 연습문제 1. Hello 문장을 5번 출력.

# for i in range(5):
#     print('Hello')
    
# print('===============')

# # 연습문제 2. 1 ~ 100 사이의 7의 배수 출력

# for i in range(1,101):
#     if i % 7 == 0:
#         print(i)
        
# print('===============')

# # while True => if 조건 : break로 빠져나오는 양식

# # 연습문제 3. 키보드로 숫자를 입력 받는 것을 반복하다가 0을 입력하면 종료
# #   => 0을 넣을 때까지 계속 반복

# while True:
#     input_num = int(input('정수 입력 : '))
    
#     if input_num == 0:
#         break
    
# print('프로그램 종료.')

# print('===============')

# 연습문제 4. 1+2+3+...+? 100을 넘어가게 하는 숫자 찾기
# while True => if 합산결과 >= 100 이면 종료 (그때 더해진 숫자 출력)

# 합산 결과를 저장한 변수
result = 0

# while을 돌면서 숫자를 늘려나갈 변수
num = 1

# 무한 반복 -> result >= 100이상이 되면 종료

while True:
    # 1 + 2 + 3 + 4 + .... 반복 합산되게
    result = result + num
    
    # 더해졌을 때, 결과가 100을 넘어가는가?
    if result >= 100:
        break
    
    # 더해지고 나면 num은 1씩 증가
    num = num + 1
    
    
# 반복을 빠져나왔을 때 num에 저장된 값 => 100을 넘게 만든 숫자
print(f'정갑 : {num}')

print('프로그램 종료.')