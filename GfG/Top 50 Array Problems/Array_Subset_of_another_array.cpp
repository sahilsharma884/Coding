string isSubset(int a1[], int a2[], int n, int m) {
    if(m > n)
    {
        return "No";
    }
    else
    {
        unordered_set<int> temp;
        
        for(int i=0; i<n; i++)
        {
            temp.insert({a1[i]});
        }
        
        for(int i=0; i<m; i++)
        {
            if(temp.find(a2[i]) == temp.end())
            {
                return "No";
            }
        }
        
        return "Yes";
    }
}