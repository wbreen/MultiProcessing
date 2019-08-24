#This is where I change the words in order to hash them
import hashlib as hl
import time

def change_digits(input):
	added_dig = input.strip()
	out = []
	for num in range(1,1000):
		out.append(input + str(num))
	return out


sym = {'a':'@','c':'(','g':'9',
	   'o':'0','b':'8','f':'#',
	   'i':'1','l':'1','s':'$'}
def change_symb(orig):
	output = ""
	for letter in orig:
		for key in sym:
			orig = orig.replace(key, sym[key])
			output = orig
	return output


def hash_given(input):
	f_hash = hl.md5(input.encode())
	f_hash = f_hash.hexdigest()
	#print(f_hash)
	return f_hash

def concat_words(inputs, file, check):
	#o = open(file, "r")
	#print("starting work on " +input)
	#time.sleep(5)
	for input in inputs:
		out = []
		#print(f"{input}")
		for word2 in file:
			#print(input+word2)
			out.append(input + word2)
				#print(f"{word1}{word2}")
			#new_out=[]
		for concat in out:
			new_out=hash_given(concat)
				#print(hash_given(concat))
			for targ in check:
				if new_out == targ:
					o=open("final_hashes.txt", "a+")
					print(f"matched {concat} to {new_out}")
					o.write(concat + " hashes to "+new_out.strip() +'\n')
					o.close()


def do_everything(inputs, file, check):
	number = 0
	for input in inputs:
		out = []
		print(f"Working on {input} which is number {number} of total: {len(inputs)}")
		number +=1
		for word2 in file:
			everything = input + word2
			everything = change_symb(everything)
			everything_list = change_digits(everything)
			for each_word in everything_list:
				new_out=hash_given(each_word)
				#print(hash_given(concat))
				for targ in check:
					if new_out == targ:
						o=open("final_hashes.txt", "a+")
						print(f"matched {each_word} to {new_out}")
						o.write(each_word + " hashes to "+new_out.strip() +'\n')
						o.close()
