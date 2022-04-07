/* The function should return the index of any
   peak element present in the array */

// arr: input array
// n: size of array
class Solution
{
    public:
    int peakElement(int arr[], int n)
    {
       // Your code here
       int i=n/2;
       if(n == 1)
       {
           return i;
       }
       if(n == 2)
       {
           if(arr[0] > arr[1]) { return 0; }
           else { return 1; }
       }
       else
       {
           int l=0, h=n-1;
           while(l<=i && i<=h)
           {
               if(i == 0 && arr[i] >= arr[i+1]) { return i; }
               if(i == (n-1) && arr[i-1] <= arr[i]) { return i; }
               if(arr[i-1] <= arr[i] && arr[i] >= arr[i+1]) { return i; }
               if(arr[i-1] <= arr[i+1])
               {
                   l = i;
                   i = (h+i+1)/2;
               }
               else
               {
                   h = i;
                   i = (l+i-1)/2;
               }
           }
           return i;
       }
    }
};