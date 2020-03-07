from test_list import test_list_of_numbers
from heap_sorting import HeapSort
from merge_sorting import Merge
from quick_sorting import QuickSort
from algorithms import Algorithms


def start():
    algorithms = Algorithms
    num_list = test_list_of_numbers()
    print("Первоначальный массив чисел: ", num_list)
    algorithms.bubble_sort(num_list)

    num_list = test_list_of_numbers()
    algorithms.selection_sort(num_list)

    num_list = test_list_of_numbers()
    algorithms.insertion_sort(num_list)

    num_list = test_list_of_numbers()
    heap = HeapSort.heap_sort
    heap(num_list)

    num_list = test_list_of_numbers()
    merge_sorting = Merge.view_sorted_list
    merge_sorting(num_list)

    num_list = test_list_of_numbers()
    quick_sorting = QuickSort.quick_sort
    quick_sorting(num_list)


# Запуск программы
start()