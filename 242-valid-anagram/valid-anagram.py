class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        counts = {} # Хэш-карта частотности символов
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        for char in t:
            # Если ключа нет или его запас исчерпан — это не анаграмма
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1
        return True