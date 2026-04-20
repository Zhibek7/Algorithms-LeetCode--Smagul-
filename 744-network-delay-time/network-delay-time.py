import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Представление графа в виде списка смежности
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # Словарь для хранения кратчайших расстояний от k до других вершин
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0
        
        # Очередь с приоритетами (min-heap) для хранения пар (текущая дистанция, узел)
        pq = [(0, k)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            # Если извлеченное расстояние больше уже найденного кратчайшего, пропускаем
            if current_dist > distances[u]:
                continue
                
            # Процесс релаксации рёбер для всех соседей узла u
            for v, weight in graph[u]:
                distance = current_dist + weight
                
                # Если найден более короткий путь до v
                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(pq, (distance, v))
                    
        # Ищем максимальное время среди всех кратчайших путей до узлов
        max_time = max(distances.values())
        
        # Если хотя бы один узел остался недостижим (inf), возвращаем -1
        return max_time if max_time < float('inf') else -1
        