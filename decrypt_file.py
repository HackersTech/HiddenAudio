import binascii
i=input('\033[34m file name')
byte=input("\033[1;32m bytes-:")
if not byte:
    print('using default value, 0')
    byte=0
else:
    byte=int(byte)

try:
    lis=''
    o=open(i,'r')
    o=o.read()
    o=eval(f'{o}')
    for i in o :
        try:
            i=int(i)/byte
            lis+=str(i)
        except:
            lis+=str(i)
    print(binascii.unhexlify(lis))
except:
    o=open(i,'r')

    
    a=o.read()
    print(a)
    a=a.split()

    for i in range(len(a)):
        l=eval(a[i])
        f=''
        for i in l:
            print(i)
            try:

                f=int(i)/byte
            except:
                f+=str(i)
        print(i,'list have this msg')
        print(eval(f"binascii.unhexlify(b'{f}')"))
