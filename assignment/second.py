def fun(arr):
  
    m=[]
    n=[]
  
    for i in range(len(arr)):
        if arr[i]<value:
            
            m.append(arr[i])
        else:
            n.append(arr[i])
    return m,n
   
arr=list(map(int,input().split()))
value=int(input())
arr.sort()

print(fun(arr))
