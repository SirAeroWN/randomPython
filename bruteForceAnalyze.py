
####################
### NOT FINISHED ###
####################

#This program accepts an alphanumeric string and lets you know an estimate of how long it would take to brute force it
#It then asks if you would like to try to brute force it

import time

def iterateLast(prefix, password):
    for i in characters[]:
        whole = prefix + characters[i]
        if(whole == password):
            stopTime = time.time()
            return
    

password = input("Enter the alphanumeric string you would like to crack: ")

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
eligableOut = ""
eligableIn = ""

startTime = time.time()
global stopTime = 0
timer = 0
length = 1
count = 0
found = 0

while(timer <= 1.0):
    
        
