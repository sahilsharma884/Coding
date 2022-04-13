class Solution{
    public:
    /*You are required to complete this method*/
     int max_path_sum(int A[], int B[], int l1, int l2)
    {
    
        //Your code here
        int sc_a = 0, sc_b = 0, total_sum = 0;
        int i=0, j=0;
        while(i<l1 && j<l2)
        {
            if(A[i] < B[j])
            {
                sc_a += A[i];
                i++;
            }
            if(A[i] > B[j])
            {
                sc_b += B[j];
                j++;
            }
            if(A[i] == B[j])
            {
                if(sc_a > sc_b)
                {
                    total_sum += sc_a;
                }
                else
                {
                    total_sum += sc_b;
                }
                
                total_sum += B[j];
                sc_a = 0, sc_b = 0;
                i++, j++;
            }
        }
        
        while(i<l1)
        {
            sc_a += A[i], i++;
        }
        
        while(j<l2)
        {
            sc_b += B[j], j++;
        }
        
        if(sc_a > sc_b)
        {
            total_sum += sc_a;
        }
        else
        {
            total_sum += sc_b;
        }
        
        return total_sum;
    }
};