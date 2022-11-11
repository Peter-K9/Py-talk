from tkinter import *

#Create a widow for the app
window=Tk()

window.title('Py Talk')
window.geometry('720x400+500+300')
window.minsize(400, 300)
window.config(bg='#4D5656')

# Create a Button
btn = Button(window, text = 'Click me !', bd = '5', command = window.destroy)
 
# Set the position of button on the top of window.  
btn.pack(  
    ipadx=3,
    ipady=3,
    expand=True)   

window.mainloop()