def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    
    if N >=0:
        if N%10 == N:
            return N
        return N%10 + sumDigits(N/10)

        
    