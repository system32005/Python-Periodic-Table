from time import sleep
try:
    print ("Periodic Table Python Program, Rev 5.")
    print ("Press Ctrl+C to end program anytime")
    hydrogen= "Name: Hydrogen, Chem Symbol: H, Atomic Weight: 1.008, NFPA Fire Diamond: Health: 0, Flammability: 4, Reactivity: 0, Special: NONE"
    helium= "Name: Helium, Chem Symbol: He, Atomic Weight: 4.002, NFPA Fire Diamond: Health: 1, Flammability: 0, Reactivity: 0, Special: NONE" 
    lithium= "Name: Lithium, Chem Symbol: Li, Atomic Weight: 6.941, NFPA Fire Diamond: Health: 3, Flammability: 2, Reactivity: 2, Special: Reacts Violently With Water, Strikethrough W"
    while 0+0 == 0:
        atom= input ("Input Atomic Number or Name of element in lower case \n")
        if atom == "hydrogen" or atom == "1":
            print (hydrogen)

        elif atom == "helium" or atom == "2":
            print (helium)

        elif atom == "lithium" or atom == "3":
            print (lithium)

        elif atom != "hydrogen" or atom != "1" or atom != "helium" or atom != "2" or atom != "lithium" or atom != "3":
            print ("Oops! We didn't find your chosen element in element DB")

except KeyboardInterrupt:
    print ("Detected CTRL+C Keybind, Shutting Down...")
    sleep (3)


