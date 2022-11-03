from os import strerror

try:
	fo = open('/home/stamatis/repos/python-institute/pcap-31-03/progs/module_4/files_for_processing/newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
