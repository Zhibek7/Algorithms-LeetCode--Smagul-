class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        self.heap_size = 0
        
        # Добавляем начальные элементы
        for num in nums:
            self.add(num)
            
    def parent(self, i): return (i - 1) // 2
    def left(self, i): return 2 * i + 1
    def right(self, i): return 2 * i + 2
    
    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        
        if l < self.heap_size and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < self.heap_size and self.heap[r] < self.heap[smallest]:
            smallest = r
            
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)
            
    def heap_extract_min(self):
        if self.heap_size < 1:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.heap.pop() # Для экономии памяти
        self.min_heapify(0)
        return min_val
        
    def min_heap_insert(self, key):
        self.heap.append(float('inf')) # Выделяем место
        self.heap_size += 1
        i = self.heap_size - 1
        self.heap[i] = key
        
        # Процесс heapify-up (просеивание вверх)
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def add(self, val: int) -> int:
        # Добавляем новый элемент
        self.min_heap_insert(val)
        
        # Если элементов стало больше k, выкидываем самый маленький
        if self.heap_size > self.k:
            self.heap_extract_min()
            
        # Корень кучи теперь и есть k-й по величине элемент
        return self.heap[0]