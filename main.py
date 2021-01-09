from typing import List


class Solution:

  def twoSum(self, numsUnsorted: List[int], target: int) -> List[int]:
    nums = list(
        map(lambda index: {
            'index': index,
            'value': numsUnsorted[index]
        }, range(len(numsUnsorted))))

    nums = sorted(numsList, key=lambda x: x['value'])

    left = 0
    right = len(nums) - 1
    ans = []

    while (left < right):
      leftVal = nums[left]['value']
      leftIndex = nums[left]['index']
      rightVal = nums[right]['value']
      rightIndex = nums[right]['index']

      if (leftVal + rightVal < target):
        left += 1
      elif (leftVal + rightVal > target):
        right -= 1
      else:
        ans = [leftIndex, rightIndex]
        left = right

    return ans


my = Solution()

n = [3, 2, 4]
t = 6

trueAns = [1, 2]

ans = my.twoSum(n, t)

print("ans", ans, ans == trueAns)
