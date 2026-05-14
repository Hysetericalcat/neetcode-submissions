class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        seen = {}
        nums_ = nums
        output_array = []
        for i,value in enumerate(nums):
             seen[i] = value
             product = 1
             for j,value in enumerate(nums_):
                if i == j:
                    continue
                product=product*value
             output_array.append(product)
        return output_array
       
       


             
