class Algorithms:
    @staticmethod
    def bubble_sort(nums):
        """Пузырьковая сортировка"""
        # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    # Меняем элементы
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    # Устанавливаем swapped в True для следующей итерации
                    swapped = True

        print("Пузырьковая сортировка: ", nums)

    @staticmethod
    def selection_sort(nums):
        """Сортировка выборкой"""
        # Значение i соответствует кол-ву отсортированных значений
        for i in range(len(nums)):
            # Исходно считаем наименьшим первый элемент
            lowest_number = i
            # Этот цикл перебирает несортированные элементы
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_number]:
                    lowest_number = j
            # Самый маленький элемент меняем с первым в списке
            nums[i], nums[lowest_number] = nums[lowest_number], nums[i]

        print("Сортировка выборкой: ", nums)

    @staticmethod
    def insertion_sort(nums):
        """Сортировка вставкой"""
        # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
        for i in range(1, len(nums)):
            insert_item = nums[i]
            # Сохраняем ссылку на индекс предыдущего элемента
            j = i - 1
            # Элементы отсортированного сегмента перемещаем вперёд, если они больше
            # элемента для вставки
            while j >= 0 and nums[j] > insert_item:
                nums[j + 1] = nums[j]
                j -= 1
            # Вставляем элемент
            nums[j + 1] = insert_item
        print("Сортировка вставкой: ", nums)

