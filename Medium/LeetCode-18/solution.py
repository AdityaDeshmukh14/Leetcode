def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    def threeSum(nums, target, a):
        n = len(nums)
        b=a+1
        while b<(n-2):
            if (b>a+1 and nums[b-1] == nums[b]):
                b+=1
            else:
                c = b+1
                d = n-1
                while c<d:
                    currsum = nums[a] + nums[b] + nums[c] + nums[d]

                    if currsum < target:
                        c+=1
                    elif currsum > target:
                        d-=1
                    else:
                        output.append((nums[a],nums[b],nums[c],nums[d]))
                        while c<d and nums[c]==nums[c+1]:
                            c+=1
                        while c<d and nums[d-1]==nums[d]:
                            d-=1
                        c+=1
                        d-=1
                b+=1            
    
    nums.sort()
    n = len(nums)
    output = []
    
    for a in range(n-3):
        if a==0 or nums[a-1] != nums[a]:
            threeSum(nums, target, a)
    
    return output