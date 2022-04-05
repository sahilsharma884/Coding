class Solution{
  public:
    int MissingNumber(vector<int>& array, int n) {
        // Your code goes here
        int total_sum = (n*(n+1)/2);
        int i;
        
        for(i=0; i<n-1; i++)
        {
            total_sum -= array[i];
        }
        
        return total_sum;
    }
};