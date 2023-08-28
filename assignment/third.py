def mergesort(arr1,arr2,n,m,arr):
    arr=[None]*(n+m)
    i=j=k=0
    while(i<n and j<m):
        if(arr1[i]<arr2[j]):
            arr[k]=arr1[i]
            i+=1 
            k+=1 
        else:
            arr[k]=arr2[j]
            j+=1 
            k+=1 
    while (i<n):
        arr[k]=arr1[i]
        i+=1
        k+=1
    while(j<m):
        arr[k]=arr2[j]
        k+=1
        j+=1
    return arr
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
n=len(arr1)
m=len(arr2)
arr=[]
print(mergesort(arr1,arr2,n,m,arr))
