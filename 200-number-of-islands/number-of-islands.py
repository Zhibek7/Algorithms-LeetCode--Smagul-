class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        islands = 0
        
        def dfs(r: int, c: int):
            # Базовый случай: выход за границы матрицы или попадание в воду ('0')
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return
            
            # Помечаем текущую сушу как посещенную (превращаем в '0')
            grid[r][c] = '0'
            
            # Ищем продолжение острова в 4 направлениях
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Если нашли неисследованную сушу, это новый остров
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)  # Запускаем DFS, чтобы пометить весь остров
                    
        return islands