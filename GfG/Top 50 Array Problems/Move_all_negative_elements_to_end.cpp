class Solution{
    public:
    void segregateElements(int A[],int n)
    {
        // Your code goes here
        int pos_idx = -1, neg_idx = n, B[n];
        int temp;
        
        for(int i=0; i<n; i++)
        {
            if(A[i] >= 0) { B[++pos_idx] = A[i]; }
            else { B[--neg_idx] = A[i]; }
        }
        
        ++pos_idx;
        neg_idx = n-1;
        
        while(pos_idx < neg_idx)
        {
            temp = B[pos_idx], B[pos_idx] = B[neg_idx];
            B[neg_idx] = temp;
            
            ++pos_idx, --neg_idx;
        }
        
        for(int i=0; i<n; i++) { A[i] = B[i]; }
    }
};