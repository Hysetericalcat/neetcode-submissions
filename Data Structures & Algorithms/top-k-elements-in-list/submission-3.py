class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        counts_ = []
        num_set = set(nums)

        for num in num_set:
            if nums.count(num) in counts:
               counts[nums.count(num)].append(num)
            else:
               counts[nums.count(num)] = [num]
            print(counts)

        sorted_keys = sorted(counts.keys(),reverse=True)  
        print(sorted_keys) 
        final_output = []
        for i,key in enumerate(sorted_keys):
            if i == k:
                break
            if len(final_output) == k:
                break
            final_output = final_output + counts[key]
        return final_output



        



           
            

        

