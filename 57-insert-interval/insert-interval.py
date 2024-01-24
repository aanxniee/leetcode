"""
binary search
first the first interval in the list having a start value greater
than the start value of newInterval
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

       
        left, right = [], []

        for i in intervals:

            # end of current interval is less than start of new interval, this interval would appear left of new interval
            if i[1] < newInterval[0]:
                left.append(i),

            # start of current interval is greater than end of new interval, this interval would appear right of the new interval
            elif i[0] > newInterval[1]:
                right.append(i),

            # either the start is less or the end is greater, find the wider interval
            else:
                newInterval = (min(newInterval[0], i[0]), max(newInterval[1], i[1]))

        return left + [newInterval] + right
        