#This is where I change the words in order to hash them
import hashlib as hl

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

def concat_words(input, file, check):
	#o = open(file, "r")
	print("starting work on " +input)
	out = []
	for word in file:
		#print(input+word)
		out.append(input + word)
	#new_out=[]
	for concat in out:
		new_out=hash_given(concat)
		#print(hash_given(concat))
		for targ in check:
			if new_out == targ:
				o=open("final_hashes.txt", "a+")
				print("matched " + new_out)
				o.write(concat + " hashes to "+new_out.strip() +'\n')
				o.close()



