#first alter the possible passwords that I need to get
#next hash and compare the changed passwords to the hashes I need to get
#print out the hashes that I got for the final work

import hashlib as hl
import functions as func
import multiprocessing
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


def harder_stuff(proc):
	print("number of processors used: "+ str(proc))
	start_time = time.time()
	print("start time with " + str(proc) + " processors is " + str(start_time))
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
		for i in word_list:
		#for line in f:
			p = multiprocessing.Process(target = func.concat_words, args = (i,word_list,check))
			jobs.append(p)
			p.start()

		for j in jobs:
			j.join()
	end = time.time()
	time_passed = end-start_time
	print('time elapsed '+ str(time_passed))




harder_stuff(4)
harder_stuff(8)
harder_stuff(12)