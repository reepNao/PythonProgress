def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def remove_duplicates(arr):
    return list(set(arr))

if __name__ == "__main__":
    input_str = input("Enter integers separated by spaces: ")
    input_list = [int(x) for x in input_str.split()]
    
    unique_input_list = remove_duplicates(input_list)
    
    if len(input_list) != len(unique_input_list):
        print("Duplicate values are not allowed. Try again.")
    else:
        sorted_list = quick_sort(unique_input_list)
        print('Sorted list: ', sorted_list)
