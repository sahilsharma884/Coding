class Solution
{
    public:
    void sort012(int a[], int n)
    {
        // code here
        int i;
        int c0=0, c1=0, c2=0;
        
        for(i=0; i<n; i++)
        {
            if(a[i] == 0) { c0 += 1; }
            else if(a[i] == 1) {c1 += 1; }
            else { c2 += 1; }
        }
        
        i=0;
        while(c0) { a[i++] = 0; c0--; }
        while(c1) { a[i++] = 1; c1--; }
        while(c2) { a[i++] = 2; c2--; }
        
    }
    
};