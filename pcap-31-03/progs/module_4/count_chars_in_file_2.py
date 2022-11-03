from os import strerror

try:
    cnt = 0
    s = open('/home/stamatis/repos/python-institute/pcap-31-03/progs/module_4/files_for_processing/text.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))
