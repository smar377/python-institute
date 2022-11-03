from os import strerror

try:
	fo = open('/home/stamatis/repos/python-institute/pcap-31-03/progs/module_4/files_for_processing/newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
	    fo.write("line #" + str(i+1) + "\n")
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
