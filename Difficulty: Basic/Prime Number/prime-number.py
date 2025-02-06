#User function Template for python3

class Solution:
    def isPrime(self, n):
        # code here
        c=0
        for i in range(1,int(n**0.5)+1,1):
            if(n%i)==0: c+=1
        return c==1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n = int(input())  # Read the number to check primality

        ob = Solution()
        # Using Python's conditional expression for true/false
        print("true" if ob.isPrime(n) else
              "false")  # Print "true" if prime, else "false"
        print("~")

# } Driver Code Ends