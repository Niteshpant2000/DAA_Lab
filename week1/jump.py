import math
t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split(" ")))
    key=int(input())
    jump=int(math.sqrt(n))
    prev=0
    step=jump
    comp=0
    flag=0
    while(arr[int(min(n,step))-1] <key):
        comp+=1
        prev=step
        step+=jump
    for i in range(prev,step+1):
        comp+=1
        if(arr[i]==key):
            print(f"Present {comp}")
            break
    if(flag==0):
        print(f"not present {comp}")
    


