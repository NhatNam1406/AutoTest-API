import os
import time
from tkinter import *
from tkinter import ttk, messagebox

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Service Request Runner")

        self.service_label = ttk.Label(self, text="Select Service:")
        self.service_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.service_var = StringVar()
        self.service_dropdown = ttk.Combobox(self, textvariable=self.service_var, state="readonly", values=["Service Request", "Company Type", "Container Appointment"])
        self.service_dropdown.grid(row=0, column=1, padx=5, pady=5)

        self.send_button = ttk.Button(self, text="Send", command=self.send_request)
        self.send_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def send_request(self):
        service_folder = self.service_var.get()
        
        # Check if the selected service folder exists
        folder_path = os.path.join("C:\\Users\\nhatn\\Downloads\\Python\\KPCFS-AutoTest\\ATLP Intergration\\Testcase", service_folder)
        if not os.path.exists(folder_path):
            messagebox.showerror("Error", f"Service '{service_folder}' is not available.")
            return

        # Run scripts in the selected service folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".py"):
                file_path = os.path.join(folder_path, file_name)
                os.system(f"python \"{file_path}\"")
                time.sleep(5)  # Add a delay of 5 seconds between each script execution

if __name__ == "__main__":
    app = App()
    app.mainloop()

## How to find the path
# os.system("python \"" + self.file_path + "\"")
