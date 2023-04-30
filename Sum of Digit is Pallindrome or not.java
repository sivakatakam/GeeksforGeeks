//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            int N = Integer.parseInt(read.readLine());
            Solution ob = new Solution();
            System.out.println(ob.isDigitSumPalindrome(N));
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    int isDigitSumPalindrome(int N) {
        // code here
        int s=0,r=0,s1,rev=0;
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
}