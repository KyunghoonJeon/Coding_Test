def solution(topping):
    l=len(topping)
    answer=0
    for i in range(l):
        lst1=topping[:i]
        lst2=[x for x in topping if x not in lst1]
        set1=set(lst1);set2=set(lst2)
        if len(set1)==len(set2):
            answer+=1
    return answer

print(solution([1,2,1,3,1,4,1,2]))