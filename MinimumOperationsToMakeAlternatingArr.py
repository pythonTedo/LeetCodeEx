from typing import List


def minimumOperations(nums: List[int]) -> int:
    tmp = nums

    for i in range(2, len(nums)):
        if (nums[i] != nums[i-2] or nums[i] == nums[i-1]):
            tmp[i-2] == tmp[i]
           
    return tmp

nums = [3,1,3,2,4,3]

print(minimumOperations(nums))