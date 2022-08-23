import collections

def solution(want,number,discount):
    dictionary=dict((zip(want,number)))
    l=len(discount)
    count=0
    for i in range(l-9):
        cnt=collections.Counter(discount[i:i+10])
        if  dictionary==cnt:
            count+=1
    return count