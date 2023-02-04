import random
import string

"""
    the password will have 40% digits 40% letters (20% lowercase 20% uppercase) and 20% special characters
"""

def generate(passwordSize):
    
    password = []
    percentDigits = passwordSize * 0.4
    percentLowercase = passwordSize * 0.2
    percentUppercase = passwordSize * 0.2
    percentPunctuation = passwordSize * 0.2
    for i in range(int(percentDigits)):
        password.append(random.choice(string.digits))
    for i in range(int(percentLowercase)):
        password.append(random.choice(string.ascii_lowercase))
    for i in range(int(percentUppercase)):
        password.append(random.choice(string.ascii_uppercase))
    for i in range(int(percentPunctuation)):
        password.append(random.choice(string.punctuation))
    # shuffle the password
    random.shuffle(password)
    password = ''.join(password)
    return password