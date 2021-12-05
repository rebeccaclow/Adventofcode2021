def read_input(file_name):
    with open(file_name) as f:
        return [int(x) for x in f.readlines()]