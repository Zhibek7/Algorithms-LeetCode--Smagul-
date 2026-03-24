class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Элиминируем дубликаты через хэширование первого набора
        set1 = set(nums1)
        res = set()
        for num in nums2:
            # Проверка принадлежности ключа набору за константное время
            if num in set1:
                res.add(num)
        return list(res)