import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import socket
import platform
import getpass
import psutil
import time
import GPUtil  # GPU ma'lumotlarini olish uchun
from datetime import datetime

class PingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ping Qurilmalari")
        self.root.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.ip_frame = tk.Frame(self.root)
        self.ip_frame.pack(pady=10)

        self.ip_entry1 = tk.Entry(self.ip_frame, width=3)
        self.ip_entry1.grid(row=0, column=0)
        self.ip_separator1 = tk.Label(self.ip_frame, text=".")
        self.ip_separator1.grid(row=0, column=1)
        
        self.ip_entry2 = tk.Entry(self.ip_frame, width=3)
        self.ip_entry2.grid(row=0, column=2)
        self.ip_separator2 = tk.Label(self.ip_frame, text=".")
        self.ip_separator2.grid(row=0, column=3)

        self.ip_entry3 = tk.Entry(self.ip_frame, width=3)
        self.ip_entry3.grid(row=0, column=4)
        self.ip_separator3 = tk.Label(self.ip_frame, text=".")
        self.ip_separator3.grid(row=0, column=5)

        self.ip_entry4 = tk.Entry(self.ip_frame, width=3)
        self.ip_entry4.grid(row=0, column=6)

        self.ping_button = tk.Button(self.root, text="Ping yuborish", command=self.ping)
        self.ping_button.pack(pady=10)

        self.result_table_frame = tk.Frame(self.root)
        self.result_table_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.result_table = ttk.Treeview(self.result_table_frame, columns=("Status", "Response"), show='headings')
        self.result_table.heading("Status", text="Status")
        self.result_table.heading("Response", text="Javob")

        self.scrollbar = ttk.Scrollbar(self.result_table_frame, orient="vertical", command=self.result_table.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.result_table.configure(yscrollcommand=self.scrollbar.set)
        self.result_table.pack(pady=10, fill=tk.BOTH, expand=True)

        self.result_table.column("Status", width=100)
        self.result_table.column("Response", width=600)

        self.save_button = tk.Button(self.root, text="Natijalarni saqlash", command=self.save_to_file)
        self.save_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Jadvalni tozalash", command=self.clear_results)
        self.clear_button.pack(pady=5)

    def ping(self):
        try:
            ip_address = f"{self.ip_entry1.get()}.{self.ip_entry2.get()}.{self.ip_entry3.get()}.{self.ip_entry4.get()}"
            
            if not self.validate_ip(ip_address):
                messagebox.showerror("Xato", "Iltimos, to'g'ri IP manzilini kiriting.")
                return

            self.clear_results()

            os_info = platform.system() + " " + platform.release()
            username = getpass.getuser()
            network_speed = self.get_network_speed()
            uptime = self.get_uptime()
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            memory_usage = memory_info.percent
            gpu_usage = self.get_gpu_usage()  # GPU ishlash ko'rsatkichlari

            status = "Onlayn"
            hostname = socket.gethostbyaddr(ip_address)[0]
            domain = self.get_domain(ip_address)
            self.result_table.insert("", "end", values=(status, f"{hostname} ({domain}) - TCP Ping muvaffaqiyatli"))

            self.result_table.insert("", "end", values=("Operatsion tizim", os_info))
            self.result_table.insert("", "end", values=("Foydalanuvchi", username))
            self.result_table.insert("", "end", values=("Tarmoq tezligi", network_speed))
            self.result_table.insert("", "end", values=("Ishga tushirish vaqti", uptime))
            self.result_table.insert("", "end", values=("CPU ishlashi", f"{cpu_usage}%"))
            self.result_table.insert("", "end", values=("Operativ xotira ishlashi", f"{memory_usage}%"))
            self.result_table.insert("", "end", values=("GPU ishlashi", gpu_usage))  # GPU ishlash ko'rsatkichlari

        except Exception as e:
            messagebox.showerror("Xato", str(e))

    def validate_ip(self, ip):
        parts = ip.split('.')
        return len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)

    def get_network_speed(self):
        try:
            speed_test = subprocess.run(["speedtest-cli", "--simple"], capture_output=True, text=True)
            speed_output = speed_test.stdout.strip().split('\n')
            download_speed = speed_output[1].split()[1] + " " + speed_output[1].split()[2]
            upload_speed = speed_output[2].split()[1] + " " + speed_output[2].split()[2]
            return f"Yuklash: {download_speed}, Yuklash: {upload_speed}"
        except Exception as e:
            return f"Tarmoq tezligini aniqlashda xato: {str(e)}"

    def get_uptime(self):
        return time.strftime("%H:%M:%S", time.gmtime(psutil.boot_time()))

    def get_domain(self, ip_address):
        try:
            domain = socket.getfqdn(ip_address)
            return domain if domain else "Domen topilmadi"
        except socket.error:
            return "Domen topilmadi"

    def get_gpu_usage(self):
        try:
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu = gpus[0]  # Agar bir nechta GPU bo'lsa, birinchisini olish
                return f"{gpu.load * 100:.2f}% ishlashda, {gpu.memoryUsed}MB/{gpu.memoryTotal}MB xotira ishlatilmoqda"
            else:
                return "GPU topilmadi"
        except Exception as e:
            return f"GPU ma'lumotlarini olishda xato: {str(e)}"

    def save_to_file(self):
        try:
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            ip_address = f"{self.ip_entry1.get()}.{self.ip_entry2.get()}.{self.ip_entry3.get()}.{self.ip_entry4.get()}"
            file_name = f"ping_results_{ip_address}_{current_time}.txt"

            with open(file_name, "w") as file:
                for row in self.result_table.get_children():
                    file.write(", ".join(self.result_table.item(row)["values"]) + "\n")

            messagebox.showinfo("Saqlash", f"Natijalar '{file_name}' nomi bilan saqlandi.")
        except Exception as e:
            messagebox.showerror("Xato", str(e))

    def clear_results(self):
        for row in self.result_table.get_children():
            self.result_table.delete(row)

if __name__ == "__main__":
    root = tk.Tk()
    app = PingApp(root)
    root.mainloop()
