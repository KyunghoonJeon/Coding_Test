import collections
import sys
input=sys.stdin.readline

def solution(X,Y):
    lst1=[]
    lst2=[]
    for i in X:
        lst1.append(i)
    for i in Y:
        lst2.append(i)

    ct1=collections.Counter(lst1)
    ct2=collections.Counter(lst2)

    lst=list((ct1&ct2).elements())
    lst.sort(reverse=True)
    if lst==[]:
        return '-1'
    elif set(lst)=={'0'}:
        return '0'
    else:
        result=''.join(lst)
        return result
