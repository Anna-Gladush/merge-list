def merge(*lists):
    list_of_all_the_lists = []
    for item_on_the_list in lists:
        list_of_all_the_lists += item_on_the_list
        list_of_all_the_lists.sort()
    return list_of_all_the_lists
print(merge(*lists))
