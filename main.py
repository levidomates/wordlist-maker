import optparse

uppercase = [
	"Q","W","E","R",
	"T","Y","U","I",
	"O","P","Ğ","Ü",
	"A","S","D","F",
	"G","H","J","K",
	"L","Ş","İ","Z",
	"X","C","V","B",
	"N","M","Ö","Ç"
	]

lowercase = [
	"q","w","e","r",
	"t","y","u","ı",
	"o","p","ğ","ü",
	"a","s","d","f",
	"g","h","j","k",
	"l","ş","i","z",
	"x","c","v","b",
	"n","m","ö","ç"
	]

number = [
	"1","2","3","4",
	"5","6","7","8",
	"9","0"
	]

def get_argumets():
	
	parser = optparse.OptionParser()
	
	parser.add_option("-n","--name",dest="filename",
							help="""+----------------------+
								| Write the file name. |
								+----------------------+
								| Example   [filename] |
								+----------------------+""")
	 						
	parser.add_option("-p","--password",dest="password",

							help="""+---------------------------------+
								| For uppercase use            [U]|
								+---------------------------------+
								| For lowercase use            [l]|
								+---------------------------------+
								| For number use               [n]|
								+---------------------------------+
								| Example                  [UUUln]|
								+---------------------------------+""")
										
	(options, args) = parser.parse_args()
	
	return options

def function(password):

	FLAG = True
	DIC,count = {},1

	for i in password:
		
		if i == "U":
				DIC[count] = uppercase
		elif i == "l":
				DIC[count] = lowercase
		elif i == "n":
				DIC[count] = number
		else:
			FLAG = False

		count += 1

	return (DIC,FLAG)

def calculate_total(password):

		result = 0

		for a in range(0,len(password)):

			calculater = 1

			if a != 0:
				character = password[:-a]
			else:
				character = password

			for i in character:
				
				if i == "U":
					calculater *= len(uppercase)
				elif i == "l":
					calculater *= len(lowercase)
				elif i == "n":
					calculater *= len(number)

			result += calculater
		return result



def create_word_list(length,character_dic,filename,total):

	file = open(f"{filename}.txt","w")
	dic = {}
	dic[1] = character_dic[1]
	counter = 0
	counter += len(character_dic[1])
	
	for count in range(1,length):
		dic[count+1] = []
		for word in dic[count]:
			for character in character_dic[count+1]:
				
				word += character
				if len(word) == length:
					file.write(word + "\n")
				dic[count+1].append(word)
				word = word[:-1]

				counter += 1
				percentage = 100 * counter // total
				print(f"\r%{percentage}",end="")
   
	file.close()
	print("\n")


if __name__ == "__main__":

	options = get_argumets()
	(DIC,FLAG) = function(options.password)
	total = calculate_total(options.password)
	if FLAG:
		create_word_list(len(options.password),
		   DIC,options.filename,total)

		
