#User function Template for python3

class Solution:
    def getAreas(self, L , W , B , H , R):
        # code here
        l = [0, 0, 0]
        l[0] = L * W
        l[1] = int(0.5 * B * H)
        l[2] = int(3.14 * R * R)
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        L,W,B,H,R=map(int,input().split())
        
        ob = Solution()
        ptr = ob.getAreas(L,W,B,H,R)
        
        print(ptr[0],ptr[1],ptr[2])
# } Driver Code Ends
