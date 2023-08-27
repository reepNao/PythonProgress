def merge_sort(left, right):
    result = []
    i = j = 0
    comparisons = 0
    
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result, comparisons

def tim_sort(arr):
    min_run = 32
    n = len(arr)
    comparisons = 0
    
    for start in range(0, n, min_run):
        end = min(start + min_run, n)
        arr[start:end] = sorted(arr[start:end])
        comparisons += len(arr[start:end]) * (len(arr[start:end]) - 1) // 2
    
    run_size = min_run
    while run_size < n:
        for start in range(0, n, run_size * 2):
            mid = min(n, start + run_size)
            end = min(n, mid + run_size)
            merged, merge_comparisons = merge(arr[start:mid], arr[mid:end])
            comparisons += merge_comparisons
            arr[start:end] = merged
        
        run_size *= 2
    
    return arr, comparisons

if __name__ == "__main__":
    input_str = input("Enter integers separated by spaces: ")
    input_list = [int(x) for x in input_str.split()]
    
    original_length = len(input_list)
    unique_input_list = list(set(input_list))
    
    if len(input_list) != len(unique_input_list) or len(input_list) != original_length:
        print("Duplicate values are not allowed. Try again.")
    else:
        sorted_list, total_comparisons = tim_sort(unique_input_list)
        print('Sorted list:', sorted_list)
        print('Total comparisons:', total_comparisons)
