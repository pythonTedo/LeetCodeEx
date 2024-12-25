from typing import List
from collections import Counter

def can_divide_into_pairs(nums: List[int]) -> bool:
    # Count occurrences of each number
    count = Counter(nums)
    
    # Check if all counts are even
    for value in count.values():
        if value % 2 != 0:
            return False
    
    return True

nums = [3,2,3,2,2,2]

print(can_divide_into_pairs(nums))