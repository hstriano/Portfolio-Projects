import random
import array

# password length
max_len = 9

# define characters
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

# create single array
combined_list = digits + upper_case + lower_case + symbols

# randomly select from each array
rand_digit = random.choice(digits)
rand_upper = random.choice(upper_case)
rand_lower = random.choice(lower_case)
rand_symbol = random.choice(symbols)

# collect random characters
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

# set password length
for x in range(max_len - 4):
    temp_pass = temp_pass + random.choice(combined_list)

    # shuffle to prevent patterns
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

# make the password
password = ""
for x in temp_pass_list:
    password = password + x

print(password)