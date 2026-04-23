class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # Если сумма нечетная, нельзя разделить на две равные части
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        # Таблица достижимости сумм (Boolean Tabulation) [cite: 16]
        dp = [False] * (target + 1)
        dp[0] = True # Сумму 0 можно собрать всегда
        
        for num in nums:
            # Идем с конца в начало, чтобы не использовать одно и то же число дважды
            # (Оптимизация Space Complexity из лекции) 
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
                
        return dp[target]  