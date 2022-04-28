/*Function to find frequency of x
* x : element whose frequency is to be found
* v : input vector
*/
int findFrequency(vector<int> v, int x){
    // Your code here
    int count_x = 0;
    
    for(int i=0; i<v.size(); i++)
    {
        if(x == v[i]) { count_x += 1; }
    }
    
    return count_x;
}