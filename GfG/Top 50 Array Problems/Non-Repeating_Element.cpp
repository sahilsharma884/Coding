class Solution{
    public:
    int firstNonRepeating(int arr[], int n) 
    { 
        // Complete the function
        unordered_map<int, int> temp;
        
        for(int i=0; i<n; i++)
        {
            auto iter = temp.find(arr[i]);
            if(iter == temp.end()) { temp.insert({arr[i], 1}); }
            else { iter->second += 1; }
        }
        
        for(int i=0; i<n; i++)
        {
            if(temp.find(arr[i])->second == 1) { return arr[i]; }
        }
        
        return 0;
    } 
  
};