a=str(input('isming nima'))
b=int(input('tugilgan yilingni  kirit'))
d=2025-b
print(a, '-', d, 'yosh')
txt = 'LMaasleitbtui'
car_name=(txt[1::2])
print(car_name)
txt = 'MsaatmiazD'
selected2_car2_names2 = (txt[0::2],txt[-1::-2])
print(selected2_car2_names2)
txt = "I'am John. I am from London"
cities=["Istanbul", "Khiva", "Barcelona", "Paris", "London", "New York", "Los Angeles"]
txt_lowrer=txt.lower()
found=[]
for city in cities:
    if city.lower() in txt_lowrer:
        found.append(city)
        
if found:
    print("topilgan shahar:", found)
else:
    print("hech qanday shahar nomi topilmadi.")

#5.Write a Python program that takes a user input string and prints it in reverse order.


a=str(input("soz kiriting"))
b=a[::-1]
print(b)
#6.Write a Python program that counts the number of vowels in a given string.


soz=input("soz kirit")
total=0
for ch in soz.lower():
    if ch in "euioa":
        total+=1
print("unlilar soni:", total)
#7.Write a Python program that takes a list of numbers as input and prints the maximum value.
nums = list(map(int, input("Sonlar: ").split()))
print(max(nums))

#8.Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
n=input("3 xonali son kiriting:")
m=n[::-1]
if n==m:
    print("palindrom") 
else:
    print("palindrom emas")    
#9.Write a Python program that extracts and prints the domain from an email address provided by the user.
email=input("email kiriting")
parts=email.split("@")
print(parts[1])
#10.Write a Python program to generate a random password containing letters, digits, and special characters.
import random

length = 12

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

password = ""
for i in range(length):
    password += random.choice(chars)

print("Sizning random parolingiz:", password)
