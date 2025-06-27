#218. The Skyline Problem

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        if len(buildings) == 1:
            l, r, h = buildings[0]
            return [[l, h], [r, 0]]
        
        mid = len(buildings) // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return self.mergeSkylines(left, right)

    def mergeSkylines(self, left: List[List[int]], right: List[List[int]]) -> List[List[int]]:
        points = []
        i = j = 0
        currH1 = currH2 = 0

        while i < len(left) or j < len(right):
            if j >= len(right) or (i < len(left) and left[i][0] < right[j][0]):
                x = left[i][0]
                currH1 = left[i][1]
                i += 1
            elif i >= len(left) or (j < len(right) and right[j][0] < left[i][0]):
                x = right[j][0]
                currH2 = right[j][1]
                j += 1
            else:
                x = left[i][0]
                currH1 = left[i][1]
                currH2 = right[j][1]
                i += 1
                j += 1

            maxH = max(currH1, currH2)
            if not points or points[-1][1] != maxH:
                points.append([x, maxH])
        
        return points
