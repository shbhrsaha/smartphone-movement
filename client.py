
import datetime, time, pygame

while True:
    
    # exception handling for when trying to read/write at same time...
    # too bad no database :(
    try:

        lines = [line.strip() for line in open("livedata.txt", "r")]

        ax = lines[0]
        ay = lines[1]
        az = lines[2]
        ai = lines[3]
        alpha = lines[4]
        beta = lines[5]
        gamma = lines[6]
        
        #now = datetime.datetime.now()
        
        output =  ax + " " + ay + " " + az + " " + ai + " " + alpha + " " + beta + " " + gamma
    
        #if int(ax) > 15:
            #print "\a"
    
        print output
    
    except:
        continue