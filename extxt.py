
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='file',help='hidden msg finder/extracter file')
parser.add_argument('-k', dest='dec',help='file is encrypted yes or no else leave blank',required=False)
parser.add_argument('-b', dest='byte',help='file is encrypted then give byte digit else leave blank',required=False)

arg=parser.parse_args()
f=arg.file
dec=arg.dec

if not f :
    print('''\033[32m usage: extxt.py [-h --help] [-f AUDIOFILE] [-k private key file ]
optional arguments -:
  -h, --help       show the full help menu
  -f AUDIOFILE     Select Audio File
\033[38;5;232;48;5;227m  -k DECRYPTION           yes or y if message is encrypted else leave this argument
  -b BYTES         decryption digit that is used while encrypting                  \033[0m ''',end='\033[0m')
   
    exit()



 
import binascii
if dec==None:
    print('')
    o=open(f,'rb')
    r=o.read()
    
    r=str(r).split("      ")
    print(r[1].strip("b'"))
    print('\n \033[32m msg extracted successfully')
elif dec=='y' or dec=='YES' or dec=="yes" or dec=="Y":
    try:
        byte=int(args.byte_digit)
    except:
        print('integer value required')
        exit()
    if not byte:
        print('bytes using default value 1')
        byte=1
    
    o=open(f,'rb')
    r=o.read()
    r=r.partition(b"      ")
    pn=str(r[2]).strip("b'")
    pn=pn.strip('b"')
    
    print(pn)
    print('\033[34m enter this list to decrypt the hidden message')
    pn=eval(input("""-> """))
    
#    r=str(r).partition("      ")
 #   r=r[2]
  #  t=(''.join(r.strip("b'\")))
   # print(t)
    try:
        print('\033[33m decrypting the numbers')
        m=''
        for j in pn:
            
            try:
                m+=str(int(int(j)/byte))
            except:
                m+=j
# print(m)
# bn=eval(f"binascii.unhexlify(b'{m}')")
        print(binascii.unhexlify(m),'\n \n','\033[32m message decrypted successfully ')
    except:
        print('\033[31m message byte is wrong or incorrect')

 
else:
    pass
