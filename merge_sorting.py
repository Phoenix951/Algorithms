class Merge:
    """Сортировка слиянием"""

    @staticmethod
    def merge(left_list, right_list):
        sorted_list = []
        left_list_index = right_list_index = 0

        # Длина списков часто используется, поэтому создадим переменные для удобства
        left_list_length, right_list_length = len(left_list), len(right_list)

        for _ in range(left_list_length + right_list_length):
            if left_list_index < left_list_length and right_list_index < right_list_length:
                # Сравниваем первые элементы в начале каждого списка
                # Если первый элемент левого подсписка меньше, добавляем его
                # в отсортированный массив
                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
                    # Если первый элемент правого подсписка меньше, добавляем его
                    # в отсортированный массив
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1

            # Если достигнут конец левого списка, элементы правого списка
            # добавляем в конец результирующего списка
            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

            # Если достигнут конец правого списка, элементы левого списка
            # добавляем в отсортированный массив
            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
        return sorted_list

    @staticmethod
    def merge_sort(nums):
        merge_class = Merge.merge
        merge_class_sort = Merge.merge_sort

        # Возвращаем список, если он состоит из одного элемента
        if len(nums) <= 1:
            return nums

        # Для того чтобы найти середину списка, используем деление без остатка
        # Индексы должны быть цнлыми
        mid = len(nums) // 2

        # Сортируем и объединяем подсписки
        left_list = merge_class_sort(nums[:mid])
        right_list = merge_class_sort(nums[mid:])

        # Объединяем отсортированные списки в результирующий
        return merge_class(left_list, right_list)

    @staticmethod
    def view_sorted_list(nums):
        # Выводим отсортированный список
        merge_sort = Merge.merge_sort

        numbers = merge_sort(nums)
        print("Сортировка слиянием: ", numbers)

