import customtkinter as ctk
from tkinter import messagebox

# ---------------- Appearance ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- Functions ----------------
def convert():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15

            result.configure(
                text=f"""Fahrenheit: {fahrenheit:.2f} °F

Celsius: {temp:.2f} °C
Kelvin: {kelvin:.2f} K"""
            )

        elif unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15

            result.configure(
                text=f"""Fahrenheit: {temp:.2f} °F

Celsius: {celsius:.2f} °C
Kelvin: {kelvin:.2f} K"""
            )

        elif unit == "Kelvin":
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32

            result.configure(
                text=f"""Fahrenheit: {fahrenheit:.2f} °F

Celsius: {celsius:.2f} °C
Kelvin: {temp:.2f} K"""
            )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")


def clear():
    entry_temp.delete(0, "end")
    unit_var.set("Celsius")
    result.configure(text="")


# ---------------- Main Window ----------------
root = ctk.CTk()
root.title("Temperature Converter")
root.geometry("900x650")
root.configure(fg_color="#16396B")

# ---------------- Title ----------------
title = ctk.CTkLabel(
    root,
    text="TEMPERATURE CONVERTER",
    font=("Arial", 34, "bold"),
    text_color="white"
)
title.pack(pady=30)

# ---------------- Glass Card ----------------
card = ctk.CTkFrame(
    root,
    width=760,
    height=470,
    corner_radius=25,
    fg_color="#4D6FA8"
)
card.pack(pady=10)
card.pack_propagate(False)

# ---------------- Label ----------------
label = ctk.CTkLabel(
    card,
    text="ENTER TEMPERATURE",
    font=("Arial", 18),
    text_color="white"
)
label.pack(anchor="w", padx=60, pady=(30, 5))

# ---------------- Entry ----------------
entry_temp = ctk.CTkEntry(
    card,
    width=500,
    height=55,
    font=("Arial", 24),
    corner_radius=12
)
entry_temp.pack()

# ---------------- Dropdown ----------------
unit_var = ctk.StringVar(value="Celsius")

dropdown = ctk.CTkOptionMenu(
    card,
    values=["Celsius", "Fahrenheit", "Kelvin"],
    variable=unit_var,
    width=180,
    height=45,
    font=("Arial", 18)
)
dropdown.pack(pady=20)

# ---------------- Buttons ----------------
button_frame = ctk.CTkFrame(card, fg_color="transparent")
button_frame.pack()

convert_btn = ctk.CTkButton(
    button_frame,
    text="Convert",
    command=convert,
    width=180,
    height=50,
    fg_color="green",
    hover_color="#006400",
    font=("Arial", 18, "bold")
)
convert_btn.grid(row=0, column=0, padx=20)

reset_btn = ctk.CTkButton(
    button_frame,
    text="Reset",
    command=clear,
    width=180,
    height=50,
    fg_color="#E74C3C",
    hover_color="#C0392B",
    font=("Arial", 18, "bold")
)
reset_btn.grid(row=0, column=1, padx=20)

# ---------------- Result Card ----------------
result_frame = ctk.CTkFrame(
    card,
    width=600,
    height=180,
    corner_radius=20,
    fg_color="white"
)
result_frame.pack(pady=40)
result_frame.pack_propagate(False)

result = ctk.CTkLabel(
    result_frame,
    text="",
    font=("Arial", 24, "bold"),
    text_color="black",
    justify="center"
)
result.pack(expand=True)

# ---------------- Run ----------------
root.mainloop()
