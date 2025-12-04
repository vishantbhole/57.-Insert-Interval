# 57. Insert Interval
from typing import List


class Solution:
    def insertInterval(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
