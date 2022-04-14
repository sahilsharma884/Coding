class Solution
{   
    public: 
    //Function to return a list of integers denoting spiral traversal of matrix.
    vector<int> spirallyTraverse(vector<vector<int> > matrix, int r, int c) 
    {
        // code here 
        int direction = 1, visited = 0;
        vector<int> result;
        
        int i = 0, j=0;
        
        while(r>0 && c>0)
        {
            while(visited<c)
            {
                result.push_back(matrix[i][j]);
                j += direction;
                visited++;
            }
            r -= 1, visited = 0, j -= direction, i += direction;
            
            while(visited<r)
            {
                result.push_back(matrix[i][j]);
                i += direction;
                visited++;
            }
            c -= 1, visited = 0, i -= direction, j -= direction;
            
            direction *= -1;
        }
        
        return result;
    }
};