from sys import path

path.append('/home/stamatis/repos/python-institute/pcap-31-03/modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
