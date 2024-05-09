def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def calculateMedian(sortedArray)->float:
        n = len(sortedArray)
        print(sortedArray)
        if n%2 == 0:
            i = int((n-1)/2)
            print((sortedArray[i] + sortedArray[i+1])/2)
            return (sortedArray[i] + sortedArray[i+1])/2
        else:
            i = int((n)/2)
            print(sortedArray[i])
            return (sortedArray[i])
        
    if not nums1:
        return calculateMedian(nums2)
    elif not nums2: 
        return calculateMedian(nums1)
    else:
        nums1.extend(nums2)
        nums1.sort()
        return calculateMedian(nums1)