class Solution{
    public:
    // arr: input array
    // n: size of array
    //Function to sort the array into a wave-like array.
    void convertToWave(vector<int>& arr, int n){
        
        // Your code here
        int i=0, j=1;
        int temp;
        while(i<n && j<n)
        {
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i+=2;
            j+=2;
        }
    }
};