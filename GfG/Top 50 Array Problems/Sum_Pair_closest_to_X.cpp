class Solution{   
public:
    vector<int> sumClosest(vector<int>arr, int x)
    {
        // code here
        int min_ = INT_MAX;
        int idx = 0, jdx = arr.size()-1;
        int fp, sp;
        
        while(idx < jdx)
        {
            if(abs(x-arr[idx]-arr[jdx]) < min_)
            {
                min_ = abs(x-arr[idx]-arr[jdx]);
                fp = idx, sp = jdx;
            }
            if(arr[idx]+arr[jdx] > x)
            {
                jdx--;
            }
            else
            {
                idx++;
            }
        }
        
        return {arr[fp], arr[sp]};
    }
};