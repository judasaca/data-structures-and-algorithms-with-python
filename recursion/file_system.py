from os import getcwd, listdir
from os.path import getsize, isdir, join


def get_disk_usage(path: str) -> int:
    total = getsize(path)
    if isdir(path):
        for filename in listdir(path):
            child_path = join(path, filename)
            total += get_disk_usage(child_path)
    return total


print(get_disk_usage(getcwd()))
