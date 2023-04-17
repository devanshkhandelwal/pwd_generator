import random
import string

length  = int(input('How long do you want the password to be? \n'))

initial_list = []
final_pwd_list = []
initial_list[:0] = string.printable
initial_list.remove(' ')

for i in range(length):
    letter = random.choice(initial_list)
    final_pwd_list.append(letter)

pwd_str = ''    
for i in final_pwd_list:
    pwd_str += i
print(f'your randomly generated password is:{pwd_str}')
    