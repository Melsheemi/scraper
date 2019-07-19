import json
# Access file content
    # file path: D:\\image\\storage\\store.json (see path constructor)
    # read file content
def read(filePath):
    objects = open(filePath,'r', encoding='utf-8').read()
    return objects
# sort (sorter-native)

# overr/wr file content

if __name__ == '__main__':
    read('D:\\image\\storage\\store.json')
