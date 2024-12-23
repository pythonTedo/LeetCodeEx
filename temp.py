from typing import List
import numpy as np

names = ["Mary","John","Emma"]
heights = [180,165,170]

def sortPeople(names: List[str], heights: List[int]) -> List[str]:
    p_key = {k: v for (k, v) in zip(heights, names)}
    print(p_key)
    return [p_key[x] for x in sorted(heights)[::-1]]

print(sortPeople(names, heights))

