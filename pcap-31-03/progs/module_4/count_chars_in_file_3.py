from os import strerror

try:
    ccnt = lcnt = 0
    s = open('/home/stamatis/repos/python-institute/pcap-31-03/progs/module_4/files_for_processing/text.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
