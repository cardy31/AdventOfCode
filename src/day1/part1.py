def get_frequency():
    file = open('input.txt')

    freq = 0
    for line in file:
        num = int(line)
        freq += num

    return freq


if __name__ == '__main__':
    print(get_frequency())
