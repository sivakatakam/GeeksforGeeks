#User function Template for python3
class Solution:
	def removeCharacters(self, S):
		# code here
		s = ''
		for i in S:
		    o = ord(i)
		    if o > 47 and o < 58:
		        s += i
		return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeCharacters(s)
		
		print(answer)


# } Driver Code Ends
