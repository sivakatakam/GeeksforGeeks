#User function Template for python3

class Solution:
    def lastIndex(self, s):
        # code here
        if '1' in s:
            a = 0
            c = 0
            for i in s:
                if i == '1':
                    a = c
                c += 1
            return a
        else:
            return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	s = input()
    	ob = Solution()
    	print(ob.lastIndex(s))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
