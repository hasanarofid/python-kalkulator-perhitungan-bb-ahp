import tkinter as tk

def on_click(button_value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(button_value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator")

# Membuat entri (entry) untuk menampilkan dan memasukkan angka
entry = tk.Entry(root, width=16, font=("Helvetica", 12))  # Reduced font size to 12
entry.grid(row=0, column=0, columnspan=4)

# Tombol-tombol kalkulator
buttons = [
    ('7', '#b3b3b3'), ('8', '#b3b3b3'), ('9', '#b3b3b3'), ('/', '#ff6666'),
    ('4', '#b3b3b3'), ('5', '#b3b3b3'), ('6', '#b3b3b3'), ('*', '#ff6666'),
    ('1', '#b3b3b3'), ('2', '#b3b3b3'), ('3', '#b3b3b3'), ('-', '#ff6666'),
    ('0', '#b3b3b3'), ('C', '#ff6666'), ('=', '#66ff66'), ('+', '#ff6666')
]

row_val = 1
col_val = 0

for button, color in buttons:
    tk.Button(root, text=button, width=4, height=2, bg=color, command=lambda b=button: on_click(b) if b != '=' else calculate() if b=='=' else clear_entry()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Menjalankan aplikasi
root.mainloop()
