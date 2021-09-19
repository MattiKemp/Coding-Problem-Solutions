# not very elegant but it gets the just done
# Runtime: O(n), where n is the number of intervals in the input.
# Technically if you don't consider the copying required for the output the Runtime is O(lg(n))
# Space Complexity: O(1), not considering the output space.
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        def binSearch(intervals, find):
            begin = 0
            end = len(intervals)
            middle = -1
            while begin < end:
                middle = (begin + end)/2
                if intervals[middle][1] < find:
                    begin = middle + 1
                elif intervals[middle][0] > find:
                    end = middle
                else:
                    return middle
            return middle
        begin = binSearch(intervals, newInterval[0])
        end = binSearch(intervals, newInterval[1])
        l = []
        for i in range(begin):
            l.append(intervals[i])
        if begin == -1:
            if end == -1:
                l.append(newInterval)
            else:
                l.append([newInterval[0],intervals[end][1]])
        else:
            newInterv = [newInterval[0],newInterval[1]]
            lower = False
            if intervals[begin][1] < newInterval[0]:
                l.append(intervals[begin])
            elif intervals[begin][0] < newInterval[0]:
                newInterv[0] = intervals[begin][0]
            if intervals[end][0] > newInterval[1]:
                lower = True
            elif intervals[end][1] > newInterval[1]:
                newInterv[1] = intervals[end][1]
            l.append(newInterv)
            if lower:
                l.append(intervals[end])
        for i in range(end+1, len(intervals)):
            l.append(intervals[i])
        return l
