# 1 ~ 10까지의 숫자를 for로 출력

for i in range(1, 11):
    print(i)
    
    # 5의 배수를 찾아냈다면 반복 종료.
    if i % 5 == 0:
        # break로 반복을 강제 종료.
        break

print('-----------------')
# 1 ~ 10까지의 숫자를 for로 출력
for i in range (1, 11):
    
    # i 값이 3의 배수인가? => 맞으면 출력 X
    if i % 3 ==0:
        continue
    
    print(i)


print('프로그램 종료')