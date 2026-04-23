class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Инициализируем таблицу значением больше возможного (amount + 1) [cite: 16]
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # Базовый случай [cite: 18]
        
        # Итеративный цикл (Bottom-Up) [cite: 13]
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    # Выбираем минимум: оставить как есть или взять текущую монету
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1