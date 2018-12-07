def differing_ids():

    for i in range(0, 26):
        lines = get_new_lines()

        # Remove letter at same position in every line
        for j in range(0, len(lines)):
            lines[j].pop(i)

        for j in range(0, len(lines)):
            temp = lines.copy()

            target = temp.pop(j)

            if target in temp:
                return ''.join(target)


def get_new_lines():
    file = open('input.txt')

    lines = []

    count = 0
    for line in file:
        lines.append([])
        for char in line:
            if char != '\n':
                lines[count].append(char)
        count += 1

    return lines


if __name__ == '__main__':
    print(differing_ids())
