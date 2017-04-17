import os


def get_files(start_path):
    all_files = {}
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = root + os.sep + file
            stats = os.stat(path)
            all_files[str(stats.st_ino)] = {'path': path, 'inode': stats.st_ino, 'size': stats.st_size}
    return all_files


def parse_sincedb(path):
    sincedb = {}
    with open(path, 'r') as reader:
        for line in reader:
            inode, maj_dev, min_dev, offset = line.strip().split(' ', 4)
            if inode != '0':
                sincedb[inode] = {'inode': inode, 'offset': offset}
    return sincedb


def merge_path_stats(sincedb, all_paths, **kwargs):
    for inode in list(sincedb):
        file = sincedb[inode]
        if inode in all_paths.keys():
            file['path'] = all_paths[inode]['path']
            file['size'] = all_paths[inode]['size']
            if int(all_paths[inode]['size']) > 0:
                file['percent_complete'] = round(int(file['offset']) / int(all_paths[inode]['size']) * 100, 2)
        elif kwargs['ignore_missing'] == 'y':
            del(sincedb[inode])
    return sincedb


def get_status(sincedb):
    pass
