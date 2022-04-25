class Solution {
  public:
    int getMinDiff(int arr[], int n, int k) {
        // code here
        sort(arr, arr+n);
        int ans = arr[n-1] - arr[0];
        int smallest = arr[0]+k, largest = arr[n-1]-k;
        int min_e, max_e;
        
        for(int i=1; i<n; i++)
        {
            if(arr[i]-k < 0)
            continue;
            min_e = min(smallest, arr[i]-k);
            max_e = max(arr[i-1]+k, largest);
            ans = min(ans, max_e-min_e);
        }
        
        return ans;
    }
};