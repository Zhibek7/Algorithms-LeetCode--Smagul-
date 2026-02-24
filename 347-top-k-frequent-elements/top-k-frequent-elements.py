class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Подсчет частот
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        # Превращаем в список кортежей (частота, значение)
        data = [[freq, val] for val, freq in counts.items()]
        self.heap_size = len(data)

        def left(i): return 2 * i + 1
        def right(i): return 2 * i + 2

        # MAX-HEAPIFY по первому элементу кортежа (частоте)
        def max_heapify(A, i):
            l, r = left(i), right(i)
            largest = i
            if l < self.heap_size and A[l][0] > A[i][0]:
                largest = l
            if r < self.heap_size and A[r][0] > A[largest][0]:
                largest = r
            if largest != i:
                A[i], A[largest] = A[largest], A[i]
                max_heapify(A, largest)

        def build_max_heap(A):
            for i in range(len(A) // 2 - 1, -1, -1):
                max_heapify(A, i)

        def extract_max(A):
            max_val = A[0]
            A[0] = A[self.heap_size - 1]
            self.heap_size -= 1
            max_heapify(A, 0)
            return max_val

        # 2. Строим кучу и вытаскиваем K элементов
        build_max_heap(data)
        result = []
        for _ in range(k):
            result.append(extract_max(data)[1])
        return result