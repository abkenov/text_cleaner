import glob
import re

src_directory = '/home/ablan/'

file_list = glob.glob('akbilek/[0-9]/*.txt')
len(file_list)

for i in range(len(file_list)):
    file_list[i] = src_directory + file_list[i]

file_list[0]

for file in file_list:
    with open(file, 'r') as text:
        line = text.readline()
        line = line.lower()
        line = re.sub(r'["«»№()—~!*+-=`_'',.<>?*;:]', '',line)
        line = re.sub(r'\s+', ' ',line)

        line = line.strip()
        clean_file_name = file[:12] + "clean_" + file[12:22] + "clean_" + file[22:]
        with open(clean_file_name, 'w') as clean_file:
            clean_file.write(line)
