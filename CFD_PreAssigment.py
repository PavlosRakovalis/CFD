import tkinter as tk
from tkinter import ttk
import pandas as pd

Number_of_elements = 100 
Length = 1 #meters
Initial_temperature = 20 #degrees Celsius
step = Length / Number_of_elements

Dt = 0.1  # time step in seconds
Number_of_iterations = 1000
Total_Running_Time = Number_of_iterations * Dt  # total simulation time in seconds









# Create a pandas DataFrame with two rows:
# We'll structure the DataFrame so each ROW is a time snapshot (index = time in seconds)
# and each COLUMN is a spatial position (column labels = x positions). This layout
# makes plotting straightforward: x = df.columns, y = df.loc[time].
positions = [i * step for i in range(Number_of_elements + 1)]
temperatures = [Initial_temperature] * (Number_of_elements + 1)

# apply boundary conditions for the initial snapshot
temperatures[0] = 100
temperatures[-1] = 20

# create DataFrame with one row (iteration 0) and columns equal to positions
df = pd.DataFrame([temperatures], index=[0], columns=positions)






# (We will create new rows as we compute each time step below.)









# Material property
alpha = 0.0001  # thermal diffusivity (m²/s) - adjust as needed

# Update temperatures for each iteration using finite difference method.
# Rows in df are indexed by iteration number; columns are spatial positions.
for iteration in range(1, Number_of_iterations + 1):
    # Get previous temperature distribution as a numpy array
    T_prev = df.loc[iteration - 1].values

    # allocate new temperature array and apply update for internal nodes
    T_new = T_prev.copy()
    for i in range(1, Number_of_elements):
        T_new[i] = T_prev[i] + alpha * Dt / (step ** 2) * (T_prev[i+1] - 2 * T_prev[i] + T_prev[i-1])

    # enforce boundary conditions
    T_new[0] = 100
    T_new[-1] = 20

    # store new row at iteration number
    df.loc[iteration] = T_new










# Create popup window
window = tk.Tk()
window.title("CFD Data Table")

# Create frame for table
frame = ttk.Frame(window, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create treeview for table display showing the entire DataFrame
# Columns: Time (index) + all spatial positions (first 10 positions to keep it manageable)
# If you want ALL positions, replace positions_to_show with df.columns
positions_to_show = list(df.columns)[:min(10, len(df.columns))]  # show first 10 positions
col_names = ["Time (s)"] + [f"x={pos:.4f}" for pos in positions_to_show]

tree = ttk.Treeview(frame, columns=col_names, show="headings", height=20)
for col in col_names:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Insert all rows (time snapshots) from the DataFrame
for time_idx in df.index:
    row_values = [f"{time_idx:.2f}"]
# Insert all rows (time snapshots) from the DataFrame
for iter_idx in df.index:
    time_seconds = iter_idx * Dt
    row_values = [f"{time_seconds:.2f}"]
    for pos in positions_to_show:
        temp = df.loc[iter_idx, pos]
        row_values.append(f"{temp:.2f}" if temp is not None else "N/A")
    tree.insert("", tk.END, values=row_values)

# Add scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)

tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

window.mainloop()


