class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       
     count = 0
     current_sum = 0
     prefix_counts = {0: 1}
    
     for num in nums:
        current_sum += num
        needed = current_sum - k
        if needed in prefix_counts:
            count += prefix_counts[needed]
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
    
     return count   
        


        