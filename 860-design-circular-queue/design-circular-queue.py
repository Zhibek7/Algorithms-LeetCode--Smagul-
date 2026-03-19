class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.queue = [0] * k
        self.head = 0  # Индекс первого элемента
        self.count = 0 # Текущее количество элементов в очереди

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # Вычисляем индекс хвоста для вставки (циклическое оборачивание)
        tail_index = (self.head + self.count) % self.capacity
        self.queue[tail_index] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # Сдвигаем голову вперед (циклическое оборачивание)
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # Вычисляем индекс текущего хвоста
        tail_index = (self.head + self.count - 1) % self.capacity
        return self.queue[tail_index]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity