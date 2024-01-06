import re

part_1 = []
part_2 = []
digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
with open('input.txt') as text:
    for line in text:

        # Part 1
        vals = re.findall('\d', line)
        part_1.append(int(vals[0]) * 10 + int(vals[-1]))

        # Part 2
        vals = re.findall("(?=(" + "|".join(digits.keys()) + "|\d" + "))", line)
        vals = [digits[k] if not k.isdigit() else int(k) for k in vals]
        part_2.append(vals[0] * 10 + vals[-1])

    # Result
    print(sum(part_1), sum(part_2))
