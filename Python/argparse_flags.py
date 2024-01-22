import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:],           # input 
                           'f:m:',                 # short options
                           ['filename','message']) # long options

print(opts) # anything that have opt are opts -f <arg>, -m <arg>
print(args) # anything that doesnt have opt are args <arg>

for opt, arg in opts:
    if opt == '-f':
        filename=arg
        print(filename)
    elif opt == '-m':
        message=arg
        print(message)

# python3 argparse_flags.py -f test.txt -m "hello world" arg1, arg2