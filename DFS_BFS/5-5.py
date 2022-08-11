# 반복적으로 구현한 팩토리얼
def factorial_iterative(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

# 재귀적으로 구현한 팩토리얼
def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)

print("반복적으로 구현:", factorial_iterative(5))
print("재귀적으로 구현:", factorial_recursive(5))

# 재귀 함수를 사용했을 때 얻을 수 있는 장점?? --> 코드가 더 간결
# 재귀 함수는 수학의 점화식을 그대로 소스코드로 옮긴 것