// My approach:
// using hash table unordered_map, vector and sort function

class Solution{
  public:
    vector<int> duplicates(int arr[], int n) {
        // code here
        unordered_map<int, int> dup_list; // take O(1)
        vector<int> result;
        int i, count = 0;
        
        for(i=0; i<n; i++)
        {
            auto itr = dup_list.find(arr[i]);
            if(itr == dup_list.end())
            {
                dup_list.insert({arr[i],1});
                count += 1;
            }
            else
            {
                itr->second += 1;
            }
        }
        
        if(count == n)
        {
            return {-1};
        }
        else
        {
            for(auto itr=dup_list.begin(); itr!=dup_list.end(); itr++)
            {
                if(itr->second > 1)
                {
                    result.push_back(itr->first);
                }
            }
            sort(result.begin(), result.end());
            return result;
        }
    }
};

// After learning the approach by others as accuracy was not good for my approach.
class Solution{
  public:
    vector<int> duplicates(int arr[], int n) {
        // code here
        vector<int> result;
        int i;
        
        for(i=0; i<n; i++)
        {
            arr[arr[i]%n] += n;
        }
        
        
        for(i=0; i<n; i++)
        {
            if((arr[i]/n)>1)
            {
                result.push_back(i);
            }
        }
        
        if(result.size() == 0)
        {
            return {-1};
        }
        else
        {
            return result;
        }
    }
};