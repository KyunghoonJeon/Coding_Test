# 나의 틀린 풀이(0의 경우는 생각하였지만, 1의 경우를 생각못함(1같은 경우는 더하는것이 이득이다.))
# s=input()
# num_list=[]
# for i in s:
#     num_list.append(int(i))
# result=1
# for i in num_list:
#     if i!=0:
#         result*=i
#     if i==0:
#         result+=i
# print(result)

s=input()
result=int(s[0])

for i in range(1,len(s)):
    # 두 수 중에서 하나라도 0 혹은 1인 경우, 곱하기 보다는 더하기 수행
    num=int(s[i])
    if num<=1 or result<=1:
        result+=num
    else:
        result*=num
print(result)