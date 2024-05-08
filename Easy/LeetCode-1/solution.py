def twoSum(self, nums: List[int], target: int) -> List[int]:
    visited = {}
    for index, val in enumerate(nums):
        rem = target - val
        if rem in visited:
            return [visited[rem],index]
        else:
            visited[val] = index