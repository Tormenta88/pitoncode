import random
mon = 0
cruz = False
res = 0


while cruz == False:
    res = random.randint(1,2)
    if res == 1:
        cruz == False
        mon += 1
    elif res == 2:
        cruz = True

print(mon)
print(2**mon)
