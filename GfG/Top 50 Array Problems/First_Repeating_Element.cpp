class Solution {
  public:
    // Function to return the position of the first repeating element.
    int firstRepeated(int arr[], int n) 
    {
        unordered_map<int,int> temp;
        temp.insert({arr[0],1});
        
        int idx_temp, flag = 0;
        
        for(int i=1; i<n; i++)
        {
            auto iter = temp.find(arr[i]);
            if(iter == temp.end())
            {
                temp.insert({arr[i], i+1});
            }
            else
            {
                if(flag == 0) 
                { 
                    idx_temp = (iter->second), flag = 1; 
                }
                else if(idx_temp > (iter->second))
                {
                    idx_temp = (iter->second); 
                }
            }
        }
        
        if(flag == 0)
        {
            return -1;
        }
        else
        {
            return idx_temp;
        }
    }
};