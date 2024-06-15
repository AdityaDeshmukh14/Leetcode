def threeSumClosest(self, nums: List[int], target: int) -> int:
    n = len(nums)
    nums.sort()
    output = nums[0] + nums[1] + nums[n-1]
    diff = abs(target - output)
    for i in range(n-2):
        if i>0 and nums[i-1] == nums[i]:
            i+=1
        else:
            j = i+1
            k = n-1
            while j<k:
                currsum = nums[i] + nums[j] + nums[k]
                currdiff = abs(target-currsum)
                if currdiff < diff:
                    diff = currdiff
                    output = currsum
                
                if currsum > target:
                    k-=1
                else:
                    j+=1
            i+=1
    return output