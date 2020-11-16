class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        
        arr = [0]*(n1+n2)
        i = 0 
        j = 0
        k = 0
        
        while i < n1 and j <n2:
            if nums1[i]<nums2[j]:
                arr[k] = nums1[i]
                k = k+1
                i = i+1
            else:
                arr[k] = nums2[j]
                k = k+1
                j = j+1
                
        while i<n1:
            arr[k] = nums1[i]
            k = k+1
            i = i+1
            
        while j<n2:
            arr[k] = nums2[j]
            k = k+1
            j = j+1
        
        total = sum(arr)
        median = total/len(arr)
        print(median)