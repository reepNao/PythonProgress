import random
# TNF(Turkey National Flag)
# Python program to sort a sequence containing only red (0) and white (1) in a single pass.
red = 0    # The first color of the flag.
white = 1  # The second color of the flag.
colors = (red, white, red)


def turkish_flag_sort(sequence: list) -> list:
    """
    A pure Python implementation of Turkish Flag sort algorithm.
    :param sequence: A sequence of 2 unique integer values (0, 1)
    :return: The same collection in ascending order
    """
    if not sequence:
        return []

    low, mid, high = 0, 0, len(sequence) - 1

    while mid <= high:
        if sequence[mid] == colors[0]:
            sequence[low], sequence[mid] = sequence[mid], sequence[low]
            low += 1
            mid += 1
        elif sequence[mid] == colors[1]:
            mid += 1
        else:
            raise ValueError(f"The elements inside the sequence must contain only {colors} values")

    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    num_elements = int(input("Enter the number of elements: "))
    unsorted = [random.choice([red, white]) for _ in range(num_elements)]
    print(f"Unsorted sequence   : {unsorted}")
    sorted_sequence = turkish_flag_sort(unsorted)
    print(f"Sorted sequence     : {sorted_sequence}")

