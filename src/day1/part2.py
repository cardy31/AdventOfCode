def first_freq():

    old_freqs = {0: 1}
    freq = 0

    while True:
        file = open('input.txt')

        for line in file:
            num = int(line)
            freq += num

            if freq in old_freqs.keys():
                return freq
            else:
                old_freqs[freq] = 1


if __name__ == '__main__':
    print(first_freq())
