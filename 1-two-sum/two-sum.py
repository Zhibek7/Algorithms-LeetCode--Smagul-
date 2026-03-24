class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} # Хранилище пар число: индекс
        for i, num in enumerate(nums):
            complement = target - num
            # Поиск комплементарного значения в таблице за O(1)
            if complement in hash_map:
                return [hash_map[complement], i]
            # Сохранение текущего числа как ключа для будущих проверок
            hash_map[num] = i
        return []