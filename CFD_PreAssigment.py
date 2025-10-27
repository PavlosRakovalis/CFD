import tkinter as tk
from tkinter import ttk
import pandas as pd

Number_of_elements = 100 
Length = 1 #meters
Initial_temperature = 20 #degrees Celsius
step = Length / Number_of_elements

# Create a pandas DataFrame with two rows:
# - first row (index) named 'x position' contains the spatial positions
# - second row named 'Temperature at T = 0' contains the initial temperatures
positions = [i * step for i in range(Number_of_elements + 1)]
temperatures = [Initial_temperature] * (Number_of_elements + 1)

# apply boundary conditions
temperatures[0] = 100
temperatures[-1] = 20

df = pd.DataFrame([positions, temperatures], index=["x position", "Temperature at T = 0"]) 





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

# Insert data from the DataFrame (one row per spatial point)
for i in range(len(df.columns)):
    pos = df.loc["x position", i]
    temp = df.loc["Temperature at T = 0", i]
    tree.insert("", tk.END, values=(f"{pos:.4f}", temp if temp is not None else "N/A"))

# Add scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)

tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

window.mainloop()



Dt = 0.1  # time step in seconds
Tottal_Running_Time = 1000 * Dt  # total simulation time in seconds


