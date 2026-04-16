import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        # Если точек нет или одна, стоимость равна 0
        if n < 2:
            return 0
        
        # Список для хранения информации о посещенных точках
        visited = [False] * n
        # Очередь с приоритетом (min-heap) для выбора ребра с минимальным весом
        # Хранит кортежи: (расстояние_до_дерева, индекс_точки)
        min_heap = [(0, 0)] # Начинаем с 0-й точки, расстояние до неё изначально 0
        
        total_cost = 0      # Итоговая минимальная стоимость
        edges_used = 0      # Счетчик добавленных точек
        
        while edges_used < n:
            # Извлекаем точку с самым коротким расстоянием до текущего дерева
            dist, curr_point = heapq.heappop(min_heap)
            
            # Если мы уже включили эту точку в дерево, пропускаем её
            if visited[curr_point]:
                continue
                
            # Добавляем точку в остовное дерево
            visited[curr_point] = True
            total_cost += dist
            edges_used += 1
            
            # Рассматриваем все остальные точки (соседей в полном графе)
            for next_point in range(n):
                if not visited[next_point]:
                    # Вычисляем Манхэттенское расстояние: |x1 - x2| + |y1 - y2|
                    weight = abs(points[curr_point][0] - points[next_point][0]) + \
                             abs(points[curr_point][1] - points[next_point][1])
                    
                    # Добавляем потенциальное соединение в кучу
                    heapq.heappush(min_heap, (weight, next_point))
                    
        return total_cost