class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        total_len = l1 + l2
        steps = (total_len//2) + 1
        
        start1, start2 = 0,0
        mid,prev = 0,0
        
        while steps:
            prev = mid
            if start1 < l1 and start2 < l2 and nums1[start1] > nums2[start2]:
                mid = nums2[start2]
                start2 += 1
            elif start1 < l1 and start2 < l2 and nums1[start1] <= nums2[start2]:
                mid = nums1[start1]
                start1 += 1
            elif start1 < l1:
                mid = nums1[start1]
                start1 += 1
            elif start2 < l2:
                mid = nums2[start2]
                start2 += 1
            
            steps -= 1
              
        if (l1+l2)%2 == 0:
            return (prev+mid)/2
        else:
            return mid