from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Шаг 1: инициализация очереди гнилыми апельсинами и подсчет свежих
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
                    
        # Если свежих апельсинов изначально нет, время 0
        if fresh_count == 0:
            return 0
            
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Шаг 2: Поиск в ширину (BFS) по уровням (минутам)
        while queue and fresh_count > 0:
            minutes += 1
            # Обрабатываем все апельсины на текущем уровне (текущей минуте)
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                # Проверяем 4 соседних направления
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Если сосед - свежий апельсин, он заражается
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Отмечаем как гнилой
                        fresh_count -= 1
                        queue.append((nr, nc))
                        
        # Если остались свежие апельсины, возвращаем -1
        return minutes if fresh_count == 0 else -1
        