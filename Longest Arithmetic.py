def longArith(line,length):
    diff=[]
    for i in range(length-1):
        diff.append(line[i+1]-line[i])
    return (sameCheck(diff,length-1))

def sameCheck(arr, n): 
    ans, temp = 1, 1
    for i in range(1, n):
        if arr[i] == arr[i - 1]: 
            temp = temp + 1
        else: 
            ans = max(ans, temp) 
            temp = 1
                  
    ans = max(ans, temp)  
    return (ans+1)

if __name__ == "__main__": 
    ans=[]  
    t=int(input())
    for test in range(t):
        length=int(input())
        line=[int(i) for i in input().split()]
        ans.append(longArith(line, length))
    for test in range(t):
        print("Case #"+str(test+1)+": "+str(ans[test]))