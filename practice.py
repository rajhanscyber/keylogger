'''f=open("log.txt", 'w')
f.write("I am freaking awesome!")
f.close()'''
with open("log.txt", 'a') as f:
    f.write("I am freaking awesome!")
    #gh=f.read()
    #print(gh)