class MinStack:
    def __init__(self):
        self.stack = []      # Основной стек для хранения элементов
        self.min_stack = []  # Стек для хранения минимумов

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Если min_stack пуст, текущее значение - это минимум.
        # Иначе сравниваем новое значение с верхним элементом min_stack и кладем наименьшее
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # При удалении элемента (POP) удаляем элементы из обоих стеков
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Возвращаем верхний элемент основного стека
        return self.stack[-1]

    def getMin(self) -> int:
        # Минимум всегда находится на вершине min_stack
        return self.min_stack[-1]