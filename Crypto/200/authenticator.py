import hashlib

fname = "ireallydonthaveafirstname "
flag = "xiomara{y0u_g0t_400_p01nt5}"

ln = ""
hw = ""

for i in range(1,4):

    print "\nStage "+str(i)+":\n"

    try:
        lname = raw_input("My last name:\n")
        hashword = raw_input("My hashword:\n")
    except:
        exit("\n")

    if lname == ln or hashword == hw:
        print "I am not a fool. Different credentials each time man."
        exit()

    hashed = hashlib.sha1(fname + lname).hexdigest()

    if hashword == hashed:
        print "\nStage "+str(i)+" cleared!"
    else:
        print "Oops! That's not my first name. Try again"
        exit()

    ln = lname
    hw = hashword

print "\nYou can't be Xiom. He isn't clever enough to break my system. Anyways, here's what you want:\n"
print flag