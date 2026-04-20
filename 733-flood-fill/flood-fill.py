class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        
        # Если цвет уже совпадает с новым, заливка не требуется
        if old_color == color:
            return image
            
        def dfs(r: int, c: int):
            # Базовый случай: проверка выхода за границы и совпадения цвета
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != old_color:
                return
            
            # Перекрашиваем текущий пиксель (отмечаем как посещенный)
            image[r][c] = color
            
            # Рекурсивно обходим соседей (вверх, вниз, влево, вправо)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        dfs(sr, sc)
        return image
        