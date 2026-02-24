class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Функция расстояния (квадрат)
        def dist(p):
            return p[0]**2 + p[1]**2

        # Создаем начальную кучу из первых k точек
        heap = [[dist(p), p] for p in points[:k]]
        self.heap_size = k

        def max_heapify(i):
            l, r = 2*i + 1, 2*i + 2
            largest = i
            if l < self.heap_size and heap[l][0] > heap[i][0]:
                largest = l
            if r < self.heap_size and heap[r][0] > heap[largest][0]:
                largest = r
            if largest != i:
                heap[i], heap[largest] = heap[largest], heap[i]
                max_heapify(largest)

        # BUILD-MAX-HEAP
        for i in range(k // 2 - 1, -1, -1):
            max_heapify(i)

        # Проходим по остальным точкам
        for i in range(k, len(points)):
            d = dist(points[i])
            if d < heap[0][0]: # Если текущая точка ближе самого дальнего в куче
                heap[0] = [d, points[i]]
                max_heapify(0)

        return [item[1] for item in heap]