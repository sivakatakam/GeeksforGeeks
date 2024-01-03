Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #User function Template for python3
... class Solution:
... 	def isPalindrome(self, S):
... 		# code here
... 		if S == "".join(reversed(S)):
... 		    return 1
... 		else:
... 		    return 0
... 
... 
... #{ 
...  # Driver Code Starts
... #Initial Template for Python 3
... 
... if __name__ == '__main__':
... 	T=int(input())
... 	for i in range(T):
... 		S = input()
... 		ob = Solution()
... 		answer = ob.isPalindrome(S)
... 		print(answer)
... 
