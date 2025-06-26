#53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def max_crossing_sum(left: int, mid: int, right: int) -> int:
            left_sum = float('-inf')
            sum_ = 0
            for i in range(mid, left - 1, -1):
                sum_ += nums[i]
                left_sum = max(left_sum, sum_)

            right_sum = float('-inf')
            sum_ = 0
            for i in range(mid + 1, right + 1):
                sum_ += nums[i]
                right_sum = max(right_sum, sum_)

            return left_sum + right_sum

        def divide_and_conquer(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2
            left_max = divide_and_conquer(left, mid)
            right_max = divide_and_conquer(mid + 1, right)
            cross_max = max_crossing_sum(left, mid, right)

            return max(left_max, right_max, cross_max)

        return divide_and_conquer(0, len(nums) - 1)
