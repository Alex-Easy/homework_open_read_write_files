files = ['1.txt', '2.txt', '3.txt']
result_file = 'result.txt'

file_lines = {}

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        file_lines[file] = len(lines)

sorted_files = sorted(file_lines, key=file_lines.get)

with open(result_file, 'w') as result:
    for file in sorted_files:
        result.write(file + '\n')
        result.write(str(file_lines[file]) + '\n')
        with open(file, 'r', encoding='utf-8') as f:
            result.writelines(f.readlines())
        result.write('\n')

with open(result_file, 'r') as file:
    read_file = file.read()
print(read_file)

