# Two Sum

Given an array of integers **nums** and an **integer** target, return _indices of the two numbers such that they add up to **target**._
<br>
You may assume that each input would have exactly one solution, and you may not use the same element twice.
<br>
You can return the answer in any order.

**Example 1:**
> **Input:** nums = [2,7,11,15], target = 9 <br>
> **Output:** [0,1] <br>
> **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1]. <br>

<br>

### Example 2:
> **Input:** nums = [3,2,4], target = 6 <br>
> **Output:** [1,2]

<br>

### Example 3:
> **Input:** nums = [3,3], target = 6 <br>
> **Output:** [0,1] <br>
 
### Constraints:

- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists.
 
<br>

**Follow-up:** Can you come up with an algorithm that is less than O(n2) time complexity?