import random
import math

def gen_pwd(length):
    pwd = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+|[]{};:/?/,~`'.<>"
    for i in range(length):
        new = math.floor(random.random() * len(chars))
        pwd += chars[new]
    return pwd

pwd_len = int(input("Enter the lenght of the password: "))
gentd_pwd = gen_pwd(pwd_len)
print("Your Random Generated Password is: " , gentd_pwd)
