class MyQueue:
    def __init__(self):
        self.s1 = [] # Стек для добавления элементов (Push)
        self.s2 = [] # Стек для извлечения элементов (Pop/Peek)

    def push(self, x: int) -> None:
        # Просто кладем элемент в первый стек
        self.s1.append(x)

    def pop(self) -> int:
        # Убеждаемся, что s2 не пуст
        self.peek()
        # Извлекаем верхний элемент (это будет первый вошедший элемент)
        return self.s2.pop()

    def peek(self) -> int:
        # Если стек s2 пуст, перекладываем все из s1 в s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        # Возвращаем верхний элемент s2 
        return self.s2[-1]

    def empty(self) -> bool:
        # Очередь пуста, если пусты оба стека
        return not self.s1 and not self.s2