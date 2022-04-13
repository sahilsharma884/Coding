class Solution{
public:

	void rearrange(int arr[], int n) {
	    // code here
	    int temp[n], pos_idx, neg_idx;
	    pos_idx = -1, neg_idx = n;
        
        for(int i=0; i<n; i++)
        {
            if(arr[i] >=0 ) { temp[++pos_idx] = arr[i]; }
            else { temp[--neg_idx] = arr[i]; }
        }
	        
	    int i = 0, n_pos = pos_idx+1, n_neg = n - n_pos;
	    pos_idx = 0, neg_idx = n-1;
	    while(n_pos > 0 && n_neg > 0)
	    {
	        arr[i] = temp[pos_idx++];
	        arr[i+1] = temp[neg_idx--];
	        n_pos--, n_neg--;
	        i += 2;
	    }
	    
	    while(n_pos > 0)
	    {
	        arr[i] = temp[pos_idx++], i++, n_pos--;
	    }
	    
	    while(n_neg > 0)
	    {
	        arr[i] = temp[neg_idx--], i++, n_neg--;
	    }
	}
};