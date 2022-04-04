pair<long long, long long> getMinMax(long long a[], int n) {
    long long int minV, maxV;
    minV = a[0];
    maxV = a[0];
    
    int i=1;
    
    while(i < n)
    {
        if(minV > a[i])
        {
            minV = a[i];
        }
        
        if(maxV < a[i])
        {
            maxV = a[i];
        }
        
        i++;
    }
    
    return std::make_pair(minV,maxV);
}