def checksum():
    file = open('input.txt')

    two = 0
    three = 0

    for line in file:
        arr = [0] * 26
        # print(line)
        line = line.lower()
        for char in line:
            if char != '\n':
                val = ord(char) - 97
                # print(val, char)
                arr[val] += 1

        print(arr)
        used_two = False
        used_three = False

        for num in arr:
            if num == 2 and used_two is False:
                used_two = True
                two += 1
            elif num == 3 and used_three is False:
                used_three = True
                three += 1
            if used_two and used_three:
                break

    return two * three


if __name__ == '__main__':
    print(checksum())
