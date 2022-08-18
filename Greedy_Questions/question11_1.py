import sys
input=sys.stdin.readline

n=int(input())
people=list(map(int,input().split()))
people.sort() # 정렬해서 한 길드에 적은 수가 담기게 하기

result=0 # 총 그룹의 수
cnt=0 # 한 그룹 내의 사람 수

for i in people:
    cnt+=1
    if cnt>=i:
        result+=1
        cnt=0
print(result)
