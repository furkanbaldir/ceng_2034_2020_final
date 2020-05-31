# Furkan Baldır		170709031

# Please launch this code only own directory or empty directory.

import os
import requests
import uuid
from multiprocessing import Pool
import hashlib
import time

def control_process(urls):

	#####################################################################################
	# Question1 - Question3
	# Creating a child process and print its pid.
	# Avoid orphan process
	#####################################################################################

	try:
		pid = os.fork()
	except OSError:
		exit("Could not create a child process")

	# Parent and child process works independently
	if pid > 0:
		print("\nParent process pid is = {}".format(os.getpid()))
		os.waitpid(pid, 0) # Parent waits to finish child process.

	else:
		print("\n*************************************************\n")
		print("Child process pid is = {}\n".format(os.getpid()))
		print("*************************************************\n")

	#####################################################################################
	
	#####################################################################################
	# Question2
	# Download files with child process
	#####################################################################################

		
		print("{} files downloading...\n".format(len(urls)))
		start_downloading_time = time.time()
		for i in range(len(urls)):
			download_file(urls[i], "file{}".format(i))
			print("file{0} downloaded from\n{1}\n".format(i, urls[i]))

		end_downloading_time = time.time()

		subtract_downloading_time = end_downloading_time - start_downloading_time

		print("Total execution time to download = {}\n".format(subtract_downloading_time))

		print("*************************************************\n")


	#####################################################################################

	#############################################################
	# Question4
	# Controlling duplicate files with multi processing
	#####################################################################################
		
		# Check files from directory that python file is existing
		files = os.listdir() 

		# Remove main.py
		files.remove("ceng_2034_final_answer.py")

		#print(files)

		list_md5 = []

		print("Checking checksum md5 values...\n")

		start_duplicate_time = time.time()

		# Finding checksum values and append to list_md5 list with multiprocessing
		with Pool(5) as p:
			list_md5 = p.map(md5,files)

		#print(list_md5)

		print("Checking duplicate values...\n")

		# Creating a list_duplicate list with using multiprocessing
		with Pool(5) as p:
			list_duplicate = p.starmap(check_duplicate,( [list_md5[0],
			 list_md5],[list_md5[1], list_md5], 
			 [list_md5[2], list_md5], [list_md5[3],
			 list_md5], [list_md5[4], list_md5]))


		list_duplicates = list(list_duplicate)

		#print(list_duplicates)
		#print('\n')

		print("Last fixes...\n")

		# Creating unique_duplicate list for repeating same duplicate values
		unique_duplicates = unique(list_duplicates)

		#print(unique_duplicates)
		#print('\n')

		for j in range(len(unique_duplicates)):
			print("{0} and {1} duplicate files.".format(files[unique_duplicates[j][0]],
			 files[unique_duplicates[j][1]]))

		end_duplicate_time = time.time()

		subtract_duplicate_time = end_duplicate_time - start_duplicate_time

		print("\nTotal execution time to check duplicate = {}".format(subtract_duplicate_time))

		print("\n*************************************************")

#########################################################################################

# Return new list with unique members
def unique(list1): 
  
    # init a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        if x == None:
        	list1.remove(None)
        elif x not in unique_list: 
            unique_list.append(x) 
    
    return unique_list
	
# Download files with url
def download_file(url, file_name=None):

	r = requests.get(url, allow_redirects=True)
	
	file = file_name if file_name else str(uuid.uuid4())
	
	open(file, 'wb').write(r.content)

# Return checksum md5 values
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Return duplicate indexes in list
def check_duplicate(element, list_md5):

	duplicate_count = 0
	indexes = []

	for i in range(len(list_md5)):
		if list_md5[i] == element:
			duplicate_count += 1
			indexes.append(i)
			
	if duplicate_count > 1:
		
		#print(indexes)
		return indexes


#Opening
os.system("clear")
print("\n***********************************************\n")
print("Welcome to my Operating System homework\n\n        © Made by Furkan Baldır\n")
print("***********************************************\n")
print("This is your operating system:\n")
os.system("lsb_release -d")
print("\n***********************************************\n")
print("Python version:\n")
os.system("python3 --version")
print("\n***********************************************\n")
print("Kernel version:\n")
os.system("uname -srm")
print("\n*************************************************\n")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("RESULTS")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# Main part
urls = ["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
	"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg",
	"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
	"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]

control_process(urls)

