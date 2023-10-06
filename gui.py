import tkinter as tk
from tkinter import ttk
import pandas as pd
from LR_runs import predict_runs, predicted_runs
from temp import winloss

def update_data():
    overs = float(overs_entry.get())
    rpo = float(rpo_entry.get())
    inns = int(inns_entry.get())
    country = str(country_entry.get())
    target = int(target_entry.get())
    
    print(predict_runs(overs, rpo, inns))
    predicted_score_label.config(text=f"Predicted Score: {int(predict_runs(overs, rpo, inns))}")
    winloss_label.config(text = f"Win Loss Prediction: {str(winloss(country, rpo, overs, target))}")

root = tk.Tk()
root.title("Cricket Data Analysis")

# Create and set a custom style for ttk widgets
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14))
style.configure("TButton", font=("Helvetica", 14))

# Set the initial size of the window (width x height)
root.geometry("800x600")  # Adjust the width and height as needed

# Create and place widgets using ttk widgets for better styling
match_summary_label = ttk.Label(root, text="Match Summary:")
match_summary_label.pack(pady=10)

# Add Entry widgets for user input
country_label = ttk.Label(root, text="Opposition Country:")
country_label.pack()
country_entry = ttk.Entry(root)
country_entry.pack(pady=5)

overs_label = ttk.Label(root, text="Overs:")
overs_label.pack()
overs_entry = ttk.Entry(root)
overs_entry.pack(pady=5)

rpo_label = ttk.Label(root, text="RPO (Runs Per Over):")
rpo_label.pack()
rpo_entry = ttk.Entry(root)
rpo_entry.pack(pady=5)

inns_label = ttk.Label(root, text="Innings:")
inns_label.pack()
inns_entry = ttk.Entry(root)
inns_entry.pack(pady=5)

target_label = ttk.Label(root, text="Target Score (to chase):")
target_label.pack()
target_entry = ttk.Entry(root)
target_entry.pack(pady=5)

update_button = ttk.Button(root, text="Predict Runs", command=update_data)
update_button.pack(pady=10)

update_button = ttk.Button(root, text="Predict Win Loss", command=update_data)
update_button.pack(pady=10)

predicted_score_label = ttk.Label(root, text="Predicted Score:")
predicted_score_label.pack(pady=10)

winloss_label = ttk.Label(root, text="Win Loss Prediction:")
winloss_label.pack(pady=10)

quit_button = ttk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()