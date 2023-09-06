#User function Template for python3

class Solution:
    def sumOfDigits (self, N):
        # code here
        s=0
        while N!=0:
            r=N%10
            N=N//10
            s=s+r
        return s
