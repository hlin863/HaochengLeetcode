from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        res = -1
        for num, count in freq.items():
            if num == count:
                res = max(res, num)
        return res