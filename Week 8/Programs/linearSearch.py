def linearSearch(lst, item):
    'return the index where item is found in lst'
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1
