class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() # Хэш-таблица для фиксации уникальных ключей
        for num in nums:
            # Если хэш-функция указывает на уже занятый слот с тем же значением
            if num in seen:
                return True
            seen.add(num)
        return False