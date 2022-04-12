class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> arr;
        vector<int> result;
        
        for(int idx=0; idx<nums.size(); idx++)
        {
            arr.insert({nums[idx], idx});
        }

        for(int i=0; i<nums.size(); i++)
        {
            int k = target - nums[i];
            auto iter = arr.find(k);
            if(iter == arr.end() || iter->second == i) { continue; }
            else
            {
                result.push_back(i);
                result.push_back(iter->second);
                break;
            }
        }
            
        return result;
    }
};