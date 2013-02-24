import time, sys

for a in range(0,10) :
        print "first " + str(a)
        time.sleep(0.5)
        
        #pipe is blocking if the line is not read than everything is blocked
        line = sys.stdin.readline()
        if line :
            print "first : received from pipe " + line
               