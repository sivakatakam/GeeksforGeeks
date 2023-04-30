//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int isDigitSumPalindrome(int N) {
        // code here
        int r=0,s=0,s1,rev=0;
        while(N!=0)
        {
            r=N%10;
            N=N/10;
            s=s+r;
        }
        s1=s;
        while(s!=0)
        {
            r=s%10;
            s=s/10;
            rev=rev*10+r;
        }
        if(rev==s1)
        return 1;
        else
        return 0;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        Solution ob;
        cout << ob.isDigitSumPalindrome(N) << "\n";
    }
}

// } Driver Code Ends
