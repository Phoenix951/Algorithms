class QuickSort:
    @staticmethod
    def partition(nums, low, high):
        # Выбираем средний элемент в качестве опорного
        # Также возможен выбор первого, последнего
        # или произвольного элементов в качестве опорного
        pivot = nums[(low + high) // 2]
        i_number = low - 1
        j_number = high + 1

        while True:
            i_number += 1
            while nums[i_number] < pivot:
                i_number += 1

            j_number -= 1
            while nums[j_number] > pivot:
                j_number -= 1

            if i_number >= j_number:
                return j_number

            # Если элемент с индексом i (слева от опорного) больше, чем
            # элемент с индексом j (справа от опорного), меняем их местами
            nums[i_number], nums[j_number] = nums[j_number], nums[i_number]

    @staticmethod
    def quick_sort(nums):
        """"Вспомогательная функция для рекурсии"""

        def _quick_sort(items, low, high):
            partion_func = QuickSort.partition
            if low < high:
                # Идекс для элемента после pivot, который разбивает список
                split_index = partion_func(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)
        print("Быстрая сортирвока: ", nums)