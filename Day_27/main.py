from tkinter import *


def calculate_miles_to_km():
    km = int(miles_input.get()) * 1.609344
    km_output["text"] = round(km)


# create and configure  the window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entry box
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# miles label
miles_label = Label(text="Miles", font=("Arial", 36))
miles_label.grid(column=2, row=0)

# is equal label
is_equal = Label(text="is equal to", font=("Arial", 36))
is_equal.grid(column=0, row=1)

# output label
km_output = Label(text="0", font=("Arial", 36))
km_output.grid(column=1, row=1)

# km label
km_label = Label(text="Km", font=("Arial", 36))
km_label.grid(column=2, row=1)

# calculate button
calculate_button = Button(text="Calculate", command=calculate_miles_to_km)
calculate_button.grid(column=1, row=2)


# keeps window open
window.mainloop()