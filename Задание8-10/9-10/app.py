import tkinter as tk
from tkinter import messagebox
from animal import Dog, Cat, Hamster
from registry import AnimalRegistry

class PetRegistryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Registry")
        
        self.registry = AnimalRegistry()
        
        self.create_main_menu()
    
    def create_main_menu(self):
        self.main_menu = tk.Menu(self.root)
        self.root.config(menu=self.main_menu)
        
        self.main_menu.add_command(label="Add Animal", command=self.add_animal_window)
        self.main_menu.add_command(label="List Commands", command=self.list_commands_window)
        self.main_menu.add_command(label="Teach Command", command=self.teach_command_window)
        self.main_menu.add_command(label="Animals by Birth Date", command=self.list_animals_by_birth_date)
    
    def add_animal_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Add New Animal")
        
        tk.Label(self.new_window, text="Name:").grid(row=0, column=0)
        tk.Label(self.new_window, text="Birth Date (YYYY-MM-DD):").grid(row=1, column=0)
        tk.Label(self.new_window, text="Type (dog, cat, hamster):").grid(row=2, column=0)
        
        self.name_entry = tk.Entry(self.new_window)
        self.birth_date_entry = tk.Entry(self.new_window)
        self.type_entry = tk.Entry(self.new_window)
        
        self.name_entry.grid(row=0, column=1)
        self.birth_date_entry.grid(row=1, column=1)
        self.type_entry.grid(row=2, column=1)
        
        tk.Button(self.new_window, text="Add", command=self.add_animal).grid(row=3, column=0, columnspan=2)
    
    def add_animal(self):
        name = self.name_entry.get()
        birth_date = self.birth_date_entry.get()
        animal_type = self.type_entry.get().lower()
        
        if animal_type == "dog":
            animal = Dog(name, birth_date)
        elif animal_type == "cat":
            animal = Cat(name, birth_date)
        elif animal_type == "hamster":
            animal = Hamster(name, birth_date)
        else:
            messagebox.showerror("Error", "Invalid animal type")
            return
        
        self.registry.add_animal(animal)
        messagebox.showinfo("Success", "Animal added successfully")
        self.new_window.destroy()
    
    def list_commands_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("List Commands")
        
        tk.Label(self.new_window, text="Animal Name:").grid(row=0, column=0)
        
        self.animal_name_entry = tk.Entry(self.new_window)
        self.animal_name_entry.grid(row=0, column=1)
        
        tk.Button(self.new_window, text="List", command=self.list_commands).grid(row=1, column=0, columnspan=2)
    
    def list_commands(self):
        animal_name = self.animal_name_entry.get()
        
        for animal in self.registry.animals:
            if animal.name == animal_name:
                commands = animal.get_commands()
                commands_str = ", ".join(commands)
                messagebox.showinfo("Commands", f"{animal_name} can: {commands_str}")
                return
        
        messagebox.showerror("Error", "Animal not found")
    
    def teach_command_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Teach Command")
        
        tk.Label(self.new_window, text="Animal Name:").grid(row=0, column=0)
        tk.Label(self.new_window, text="Command:").grid(row=1, column=0)
        
        self.animal_name_entry = tk.Entry(self.new_window)
        self.command_entry = tk.Entry(self.new_window)
        
        self.animal_name_entry.grid(row=0, column=1)
        self.command_entry.grid(row=1, column=1)
        
        tk.Button(self.new_window, text="Teach", command=self.teach_command).grid(row=2, column=0, columnspan=2)
    
    def teach_command(self):
        animal_name = self.animal_name_entry.get()
        command = self.command_entry.get()
        
        for animal in self.registry.animals:
            if animal.name == animal_name:
                animal.add_command(command)
                messagebox.showinfo("Success", f"{animal_name} learned {command}")
                return
        
        messagebox.showerror("Error", "Animal not found")
    
    def list_animals_by_birth_date(self):
        animals = self.registry.get_animals_by_birth_date()
        animals_str = "\n".join([f"{a.name} - {a.birth_date}" for a in animals])
        messagebox.showinfo("Animals by Birth Date", animals_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = PetRegistryApp(root)
    root.mainloop()
