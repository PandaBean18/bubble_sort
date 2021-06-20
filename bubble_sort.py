def bubble_sort(list):
    i = 0
    var_sorted = True
    while i < len(list) - 1:
        if list[i] > list[i + 1]:
            var = list[i]
            list[i] = list[i + 1]
            list[i + 1] = var
            var_sorted = False
        i += 1
        
    if var_sorted == False:
        return bubble_sort(list)
    else:
        return list

bubble_sort([1, 6, 3, 4, 2, 5])
