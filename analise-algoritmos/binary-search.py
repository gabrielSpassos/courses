def recursive_binary_search(array, number_to_search):
    left = 0
    right = len(array)
    mid = (left + right) // 2
    aux_num = array[mid]
    if aux_num == number_to_search:
        return aux_num
    elif number_to_search > aux_num:
        new_array = array[mid:]
        print('right:', new_array)
        return recursive_binary_search(new_array, number_to_search)
    else:
        new_array = array[:mid]
        print('left:', new_array)
        return recursive_binary_search(new_array, number_to_search)


def main():
    array = [1, 2, 3, 4, 5 , 6]
    print(recursive_binary_search(array, 6))

main()
