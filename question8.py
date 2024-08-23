list_of_tuples = [(1, 50), (3, 20), (2, 30)]

sorted_list = sorted(list_of_tuples, key=lambda x: x[1])

print(sorted_list)  # Output: [(3, 20), (2, 30), (1, 50)]
