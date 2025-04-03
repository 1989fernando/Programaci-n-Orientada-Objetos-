import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(root, text="Completar Tarea", command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack()

        # Lista de tareas
        self.task_list = tk.Listbox(root, width=50)
        self.task_list.pack(pady=10)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.update_task_list()

    def complete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]["completed"] = True
            self.update_task_list()

    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            status = "[Completada]" if task["completed"] else "[Pendiente]"
            self.task_list.insert(tk.END, f"{status} {task['task']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()