class Solution
{
    public:
    //Function to find a continuous sub-array which adds up to a given number.
    vector<int> subarraySum(int arr[], int n, long long s)
    {
        // Your code here
        int start, end;
        start=0, end=1;
        
        long long currentSum = arr[0];
        
        bool flag = false;
        while(end < n+1)
        {
            while((currentSum > s) && (start < end))
            {
                currentSum -= arr[start];
                start += 1;
            }
            
            if(currentSum == s)
            {
                flag = true;
                break;
            }
            
            if(end < n)
            {
                currentSum += arr[end];
            }
            
            end += 1;
        }
        
        if(flag == true)
        {
            return {start+1,end};
        }
        else
        {
            return {-1};
        }
    }
};