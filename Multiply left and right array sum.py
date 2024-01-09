#User function Template for python3

def multiply (arr, n) : 
    #Complete the function
    f = 0
    s = 0
    for i in range(n // 2):
        f += arr[i]
    if n % 2 == 0:
        for i in range(n // 2, n, 1):
            s += arr[i]
    else:
        for i in range((n // 2), n, 1):
            s += arr[i]
    return f * s



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = multiply(arr, n)
    print(ans)
# } Driver Code Ends
