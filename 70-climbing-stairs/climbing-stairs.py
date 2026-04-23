class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        # Используем оптимизацию памяти  
        # Храним только два предыдущих значения
        prev2, prev1 = 1, 1 
        
        for i in range(2, n + 1):
            # Текущее состояние зависит от двух предыдущих
            current = prev1 + prev2
            # Обновляем значения для следующей итерации
            prev2 = prev1
            prev1 = current
            
        return prev1