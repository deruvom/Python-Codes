def f(s):
    return 'a' in s
    
def satisfiesF(L):
    m = list(L)
    if m ==[]:
        return []
    for s in m:
        print s, f(s), L
        if not f(s):
            L.remove(s)
    
    return len(L)


    
    

L=['a','b','a']
print satisfiesF(L)

