import tkinter as tk
from tkinter import messagebox

def save_config():
    token = entry_token.get()
    prefix = entry_prefix.get()
    spam_message = entry_spam_message.get(1.0, tk.END).encode('utf-8')
    server_name = entry_server_name.get()
    channel_name = entry_channel_name.get()
    owner_id = entry_owner_id.get()
    cooldown = entry_cooldown.get()
    role_name = entry_role_name.get()
    admin_role = entry_admin_role.get()
    member_name = entry_member_name.get()

    with open('config.py', 'w', encoding='utf-8') as f:
        f.write(f"TOKEN = '{token}'\n")
        f.write(f"PREFIX = '{prefix}'\n")
        f.write(f"SPAM_MESSAGE = {repr(spam_message.decode('utf-8'))}\n")
        f.write(f"SERVER_NAME = '{server_name}'\n")
        f.write(f"CHANNEL_NAME = '{channel_name}'\n")
        f.write(f"OWNER_ID = {owner_id}\n")
        f.write(f"COOLDOWN = {cooldown}\n")
        f.write(f"ROLE_NAME = '{role_name}'\n")
        f.write(f"ADMIN_ROLE = '{admin_role}'\n")
        f.write(f"MEMBER_NAME = '{member_name}'\n")

    messagebox.showinfo("Info", "Бот сконфигурирован!")

def update_config():
    with open('config.py', 'r', encoding='utf-8') as f:
        config = f.read()
        entry_token.delete(0, tk.END)
        entry_token.insert(0, config.split('TOKEN = ')[1].splitlines()[0].strip().replace("'", ""))
        entry_prefix.delete(0, tk.END)
        entry_prefix.insert(0, config.split('PREFIX = ')[1].splitlines()[0].strip().replace("'", ""))
        entry_spam_message.delete(1.0, tk.END)
        entry_spam_message.insert(1.0, config.split('SPAM_MESSAGE = ')[1].splitlines()[0].strip().replace("'", ""))
        entry_server_name.delete(0, tk.END)
        entry_server_name.insert(0, config.split('SERVER_NAME = ')[1].splitlines()[0].strip().replace("'", ""))
        entry_channel_name.delete(0, tk.END)
        entry_channel_name.insert(0, config.split('CHANNEL_NAME = ')[1].splitlines()[0].strip().replace("'", ""))
        entry_owner_id.delete(0, tk.END)
        entry_owner_id.insert(0, config.split('OWNER_ID = ')[1].splitlines()[0].strip())
        entry_cooldown.delete(0, tk.END)
        entry_cooldown.insert(0, config.split('COOLDOWN = ')[1].splitlines()[0].strip())
        entry_role_name.delete(0, tk.END)
        entry_role_name.insert(0, config.split('ROLE_NAME = ')[1].splitlines()[0].strip().replace("'", ""))
        entry_admin_role.delete(0, tk.END)
        entry_admin_role.insert(0, config.split('ADMIN_ROLE = ')[1].splitlines()[0].strip().replace("'", ""))
        entry_member_name.delete(0, tk.END)
        entry_member_name.insert(0, config.split('MEMBER_NAME = ')[1].splitlines()[0].strip().replace("'", ""))

root = tk.Tk()
root.title("Конфигурация")
root.geometry("800x600")
root.configure(bg="#2f2f2f")  # тёмный фон

tk.Label(root, text="Токен бота", font=("Arial", 10), bg="#2f2f2f", fg="#ffffff").grid(row=0, column=0, padx=8, pady=8)
tk.Label(root, text="Префикс команд", font=("Arial", 10), bg="#2f2f2f", fg="#ffffff").grid(row=1, column=0, padx=8, pady=8)
tk.Label(root, text="Сообщение для краша", font=("Arial", 10), bg="#2f2f2f", fg="#ffffff").grid(row=2, column=0, padx=8, pady=8)
tk.Label(root, text="Название сервера", font=("Arial", 10), bg="#2f2f2f", fg="#ffffff").grid(row=3, column=0, padx=8, pady=8)
tk.Label(root, text="Название канала для краша", font=("Arial", 10), bg="#2f2f2f", fg="#ffffff").grid(row=4, column=0, padx=8, pady=8)
tk.Label(root, text="Ваш ID", font=("Arial", 10), bg="#2f2f2f", fg="#ffffff").grid(row=5, column=0, padx=8, pady=8)
tk.Label(root, text="Кулдаун", font=("Arial", 10), bg="#2f2f2f", fg="#ffffff").grid(row=6, column=0, padx=8, pady=8)
tk.Label(root, text="Имя ролей для создания", font=("Arial", 10), bg="#2f2f2f", fg="#ffffff").grid(row=7, column=0, padx=8, pady=8)
tk.Label(root, text="Роль админа", font=("Arial", 10), bg="#2f2f2f", fg="#ffffff").grid(row=8, column=0, padx=8, pady=8)
tk.Label(root, text="Имя для участников", font=("Arial", 10), bg="#2f2f2f", fg="#ffffff").grid(row=9, column=0, padx=8, pady=8)

entry_token = tk.Entry(root, font=("Arial", 10), width=80)
entry_prefix = tk.Entry(root, font=("Arial", 10), width=8)
entry_spam_message = tk.Text(root, font=("Arial", 10), width=50, height=8)
entry_server_name = tk.Entry(root, font=("Arial", 10), width=35)
entry_channel_name = tk.Entry(root, font=("Arial", 10), width=35)
entry_owner_id = tk.Entry(root, font=("Arial", 10), width=35)
entry_cooldown = tk.Entry(root, font=("Arial", 10), width=8)
entry_role_name = tk.Entry(root, font=("Arial", 10), width=35)
entry_admin_role = tk.Entry(root, font=("Arial", 10), width=35)
entry_member_name = tk.Entry(root, font=("Arial", 10), width=35)

entry_token.grid(row=0, column=1, padx=8, pady=8)
entry_prefix.grid(row=1, column=1, padx=8, pady=8)
entry_spam_message.grid(row=2, column=1, padx=8, pady=8)
entry_server_name.grid(row=3, column=1, padx=8, pady=8)
entry_channel_name.grid(row=4, column=1, padx=8, pady=8)
entry_owner_id.grid(row=5, column=1, padx=8, pady=8)
entry_cooldown.grid(row=6, column=1, padx=8, pady=8)
entry_role_name.grid(row=7, column=1, padx=8, pady=8)
entry_admin_role.grid(row=8, column=1, padx=8, pady=8)
entry_member_name.grid(row=9, column=1, padx=8, pady=8)

tk.Button(root, text='Save', command=save_config, font=("Arial", 10), bg="#4CAF50", fg="#ffffff").grid(row=10, column=0, columnspan=2, padx=8, pady=8)

update_config()
root.mainloop()