class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap_size = len(stones)
        
        def max_heapify(A, i):
            l, r = 2*i + 1, 2*i + 2
            largest = i
            if l < self.heap_size and A[l] > A[i]:
                largest = l
            if r < self.heap_size and A[r] > A[largest]:
                largest = r
            if largest != i:
                A[i], A[largest] = A[largest], A[i]
                max_heapify(A, largest)

        def extract_max(A):
            res = A[0]
            A[0] = A[self.heap_size - 1]
            self.heap_size -= 1
            max_heapify(A, 0)
            return res

        def insert(A, key):
            if self.heap_size < len(A):
                A[self.heap_size] = key
            else:
                A.append(key)
            self.heap_size += 1
            # Всплытие (Heapify-up)
            curr = self.heap_size - 1
            while curr > 0:
                p = (curr - 1) // 2
                if A[p] < A[curr]:
                    A[p], A[curr] = A[curr], A[p]
                    curr = p
                else: break

        # Подготовка
        for i in range(self.heap_size // 2 - 1, -1, -1):
            max_heapify(stones, i)

        while self.heap_size > 1:
            y = extract_max(stones)
            x = extract_max(stones)
            if x != y:
                insert(stones, y - x)

        return stones[0] if self.heap_size == 1 else 0