from os import strerror

try:
    cnt = 0
    s = open('/home/stamatis/repos/python-institute/pcap-31-03/progs/module_4/files_for_processing/text.txt', "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
