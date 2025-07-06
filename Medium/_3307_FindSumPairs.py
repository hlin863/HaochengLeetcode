from collections import Counter
from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1 = nums1
        self.n2 = nums2
        self.m = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.n2[index]
        self.m[old_val] -= 1
        self.n2[index] += val
        self.m[self.n2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(self.m[tot - x] for x in self.n1)