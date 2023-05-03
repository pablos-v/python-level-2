from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
#         form ls_of_sums of 3 elts
        ls_of_sums = []

        return min(i % target for i in ls_of_sums)


if __name__ == '__main__':
    eee = Solution()
    print(eee.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
