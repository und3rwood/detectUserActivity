from pynput import mouse
import time

mouseEvents = []

class click: #creates a click class so that we can easily access the data we need in the 
    def __init__(self, timestamp, kind): #mouseEvents array
        self.timestamp = timestamp #when the click was registered
        self.kind = kind #whether it was a release or a press 
    
def on_click(x,y,button,pressed): #this method gets called by the mouse.listener
    if pressed:
        #print("Button pressed")
        new_click = click(time.time(),"pressed")
        mouseEvents.append(new_click)
    else:
        #print("Button released")
        new_click = click(time.time(),"released")
        mouseEvents.append(new_click)
    for x in mouseEvents:
        print(mouseEvents[x])

with mouse.Listener(on_click=on_click) as listener: #idk how this works bruh
    listener.join()