import random

def gen_pass(hane):
    karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    parola = ""

    for i in range(hane):
        parola += random.choice(karakterler)

    return parola
