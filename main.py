from typing import List


class Solution:

  def twoSum(self, nums: List[int], target: int) -> List[int]:
    diffMap = {}

    for index, x in enumerate(nums):
      print(x, diffMap)
      diff = target - x

      if diff in diffMap:
        return [diffMap[diff], index]

      diffMap[x] = index

    return []


my = Solution()

n = [3, 2, 4]
t = 6

trueAns = [1, 2]

ans = my.twoSum(n, t)

print("ans", ans, ans == trueAns)
