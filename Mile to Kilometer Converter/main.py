from tkinter import *

FONT = ("Arial", 12, "bold")

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=250)
window.config(padx=50, pady=50)


def m_km_conversion():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    output_text.config(text=f"{km}")


miles_input = Entry(width=16)
miles_input.insert(END, "0")
miles_input.grid(column=1, row=0)

text1 = Label(text="Miles", font=FONT)
text1.grid(column=2, row=0)

text2 = Label(text="is equal to", font=FONT)
text2.grid(column=0, row=1)

output_text = Label(text="0", font=FONT)
output_text.grid(column=1, row=1)

text3 = Label(text="Km", font=FONT)
text3.grid(column=2, row=1)

calc_button = Button(text="Calculate", font=FONT, command=m_km_conversion)
calc_button.grid(column=1, row=2)

window.mainloop()
