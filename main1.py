from multiprocessing.pool import ThreadPool as Pool
import hashlib as hl
import functions as func
import time
# from multiprocessing import Pool

pool_size = 10  # your "parallelness"
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

	pool = Pool(pool_size)

	for item in word_list:
	    pool.apply_async(func.concat_words, (item,word_list,check,))

	pool.close()
	pool.join()
