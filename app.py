def bubblesort(list_to_sort):
    for i in range(len(list_to_sort)):
        # n_swap parameter tells us, how many swaps were made in one iteration
        n_swap = 0

        for j in range(len(list_to_sort)-1):
            # checking, if the very next number is greater than current one
            if list_to_sort[j] > list_to_sort[j+1]:
                # if condition is true, then we are swapping those numbers
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
                n_swap += 1

        # if there were no swaps, that means that our list is sorted and we can return it
        if n_swap == 0:
            return list_to_sort
    return list_to_sort