import socket
import sys,os
import subprocess

# list with filenames
calling = ["weio_first", "weio_second"]

#list where processes will be stored
processes = []
#dictionary od PIDs for each process number:name
pids = {}

#run processes from list
for name in calling :
    # -u parameter runs pythnon in unbuffered mode,
    # that means that after each print python will flush stdout.
    # It's like sys.stdout.flush() inside running process
    p = subprocess.Popen(['python', '-u', name + ".py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE) 
    processes.append(p) #add running process to the list
    # associate each pid number with his name
    pids[str(p.pid)] = name

counter = 0
processRuns = True
while processRuns :
    
    # read stdin from all processes and print them
    for p in processes :
        
        #check if process is alive, if not close stdin and remove the object
        if p.poll() is not None :
            print "MASTER : Process PID : " + pids[str(p.pid)]  + " is terminated"
            processes.remove(p)
            break
        
        line = p.stdout.readline()
        if line :
            print line
            
        #write somethnig to stdin
        if (counter<10) :
           counter = counter + 1
        else :
           counter = 0
        msg = str(counter)+ '\n' # \n is added because sys.stdin.readline() is used at the other end of PIPE
        
        #TODO don't know why pipe is broken here when a process is terminated, normally it don't exist anymore
        try :
            p.stdin.write(msg)
            p.stdin.flush()
        except :
            print "MASTER : aouch! " + pids[str(p.pid)] + " process will die"        
            
    # quit infinite loop is all processes are finished
    if (len(processes)==0):
        processRuns = False
        
print "MASTER : all processes are finished"


