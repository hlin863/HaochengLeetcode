# tests/test_find_sum_pairs.py

import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Medium._3307_FindSumPairs import FindSumPairs

def test_example_case():
    findSumPairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
    assert findSumPairs.count(7) == 8
    findSumPairs.add(3, 2)  # nums2 becomes [1, 4, 5, 4, 5, 4]
    assert findSumPairs.count(8) == 2
    assert findSumPairs.count(4) == 1
    findSumPairs.add(0, 1)  # nums2 becomes [2, 4, 5, 4, 5, 4]
    findSumPairs.add(1, 1)  # nums2 becomes [2, 5, 5, 4, 5, 4]
    assert findSumPairs.count(7) == 11