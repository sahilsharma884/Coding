class Solution{   
public:
    int getPairsCount(int arr[], int n, int k) {
        // code here
        unordered_map<int, int> occ_num;
        int count_pair = 0;
        
    	for(int i=0;i<n;i++)
    	{
    		auto iter = occ_num.find(arr[i]);
    		if(iter == occ_num.end()) { occ_num.insert({arr[i],1}); }
    		else { iter->second += 1; }
    	}
    
    	for(int i=0;i<n;i++)
    	{
    		auto iter1 = occ_num.find(arr[i]);
    		iter1->second -= 1;
    
    		int target = k - arr[i];
    		auto iter2 = occ_num.find(target);
    		if(iter2 == occ_num.end()) { continue;}
    		else if(iter2->second != 0) { count_pair += iter2->second; }
    	}
    	
    	return count_pair;
    }
};