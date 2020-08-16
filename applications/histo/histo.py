# Your code here
with open('robin.txt') as f:
    # read_data = f.read()
    # print(read_data)
    for line in f:
        print(line, end='')

    f.close()

