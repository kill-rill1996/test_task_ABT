import os
from time import time
from threading import Thread


def get_all_filenames_with_paths():
    all_files_paths = []
    for root, dirs, files in os.walk('./test'):
        for file in files:
            path = os.path.join(root, file)
            all_files_paths.append((path, file))
    return all_files_paths


def task1():
    # в папке test найти все файлы filenames вывести колличество
    return len([filename for _, filename in get_all_filenames_with_paths() if 'filenames' in filename])


def task2():
    # в папке test найти все email адреса записанные в файлы
    res = []

    for path, _ in get_all_filenames_with_paths():
        if os.path.getsize(path):
            with open(path, 'r') as f:
                text = f.read().split()
                for word in text:
                    if '@' in word:
                        res.append(word)
    return res


def main():
    task1()
    task2()
    # дополнительно: придумать над механизм оптимизации 2-й задачи (используя threading)


if __name__ == '__main__':
    main()
