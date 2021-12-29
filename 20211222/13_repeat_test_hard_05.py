num_str = input('369 판별 숫자 입력 :')

clap_count = 0

# 한 글자씩 검사 => 문자열의 한 글자씩 추출
for i in range(len(num_str)):
    
    # 자리에 맞는 문구가 3 or 6 or 9 => [3,6,9] 중 하나? => 박수를 한 번 더 쳐야 함
    if num_str[i] in ['3','6','9']:  # in : 뒤에 있는 목록에 들어있는가? bool 리턴
    # if num_str[i] == '3' or num_str[i] == '6' or num_str[i] == '9':
        clap_count += 1
        
# clap_count에 0이냐 아니냐에 따라 박수 / 숫자 갈림
if clap_count == 0:
    print(num_str)
    
else:
    # 박수 1회 이상 쳐야 함
    for i in range(clap_count):
        print("짝!",end ='')