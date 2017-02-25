import base64

key = "iamjokermanandiamawesomenoonecantouchmenoonecankillme"

msg = ["Dear Batman,",
"Their morals, their code; it's a bad joke.",
"Dropped at the first sign of trouble.",
"They're only as good as the world allows them to be.",
"You'll see- I'll show you.",
"When the chips are down these, uh, civilized people?",
"They'll eat each other.",
"Here you go Batman, this is what you seek:",
"y0u_w0n7_ch4n63_3v3n_4f73r_4_7h0u54nd_v3n0n4",
"See I'm not a monster, I'm just ahead of the curve.",
"Yours lovingly,",
"Joker."]

def xor(str1,str2):
    return "".join([chr(ord(str1[i])^ord(str2[i])) for i in xrange(0, len(str1 if len(str1) == len(str2) else str2))])

for i in msg:
    print base64.b64encode(xor(key,i))
