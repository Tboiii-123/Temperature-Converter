from tkinter import *

from tkinter import messagebox

from math import *

root = Tk()

root.title("TEMPERATURE CONVERTER")

root.geometry('1000x600')

root.resizable('false','false')

root.configure(bg='blue')




def faren():
     try:
        
        value =fahrenheitinput.get()
        value =float(value)

        celsius = 5/9 *(value -32)
        celsius =round(celsius,5)

        kelvin =5/9 * (value -32) +273.15
        kelvin =round(kelvin,5)

        farshow.config(text=f'{value}*F')
        kelvshow.config(text=f'{kelvin}*K')
        celshow.config(text=f'{celsius}*C')

        messagebox.showinfo('','TEMPERATURE CONVERTED SUCCESSFULLY............')
        

     except ValueError :
         messagebox.showerror('','PLEASE INSERT A NUMBER.........')


def kelvi():
    try:
            
        value =KelvinInput.get()
        value =float(value)

        celsius = value -273.15
        celsius =round(celsius,5)

        fahrenheit = 9/5 *(value -273.15) +13
        fahrenheit =round(fahrenheit,5)

        farshow.config(text=f'{fahrenheit}*F')
        kelvshow.config(text=f'{value}*K')
        celshow.config(text=f'{celsius}*C')


        messagebox.showinfo('','TEMPERATURE CONVERTED SUCCESSFULLY............')

    except ValueError:

        messagebox.showerror('','PLEASE INSERT A NUMBER.........')




def celsi():
    try:
        value =CelsiusInput.get()
        value =float(value)

        kelvin =value +273.15
        
        fahrenheit =9/5 * value +32
        fahrenheit =round(fahrenheit,4)


        farshow.config(text=f'{fahrenheit}*F')
        kelvshow.config(text=f'{kelvin}*K')
        celshow.config(text=f'{value}*C')

        
        messagebox.showinfo('','TEMPERATURE CONVERTED SUCCESSFULLY............')

    except ValueError:
        messagebox.showerror('','PLEASE INSERT A NUMBER.........')


def clear():
    celshow.config(text="")
    
    kelvshow.config(text="")
    
    farshow.config(text="")
    
    KelvinInput.delete(0,END)
    
    CelsiusInput.delete(0,END)
    
    fahrenheitinput.delete(0,END)

    messagebox.showinfo('','RESUlTS CLEARED.....')

#Title

Title =Label(root,text="TEMPERATURE CONVERTER",font=('Calibri',30),fg='red',bg='black')
Title.place(x=250,y=0)




#   FAHRENHEIT
fahrenheit =Label(root,text="FAHRENHEIT",font=('Calibri',27),fg='white',bg='blue')

fahrenheit.place(x=50,y=100)

#Input
fahrenheitinput =Entry(root,bd=3,width=16,font={'Helvetica',12})
fahrenheitinput.place(x=70,y=200)


#Submit
fahrenheitSubmit =Button(root,text="Calculate",width=13,height=2,font=("Heletica",12),bg='green',command=faren )
fahrenheitSubmit.place(x=70,y=260)






#   CELSIUS


Celsius=Label(root,text="CELCIUS",font=('Calibri',27),fg='white',bg='blue')
Celsius.place(x=430,y=100)


#Input
CelsiusInput = Entry(root,bd=3,width=16,font={'Helvetica',12})
CelsiusInput.place(x=425,y=200)

#Submit
Celsiussubmit =Button(root,text="Calculate",width=13,height=2,font=("Heletica",12),bg='green', command=celsi)

Celsiussubmit.place(x=430,y=260)





#    KELVIN

Kelvin =Label(root,text="KELVIN",font=('Calibri',27),fg='white',bg='blue')
Kelvin.place(x=800,y=100)

#Input
KelvinInput =Entry(root,bd=3,width=16,font=('Helvetica',12))
KelvinInput.place(x=750,y=200)


#Submit
KelvinSubmit =Button(root,text="Calculate",width=13,height=2,font=("Heletica",12),bg='green',command=kelvi)
KelvinSubmit.place(x=750,y=260)








# CLEAR WIDGET
Clear =Button(root,text="CLEAR",width=120,height=2,font=("Heletica",12),bg='red',command=clear)
Clear.place(x=0,y=380)



# RESULT

result =Label(root,text="RESULTS:",font=('Calibri',29),fg='green',bg='black')
result.place(x=0,y=430)



# FARSHOW

farshow=Label(root,text="0",font=('Calibri',30),fg='yellow',bg='blue')
farshow.place(x=150,y=500)


#CEL SHOW
celshow=Label(root,text="0",font=('Calibri',30),fg='yellow',bg='blue')
celshow.place(x=400,y=500)



#KELSHOW

kelvshow =Label(root,text="0",font=('Calibri',30),fg='yellow',bg='blue')

kelvshow.place(x=700,y=500)





root.mainloop()
