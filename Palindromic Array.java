//{ Driver Code Starts
import java.util.*;
class PalindromicArray{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0)
		{
			int n = sc.nextInt();
			int[] a = new int[n];
			for(int i = 0 ;i < n; i++)
				a[i]=sc.nextInt();
			GfG g = new GfG();
			System.out.println(g.palinArray(a , n));
		}
	}
}
// } Driver Code Ends


/*Complete the Function below*/
class GfG
{
	public static int palinArray(int[] a, int n)
           {
                  //add code here.
                  int i,c=0;
                  for(i=0;i<n;i++)
                  {
                      int n1=a[i],rev=0,r;
                      while(n1!=0)
                      {
                          r=n1%10;
                          n1=n1/10;
                          rev=rev*10+r;
                      }
                      if(rev==a[i])
                      c=1;
                      else
                      {
                          c=0;
                          break;
                      }
                  }
                  if(c==0)
                  return 0;
                  else
                  return 1;
           }
}