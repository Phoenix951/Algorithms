class HeapSort:
    """Пирамидальная сортировка"""

    @staticmethod
    def heapify(nums, heap_size, root_size):
        # Индекс наибольшего элемента считаем корневым индексом
        largest = root_size
        left_child = (2 * root_size) + 1
        right_child = (2 * root_size) + 2

        # Если левый потомок корня — допустимый индекс, а элемент больше,
        # чем текущий наибольший, обновляем наибольший элемент
        if left_child < heap_size and nums[left_child] > nums[largest]:
            largest = left_child

        # Так же для правого потомка корня
        if right_child < heap_size and nums[right_child] > nums[largest]:
            largest = right_child

        # Если наибольший элемент больше не корневой, они меняются местами
        if largest != root_size:
            nums[root_size], nums[largest] = nums[largest], nums[root_size]
            heaping = HeapSort
            heaping.heapify(nums, heap_size, largest)

    @staticmethod
    def heap_sort(nums):
        heap_sorting = HeapSort
        number_len = len(nums)

        # Создаём Max Heap из списка
        # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
        # перед первым элементом списка
        # 3-й аргумент означает повторный проход по списку в обратном направлении,
        # уменьшая счётчик i на 1
        for i in range(number_len, -1, -1):
            heap_sorting.heapify(nums, number_len, i)

        # Перемещаем корень Max Heap в конец списка
        for i in range(number_len - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heap_sorting.heapify(nums, i, 0)
        print("Сортировка кучей: ", nums)

