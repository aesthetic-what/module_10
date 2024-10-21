from threading import Thread
import time

def write_words(n, name_file):
    with open(f'{name_file}', 'w', encoding='utf-8') as file:
        for i in range(n):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {name_file}')

start_func = time.time() 
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(100, 'example3.txt')
write_words(200, 'example4.txt')
end_func = time.time() - start_func
print(f'end work: {end_func}')

trh_first = Thread(target=write_words, args=(10, 'example5.txt'))
trh_second = Thread(target=write_words, args=(30, 'example6.txt'))
trh_third = Thread(target=write_words, args=(200, 'example7.txt'))
trh_firth= Thread(target=write_words, args=(100, 'example8.txt'))

start_trh = time.time()
trh_first.start()
trh_second.start()
trh_third.start()
trh_firth.start()


trh_first.join()
trh_second.join()
trh_third.join()
trh_firth.join()
end_trh = time.time() - start_trh
print(f'end work with tread: {end_trh}')