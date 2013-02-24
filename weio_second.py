import time, sys

for a in range(0,15) :
        print "second " + str(a)
        time.sleep(0.5)
        
        #pipe is blocking if the line is not read than everything is blocked
        line = sys.stdin.readline()
        if line :
            print "second : received from pipe " + line
     