now=input()
row=int(now[1])
col=int(ord(now[0]))-int(ord('a'))+1
ways=[(1,2),(1,-2),(-1,2),(-1,2),(2,1),(2,-1),(-2,1),(-2,-1)]
cnt=0
for i in ways:
    nrow=row+i[0]
    ncol=col+i[1]
    if 1<=nrow<=8 and 1<=ncol<=8:
        cnt+=1
print(cnt)