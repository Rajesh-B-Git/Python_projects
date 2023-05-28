import string
import random
from csv import writer


def passgen():
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    platform = input("Enter the name of the platform : \n")
    pass_length = int(input("Enter the length of the password : \n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    password = ("".join(s[0:pass_length]))

    print(password)
    passdata = [platform, password]
    with open('pass.csv', 'a') as f:
        writedata = writer(f)
        writedata.writerow(passdata)


passgen()
