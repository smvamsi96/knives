i = 0

file_path = "/home/smv/nums.txt"

target = 100

with open(file_path, 'w') as the_file:
    while i < target:
        the_file.write(str(i))
        the_file.write('\n')
        i += 1

