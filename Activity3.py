print("GADGET PURCHASING PROGRAM!")
print("    CCODCDR ENTERPRISE    ")
print(" ")
print("Choose your brand type!")
print("A. SAMSUNG ")
print("B. APPLE   ")
print("C. XIAOMI  ")
type = input("Choose a Brand: ")

if (type == 'A' or type == 'a'):
    print(" ")
    print("YOU'VE CHOSEN SAMSUNG!")
    print("CHOOSE A GADGET!")
    print("A. LAPTOP   ")
    print("B. PHONE    ")
    print("C. SPEAKER  ")
    gad = input("Gadget : ")
    if(gad == 'A' or gad == 'a'):
        tt = 45000
        print("You purchased a Samsung laptop worth {}.".format(tt))
    elif(gad == 'B' or gad == 'b'):
        tt = 25000
        print("You purchased a Samsung phone worth {}.".format(tt))
    elif(gad == 'C' or gad == 'c'):
        tt = 8999
        print("You purchased a Samsung speaker worth {}.".format(tt))
    else:
        print("INVALID INPUT!")
elif (type == 'B' or type == 'b'):
    print(" ")
    print("YOU'VE CHOSEN APPLE!")
    print("CHOOSE A GADGET!")
    print("A. LAPTOP   ")
    print("B. PHONE    ")
    print("C. SPEAKER  ")
    gad = input("Gadget : ")
    if(gad == 'A' or gad == 'a'):
        tt = 95000
        print("You purchased a Apple laptop worth {}.".format(tt))
    elif(gad == 'B' or gad == 'b'):
        tt = 75000
        print("You purchased a Apple phone worth {}.".format(tt))
    elif(gad == 'C' or gad == 'c'):
        tt = 18999
        print("You purchased a Apple speaker worth {}.".format(tt))
    else:
        print("INVALID INPUT!")
elif (type == 'C' or type == 'c'):
    print(" ")
    print("YOU'VE CHOSEN XIAOMI!")
    print("CHOOSE A GADGET!")
    print("A. LAPTOP   ")
    print("B. PHONE    ")
    print("C. SPEAKER  ")
    gad = input("Gadget : ")
    if(gad == 'A' or gad == 'a'):
        tt = 53000
        print("You purchased a Xiaomi laptop worth {}.".format(tt))
    elif(gad == 'B' or gad == 'b'):
        tt = 26000
        print("You purchased a Xiaomi phone worth {}.".format(tt))
    elif(gad == 'C' or gad == 'c'):
        tt = 5999
        print("You purchased a Xiaomi speaker worth {}.".format(tt))
    else:
        print("INVALID INPUT!")
else:
    print("INVALID INPUT")
