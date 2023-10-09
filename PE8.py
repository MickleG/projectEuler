from functools import reduce
[print(reduce((lambda x, y: x * y), [subIndex for subIndex in [int(num) for num in ''.join(line.strip() for line in open('PE8_data.txt').readlines())]]))]
