def read_file():    # Function is defined with name : 'read_file'
    file = open("products.txt", "r")    # open stock file (products.txt) in read mode.
    lines = file.readlines()
    L = []  # assign empty list with name 'L'
    for line in lines:
        if line == '':
            continue
        L.append(line.replace("\n", "").split(","))
    file.close()
    return L