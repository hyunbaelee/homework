def sort_tuple(input_dict):
    a=dict(sorted(input_dict.items(), key=lambda x: x[1]))
    b=tuple(a.keys())
    print(b)
