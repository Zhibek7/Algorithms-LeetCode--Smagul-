class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Инициализация хэш-таблицы для группировки по инвариантному ключу
        anagram_map = {}
        
        for s in strs:
            # Канонизация: сортировка символов создает общий ключ для всех анаграмм
            key = "".join(sorted(s)) 
            
            # Если хэш-функция не находит ключ, создаем новую корзину
            if key not in anagram_map:
                anagram_map[key] = []
            
            # Добавление оригинальной строки в список по вычисленному хэш-адресу
            anagram_map[key].append(s)
            
        # Возврат агрегированных данных (значений хэш-таблицы)
        return list(anagram_map.values())