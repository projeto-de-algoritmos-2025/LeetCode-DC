from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def compare(num1: str, num2: str) -> bool:
            if len(num1) != len(num2):
                return len(num1) < len(num2)
            return num1 < num2

        def merge_sort(arr: List[str]) -> List[str]:
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left: List[str], right: List[str]) -> List[str]:
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if compare(left[i], right[j]):
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            while i < len(left):
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1
            return merged

        sorted_nums = merge_sort(nums)
        return sorted_nums[-k]
