from typing import List


def mostFrequentEven(self, nums: List[int]) -> int:
    seen = dict()

    for num in nums:
        if num % 2 == 0:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

    # print("seen", seen)
    if not seen: 
        return -1
    else:
        max_value = max(seen.values())
        return min([key for key, value in seen.items() if value == max_value])

nums = [0,1,2,2,4,4,1]
print(mostFrequentEven(nums))