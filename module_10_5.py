from multiprocessing import Process
import time

files = ['file_1.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt']

start_line = time.time()
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            line = line.strip()
            all_data.append(line)


if __name__ == '__main__':
    for file in files:
        read_info(file)
    end = time.time() - start_line

    print(f'Время работы: {end}')
    start_proc = time.time()
    for file in files:
        print(file)
        proccess1 = Process(target=read_info(file))
        proccess1.start()
    end_proc = time.time() - start_proc
    print(f'Время работы: {end_proc}')
