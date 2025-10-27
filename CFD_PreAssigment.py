import tkinter as tk
from tkinter import ttk

Number_of_elements = 100 
Length = 1 #meters
Initial_temperature = 20 #degrees Celsius
step = Length / Number_of_elements
table = [
    [i * step for i in range(Number_of_elements + 1)],
    [Initial_temperature] * (Number_of_elements + 1)
]

table[1][0] = 100
table[1][-1] = 20





# Create popup window
window = tk.Tk()
window.title("CFD Data Table")

# Create frame for table
frame = ttk.Frame(window, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create treeview for table display
tree = ttk.Treeview(frame, columns=("Position", "Temperature"), show="headings", height=15)
tree.heading("Position", text="Position (m)")
tree.heading("Temperature", text="Temperature (°C)")

# Insert data
for i in range(len(table[0])):
    tree.insert("", tk.END, values=(f"{table[0][i]:.4f}", table[1][i] if table[1][i] is not None else "N/A"))

# Add scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)

tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

window.mainloop()



Dt = 0.1  # time step in seconds
Tottal_Running_Time = 1000 * Dt  # total simulation time in seconds




