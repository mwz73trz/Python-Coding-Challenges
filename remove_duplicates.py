def remove_duplicates(lst):
    empty_lst = []
    for i in lst:
        if i not in empty_lst:
            empty_lst.append(i)
    return empty_lst

print(remove_duplicates([1, 3, 5, 6, 6, 6, 7.8]))