str1 = "Hello"
str6 = "Hi world"
str4 = "Arshad! {}"
str2 = str1.upper()
print(str2)

str3 = str1.isupper()
print(str3)

print(str1 == str2)

str7 = str1 + str6
print(str7)

str5 = str1 + " " + str4.format("this is going to be a good day!!!")
print(str5)

str8 = "hello {0}, learning git"
print(str8.format("Arshad"))