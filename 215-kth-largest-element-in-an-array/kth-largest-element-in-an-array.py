class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap_size = len(nums)
        
        # Вспомогательные функции для индексов
        def left(i): return 2 * i + 1
        def right(i): return 2 * i + 2
        
        def max_heapify(A, i):
            l = left(i)
            r = right(i)
            largest = i
            
            if l < self.heap_size and A[l] > A[i]:
                largest = l
            if r < self.heap_size and A[r] > A[largest]:
                largest = r
                
            if largest != i:
                A[i], A[largest] = A[largest], A[i]
                max_heapify(A, largest)
                
        def build_max_heap(A):
            self.heap_size = len(A)
            # От середины массива к началу
            for i in range(len(A) // 2 - 1, -1, -1):
                max_heapify(A, i)
                
        def heap_extract_max(A):
            if self.heap_size < 1:
                return None
            max_val = A[0]
            A[0] = A[self.heap_size - 1]
            self.heap_size -= 1
            max_heapify(A, 0)
            return max_val

        # Основной алгоритм
        build_max_heap(nums)
        
        # Удаляем (k - 1) самых больших элементов
        for _ in range(k - 1):
            heap_extract_max(nums)
            
        return heap_extract_max(nums)
        