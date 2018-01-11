arr = list(map(int, input().strip().split(' ')))

mysum=sum(arr)
maxsum=mysum-min(arr)
minsum=mysum-max(arr)
print(maxsum+' '+ minsum)
