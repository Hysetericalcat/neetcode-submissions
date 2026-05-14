class Solution:
 def longestConsecutive(self, nums: List[int]) -> int:
      sorted_nums = sorted(list(set(sorted(nums))))
      sequence_length = []
      print(sorted_nums)
      count = 0 
      for i,value in enumerate(sorted_nums):
          if i == 0:
            prev = sorted_nums[i]
            count = count + 1
          elif((sorted_nums[i] - prev)**2 == 1):
             count = count + 1
             prev = sorted_nums[i]
          else:
             sequence_length.append(count)
             count = 0
             prev = sorted_nums[i]
             count = count + 1
      sequence_length.append(count)
      return max(sequence_length) if sequence_length else count