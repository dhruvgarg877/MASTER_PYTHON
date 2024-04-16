name = "Dhruv"
print("hii " + name)
st = """ Hlo i am Dhruv
I belong to ynr
Currently living in mohali"""
print(st)
jaado = "Hlo Brother"
st1="     "
print(jaado[0:5])
print(len(jaado)) # it will print the length of the string LEN function
print(name.upper()) #it converts name string to UPPer case
print(name.lower())#it converts name string to lower case
print(name.replace("Dhruv" , "Ankit")) #it will replace all Dhruv in that name string
print(jaado.split(" ")) #it is used to create list with splitting from spaces
blogheading = "introduction to pyhton"
print(blogheading.capitalize()) #it is used to convert first word of the string to uppercase
st2 = "Hii i am Dhruv. Dhruv is my first name"
print(st2.center(50)) #it is used to move string to the center
print(st2.count("Dhruv")) # used to count the how much times word is repeated
print(st2.endswith("name"))# used to know that string is ending with given word or not always answers in bolean 
print(st2.endswith("Dhruv"))#as wrong word is written it shows False as output
print(st2.startswith("Hii"))# used to know that string is starting with given word or not always answers in bolean 
print(st2.find("am"))# it searches for the given value in the string and then prints its index where it is present. if it is absent then it returns -1
print(st2.index("am"))# it searches for the given value in the string and then prints its index where it is present. if it is absent then it raises an exception rather than printing -1
print(jaado.isalnum())# this method returns true only if string only consists A-Z , a-z , 0-1. otherwise returns will be false.
print(jaado.isalpha())# Same as alnum but it consists only alphabetics not include numbers if A-Z , a-z then true otherwise false.
print(jaado.islower())#it returns true if all the characters are in lowercase otherwise false.
print(jaado.isupper())#it returns true if all the characters are in uppercase otherwise false.
print(jaado.isprintable())#returns true if string is printable if something imprintable then flase.
print(jaado.isspace())#returns true only if there is whitespaces
print(jaado.istitle())#returns true only if first letter of every word is Capitalized . 
print(st2.swapcase())# used to convert all upper cases to lower and lower to upper
print(st2.title())# used to convert a string to title
