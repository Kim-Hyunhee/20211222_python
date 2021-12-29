# 1번 5줄 5칸
for i in range(5):
    
    for j in range(5):
       
        print(f'[{i},{j}]',end ='')
        
    # 한줄 출력 완료 ->  다음 줄로 넘어가게   
    print()        

print('===========================')

# 2번 - 가운데만 세로로 출력        
for i in range(5):
    
    for j in range(5):
        
        # 조건이 맞으면 좌표, 아니면 빈칸 5개
        if j == 2:
            print(f'[{i},{j}]', end ='')
        else:
            print('     ',end='')
            
    print()

print('===========================')
# 3번 - 우상향 대각선 - 2번 문제와 조건만 다르면 해결됨

for i in range(5):
    
    for j in range(5):
        
        # 조건이 맞으면 좌표, 아니면 빈칸 5개
        if i + j ==4:
            print(f'[{i},{j}]', end ='')
        else:
            print('     ',end='')
    print()

print('===========================')    
# 4번 - X 자 그리기

for i in range(5):
    
    for j in range(5):
        
        # 조건이 맞으면 좌표, 아니면 빈칸 5개
        if i + j ==4 or i == j:
            print(f'[{i},{j}]', end ='')
        else:
            print('     ',end='')
    print()

print('===========================')    
# 5번 - ㅁ자 그리기

for i in range(5):
    
    for j in range(5):
        
        # 조건이 맞으면 좌표, 아니면 빈칸 5개
        if i==0 or j == 4 or i ==4 or j==0:
            print(f'[{i},{j}]', end ='')
        else:
            print('     ',end='')
    print()
    