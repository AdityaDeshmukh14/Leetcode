def removeDuplicates(self, nums: List[int]) -> int:
    dic = {}
    ctr = 0
    i=0
    while i<len(nums):
        if nums[i] in dic:
            nums.pop(i)
        else:
            key = nums[i]
            dic[key] = 1
            ctr+=1
            i+=1
    return ctr