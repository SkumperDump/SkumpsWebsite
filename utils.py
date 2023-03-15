# Turns contents of a file into string representation
def open_file(filename):
    temp = ""
    with open(filename, 'r') as f:
        for line in f:
            temp += str(line)
    return temp
