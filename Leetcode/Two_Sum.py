class Solution:
    def twoSum(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = {}
        r[arr[0]] = 0
        for i in range(1,len(arr)):
            if (target - arr[i]) in r:
                return [i,r[target - arr[i]]]
            else:
                r[arr[i]] = i