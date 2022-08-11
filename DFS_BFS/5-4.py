def recursive_function(i):
    if i==100:
        return
    print(i,'번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료합니다.')
recursive_function(1)

# 재귀는 내부적으로 스택 자료구조와 동일하다. 