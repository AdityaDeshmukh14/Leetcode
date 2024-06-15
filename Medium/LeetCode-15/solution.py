def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    sumAll = 0
    output = []
    for i in range(n-2):
        if i>0 and nums[i] == nums[i-1]:
            i+=1
        else:        
            j = i+1
            k = n-1
            
            while(j<k):
                sumAll = nums[i] + nums[j] + nums[k]
                
                if sumAll < 0:
                    j = j+1
                elif sumAll > 0:
                    k = k-1
                else:
                    output.append((nums[i], nums[j], nums[k]))
                    while j<k and nums[j] == nums[j+1]:
                        j = j+1
                    while j<k and nums[k] == nums[k-1]:
                        k = k-1
                    j = j+1
                    k = k-1
            i = i+1
    return output