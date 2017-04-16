import os


def get_files(inodes, start_path):
    all_files = {}
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = root + os.sep + file
            stats = os.stat(path)
            all_files[str(stats.st_ino)] = {'path': path, 'inode': stats.st_ino, 'size': stats.st_size}
    print(all_files)
    return all_files


def parse_sincedb(path):
    sincedb = {}
    with open(path, 'r') as reader:
        for line in reader:
            inode, maj_dev, min_dev, offset = line.strip().split(' ', 4)
            if inode != '0':
                sincedb[inode] = {'inode': inode, 'offset': offset}
    print(sincedb)
    return sincedb


def merge_path_stats(sincedb, all_paths):
    for inode in sincedb.keys():
        file = sincedb[inode]
        if inode in all_paths.keys():
            file['path'] = all_paths[inode]['path']
            file['size'] = all_paths[inode]['size']
            if int(all_paths[inode]['size']) > 0:
                file['percent'] = round(int(file['offset']) / int(all_paths[inode]['size']), 2) * 100
    print(sincedb)
    return sincedb


def get_status(sincedb):
    pass
