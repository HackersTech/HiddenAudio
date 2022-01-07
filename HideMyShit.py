#hackers tech 
#/dev/null/
#hacker+programmer

print("""Author of this
\033[33m
 +-+-+-+-+-+-+-+ +-+-+-+-+
 |h|a|c|k|e|r|s| |t|e|c|h|
 +-+-+-+-+-+-+-+ +-+-+-+-+\n""")



import argparse, os,sys,time
parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='file',help='any type of file')
parser.add_argument('-m', dest='secret_msg',help='close it with double quotes')
parser.add_argument('-o', dest='outputfile',help='output file name')
parser.add_argument('-e',dest='encryption_key',help='YES or NO y/n')
parser.add_argument('-b',dest='byte_digit',help='if encryption is selected then use this else leave blank')

args = parser.parse_args()

k=args.file
output=args.outputfile
m=args.secret_msg
enc=args.encryption_key

if  not k and not output and not m :
    print(""" usage: Hidden_secret.py [-h] [-f AUDIOFILE] [-m SECRETMSG] [-o OUTPUTFILE]
required arguments -:
  -h, --help    show the full help menu
  -f AUDIOFILE  Select Audio File
  -m SECRETMSG  Enter your message
  -o OUTPUTFILE Your output file name with extension
  -e ENCRYPTION YES or NO y/n
  -b byte_digit  it should be 1 to infinite
""")
else:
    
    a=input('enter name-: ')
    b=len(a)
    print('tool is used by \n \t')
    j='+''-'
    n=''.join(j*b)
    print(n,end='+')
    print()
    for i in a:
        print(f'|{i}',end='')
    print("|")
    print(''.join(j*b),end='')
    print("+")
    
    if enc=='Y' or enc=='YES' or enc =='y' or enc=='yes':
        try:
            byte=int(args.byte_digit)
        except:
            print('integer value required')
            exit()
        if not byte:
            print('by default value is 1')
            byte=1
        
        import binascii
        bi=eval(f"binascii.hexlify(b'{m}')")
        
        m=bi
        l=[]
        a=str(m).strip(r"b'")
        print(a)
        for i in a:
            #print(i)
            try:

                l.append(str(int(i)*byte))
            except:
                l.append(i)
        m=l 

    import os
    import shutil
    src=k
    dst=output
    print('injecting message in -: ',shutil.copy2(src,dst))
    print('pls wait.. ',end='')
    for _ in range(10):
        for j in '/-\\|':

            sys.stdout.write("\b"+j)
            sys.stdout.flush()
            time.sleep(.08)
    os.system('clear')
    os.rename(output,'i.wav')
    n=open('i.wav',mode='ab')
    a=eval(f'b"      {m}"')
    n.write(a)
    os.rename('i.wav',output)
    print('done')


