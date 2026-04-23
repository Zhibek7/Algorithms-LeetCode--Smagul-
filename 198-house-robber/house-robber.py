class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Оптимизация памяти: храним максимум для (i-2) и (i-1) домов
        prev2 = 0 # Эквивалент dp[i-2]
        prev1 = 0 # Эквивалент dp[i-1]
        
        for num in nums:
            # Выбираем: грабить текущий дом + (i-2) или пропустить (i-1)
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
            
        return prev1