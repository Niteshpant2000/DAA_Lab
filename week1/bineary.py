t=int(input())
for i in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    key=int(input())
    first=0
    last=n-1
    count=0
    flag=0
    while(first<=last):
        m=first+(last-first)//2

        if(arr[m]<key):
            first=m+1
        elif(arr[m]>key):
            last=m-1
        else:
            flag=1
            count+=1
            break
        count+=1
    if(flag==1):
        print(f"Present {count}")
    else:
        print(f"Not Present {count}")
        
    
    

