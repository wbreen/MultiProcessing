#first alter the possible passwords that I need to get
#next hash and compare the changed passwords to the hashes I need to get
#print out the hashes that I got for the final work

import hashlib as hl
import functions as func
import multiprocessing
#import os
import time
#alter passwords

def hash_given(input):
	f_hash = hl.md5(input.encode())
	f_hash = f_hash.hexdigest()
	#print(f_hash)
	return f_hash

def easy_hashes():

	f=open("commonengwords.txt", "r")
	o=open("final_hashes.txt", "w+")

	for line in f:
		line = line.strip()
		symb = func.change_symb(line)
		digits = func.change_digits(line)

		o_hash = hash_given(line)
		s_hash = hash_given(symb)
		d_hash = []
		for digit in digits:
			d_hash.append(hash_given(digit))


		#matching hash values to the target
		hashes = open("hashes.txt", "r")
		for line1 in hashes:
			if o_hash.strip() == line1.strip():
				print("matched " + line)
				o.write(line + " hashes to " +o_hash.strip() + '\n')
			if s_hash.strip() == line1.strip():
				print("matched " + symb)
				o.write(symb + " hashes to " +s_hash.strip() + '\n')
			num = 1
			for each_dig in d_hash:
				if each_dig.strip() == line1.strip():
					print("matched " + line+str(num))
					o.write(line+str(num) +" hashes to " +each_dig.strip() +'\n')
				num +=1
		#f.close()
		#o.close()

def no_multiproc():
	f=open("commonengwords.txt", "r")
	hashes = open("hashes.txt", "r")
	check = []
	for hash in hashes:
		check.append(hash.strip())
	word_list = []
	for line in f:
		word_list.append(line.strip())
	start = time.time()
	for word in word_list:
		#line = line.strip()
		#print(f"{word}")
		func.concat_words(word, word_list, check)
	end = time.time()
	total_time = end-start
	print(f"total time in sequence is {total_time}")


def harder_stuff(procs):
	print(f"number of processors used: {procs}")
	#start_time = time.time()
	#print(f"start time with {procs} processors is {start_time}")
	f=open("commonengwords.txt", "r")
	o=open("final_hashes.txt", "w+")
	hashes = open("hashes.txt", "r")
	word_list = []
	for line in f:
		word_list.append(line.strip())
	f.close()
	check=[]
	for hash in hashes:
		check.append(hash.strip())
	f=open("commonengwords.txt", "r")
	if __name__ == '__main__':
		jobs = []
		#for i in range(len(word_list)):
		a = 0
		for proc in range(procs):
		#for line in f:
			startpoint=len(word_list)/procs
			endpoint = len(word_list)/procs
			startpoint = int(startpoint*a)
			endpoint = int(endpoint*(a+1))
			process = multiprocessing.Process(target = func.concat_words, args = (word_list[startpoint:endpoint],word_list,check))
			jobs.append(process)
			process.start()
			a+=1

		for job in jobs:
			job.join()
	#end = time.time()
	#time_passed = end-start_time
	#print('time elapsed '+ str(time_passed))
	#print()


def hardest_stuff(procs):
	#print(f"number of processors used: {procs}")
	#start_time = time.time()
	#print(f"start time with {procs} processors is {start_time}")
	f=open("commonengwords.txt", "r")
	o=open("final_hashes.txt", "w+")
	hashes = open("hashes.txt", "r")
	word_list = []
	for line in f:
		word_list.append(line.strip())
	f.close()
	check=[]
	for hash in hashes:
		check.append(hash.strip())
	f=open("commonengwords.txt", "r")
	if __name__ == '__main__':
		jobs = []
		#for i in range(len(word_list)):
		a = 0
		for proc in range(procs):
		#for line in f:
			startpoint=len(word_list)/procs
			endpoint = len(word_list)/procs
			startpoint = int(startpoint*a)
			endpoint = int(endpoint*(a+1))
			process = multiprocessing.Process(target = func.do_everything, args = (word_list[startpoint:endpoint],word_list,check))
			jobs.append(process)
			process.start()
			a+=1

		for job in jobs:
			job.join()


#no_multiproc()

start_time = time.time()
#easy_hashes()
#harder_stuff(8)
processors_used = 11
print(f"number of processors used is {processors_used}")
hardest_stuff(processors_used)
end = time.time()
time_passed = end-start_time
print('time elapsed '+ str(time_passed))

