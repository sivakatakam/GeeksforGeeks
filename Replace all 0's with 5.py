# Function should return an integer value
def convertFive(n):
    # Code here
    n = str(n)
    s = ''
    for i in n:
        if i == '0':
            s = s + '5'
        else:
            s = s + i
    return int(s)


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
# } Driver Code Ends
