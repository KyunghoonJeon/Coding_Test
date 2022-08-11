import sys
input=sys.stdin.readline
n,m=map(int,input().split())
# 방문 위치를 저장하기 위한 맵을 생성
d=[[0]*m for _ in range(n)]
x,y,dir=map(int,input().split())
d[x][y]=1 # 현재 위치는 방문 처리

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

# 북,동,남,서 방향 정의
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
    global dir
    dir-=1
    if dir==-1:
        dir=3

# 시뮬 시작
cnt=1
turn_time=0
while True:
    turn_left()
    nx=x+dx[dir]
    ny=y+dy[dir]
    if d[nx][ny]==0 and arr[nx][ny]==0: # 방문하지 않았고 육지인 지점
        d[nx][ny]=1
        x,y=nx,ny
        cnt+=1
        turn_time=0
        continue
    else:
        turn_time+=1
    # 네 방향 모두 막혔다면?
    if turn_time==4:
        nx=x-dx[dir]
        ny=y-dy[dir]
        if arr[nx][ny]==0:
            x,y=nx,ny
        else:
            break
        turn_time=0
print(cnt)