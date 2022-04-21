class Solution{
    public:
    // arr: input array
    // n: size of array
    //Function to find the sum of contiguous subarray with maximum sum.
    long long maxSubarraySum(int arr[], int n){
        long long sum_ = arr[0];
        long long temp = sum_;
        bool neg = false;
    
        for(int i=1; i<n; i++)
        {
            if(sum_ < 0) 
            {
                if(sum_ < arr[i]) 
                { 
                    temp = arr[i];
                    sum_ = arr[i]; 
                }  
                neg = true; 
            }
            else if(sum_+arr[i] < 0)
            {
                neg = true;
                continue;
            }
    
            if(neg == true && arr[i] >= 0)
            {
                if(temp < sum_) { temp = sum_; }
                sum_ = arr[i];
                if(temp < sum_) { temp = sum_; }
                neg = false;
            }
            else if(sum_+arr[i] >= 0)
            {
                sum_ += arr[i];
                if(temp < sum_) { temp = sum_; }
            }
        }
    
        if(temp < sum_) { temp = sum_; }
    
        return temp;
    }
};