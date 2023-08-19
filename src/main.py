from CreatePassword import create_pw
import tkinter as tk
import pyperclip

def generate_password():
    try:
        password_length = slider.get()

        if password_length == 1:
            password_result_label.config(text="Generated Password: Passwords with length 1 are not secure.")
        else:
            password = create_pw(password_length)
            password_result_label.config(text=f"Generated Password: {password}")
            generated_password = password  # Store the generated password in a variable

    except Exception as e:
        password_result_label.config(text="Error generating password")

def copy_to_clipboard():
    generated_password = password_result_label.cget("text").split(": ")[1]  # Extract the password from the label text
    pyperclip.copy(generated_password)  # Copy the password to the clipboard

# set up window
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x350")

# icon
icon_path = "favicon.ico"
root.iconbitmap(icon_path)

# password generator title
label = tk.Label(root, text="Password Generator", font=("Helvetica", 16))
label.pack(side="top", pady=20)

# create label for password length slider
result_label = tk.Label(root, text="Select password length")
result_label.pack()

# Create password length slider
slider = tk.Scale(root, from_=1, to=30, orient="horizontal")
slider.pack(pady=10)

# Create generate password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Create "Copy to Clipboard" button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, width=15, height=1)
copy_button.pack(pady=20)

# Create label to display the generated password
password_result_label = tk.Label(root, text="", font=("Helvetica", 12))
password_result_label.pack(pady=10)

root.mainloop()
