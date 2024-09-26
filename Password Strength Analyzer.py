import tkinter as tk
from tkinter import messagebox

def check_password():
    password = password_entry.get()
    if len(password) >= 8:
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:'\",.<>/?/" for c in password)

        if has_upper and has_lower and has_digit and has_special:
            result = "Very Strong"
            result_color = "#00FF00"  # Green
        elif (has_upper and has_lower and has_digit) or (has_upper and has_lower and has_special) or (has_upper and has_digit and has_special) or (has_lower and has_digit and has_special):
            result = "Strong"
            result_color = "#007FFF"  # Blue
        elif (has_upper and has_lower) or (has_upper and has_special) or (has_upper and has_digit) or (has_lower and has_digit) or (has_lower and has_special) or (has_digit and has_special):
            result = "Weak"
            result_color = "#FFA500"  # Orange
        else:
            result = "Very Weak"
            result_color = "#FF0000"  # Red
    else:
        result = "At RISK"
        result_color = "#FF0000"  # Red

    result_label.config(text=f"Password Complexity: {result}", fg=result_color, font=("Arial", 18, "bold"))

root = tk.Tk()
root.title("Password Complexity Checker")

password_label = tk.Label(root, text="Enter your test password:", font=("Arial", 18, "bold"), fg="#00698F")  # Dark blue
password_label.pack(pady=10)

password_entry = tk.Entry(root, width=40, show="*", font=("Arial", 18), fg="#00698F")  # Dark blue
password_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Password", command=check_password, font=("Arial", 18, "bold"), bg="#34A85A", fg="white")  # Green
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 18, "bold"))
result_label.pack(pady=10)

root.mainloop()
