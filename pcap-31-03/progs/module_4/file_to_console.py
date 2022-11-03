# Opening tzop.txt in read mode, returning it as a file object:
stream = open("/home/stamatis/repos/python-institute/pcap-31-03/progs/module_4/files_for_processing/tzop.txt", "rt", encoding = "utf-8")

# Printing the contents of the file
print(stream.read())
