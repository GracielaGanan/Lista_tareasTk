


# Importamos modulo tkinter para crear la interzaz grafica (GUI) segun lo solicitado enel proyecto
#lo vamos a usar para manejar ventanas, botones, etiquetas..etc
import tkinter as tk

#importamos messagebox para mostrar las ventanas emergentes
from tkinter import messagebox


class ListaTareasApp:
    def __init__(self, root):

        #inicializamos atributos

        #guarda la ventana principal
        self.root = root
        #Titulo de la ventana
        self.root.title("Lista de Tareas") #Titulo de la ventana
        self.root.geometry("400x500")  # tamaño de la ventana
        self.root.config(bg="#f7f7f7")  # Color de fondo de la ventana
        self.usuarios = {}  # crea un diccionario para almacenar los usuarios y contraseñas
        self.pantalla_bienvenida()

        #Creamos la pantalla de bienvenida
    def pantalla_bienvenida(self):
        
        for widget in self.root.winfo_children():  #ES para eliminar cualquier widget que quede
            widget.destroy()

        #creamos un contenedor de color rosa y tamaño 400 x 500
        self.bienvenida_frame = tk.Frame(self.root, bg="#FF69B4", width=400, height=500) 
        self.bienvenida_frame.pack_propagate(False)  # Evitamos que se cambie el tamaño segun el contenido
        self.bienvenida_frame.pack()

        bienvenida_label = tk.Label(self.bienvenida_frame, text="¡Tu Lista de Tareas!", 
                                    font=("Comic Sans MS", 22, "bold"), bg="#FF69B4", fg="white")
        bienvenida_label.pack(pady=50)

        # creamos el boton para registrarse
        btn_registrarse = tk.Button(self.bienvenida_frame, text="Registrarse", font=("Verdana", 14), 
                                    command=self.pantalla_registro, relief="raised", bd=3, 
                                    bg="#fff", fg="#FF69B4")
        btn_registrarse.pack(pady=20)

        # Botón para entrar
        btn_inicio_sesion = tk.Button(self.bienvenida_frame, text="Entrar", font=("Verdana", 14), 
                                      command=self.pantalla_inicio_sesion, relief="raised", bd=3, 
                                      bg="#fff", fg="#FF69B4")
        btn_inicio_sesion.pack(pady=20)

    # creamos el metodo que crea la pantalla de registro
    def pantalla_registro(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear el frame para el registro
        self.registro_frame = tk.Frame(self.root, bg="#ffffff", width=400, height=500)
        self.registro_frame.pack_propagate(False) # evita que cambie de tamaño
        self.registro_frame.pack()

        # Etiqueta de registro
        registro_label = tk.Label(self.registro_frame, text="Registrarse", 
                                  font=("Comic Sans MS", 18, "bold"), bg="#ffffff")
        registro_label.pack(pady=50)

        # Campo de entrada para el correo
        self.correo_entry = tk.Entry(self.registro_frame, font=("Helvetica", 14), width=30)
        self.correo_entry.insert(0, "Correo Electrónico")
        self.correo_entry.pack(pady=10)

        # Campo de entrada para la contraseña
        self.contraseña_entry_registro = tk.Entry(self.registro_frame, font=("Helvetica", 14), width=30, show="*")
        self.contraseña_entry_registro.insert(0, "Contraseña")
        self.contraseña_entry_registro.pack(pady=10)

        # Botón para registrar
        btn_registrar = tk.Button(self.registro_frame, text="Registrar", font=("Verdana", 14), 
                                  command=self.registrar_usuario, relief="raised", bd=3, 
                                  bg="#FF69B4", fg="white")
        btn_registrar.pack(pady=20)

        # Botón para volver a la pantalla de bienvenida
        btn_volver = tk.Button(self.registro_frame, text="Volver al inicio", font=("Verdana", 12), 
                               command=self.pantalla_bienvenida, relief="raised", bd=3, 
                               bg="#FF69B4", fg="white")
        btn_volver.pack(pady=10)

    def registrar_usuario(self):
        correo = self.correo_entry.get()
        contraseña = self.contraseña_entry_registro.get()

        if correo and contraseña:
            # Guardar el nuevo usuario y contraseña en el diccionario
            self.usuarios[correo] = contraseña
            messagebox.showinfo("Registro Exitoso", "¡Te has registrado correctamente!")
            self.pantalla_inicio_sesion()  # Volver a la pantalla de inicio para iniciar sesión
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un correo y una contraseña.")

    def pantalla_inicio_sesion(self):
        # Destruir cualquier frame anterior si existe
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear el frame para el inicio de sesión
        self.inicio_sesion_frame = tk.Frame(self.root, bg="#ffffff", width=400, height=500)
        self.inicio_sesion_frame.pack_propagate(False)
        self.inicio_sesion_frame.pack()

        # Etiqueta de inicio de sesión
        inicio_sesion_label = tk.Label(self.inicio_sesion_frame, text="Iniciar Sesión", 
                                       font=("Comic Sans MS", 18, "bold"), bg="#ffffff")
        inicio_sesion_label.pack(pady=50)
        #correo
        self.correo_entry_sesion = tk.Entry(self.inicio_sesion_frame, font=("Helvetica", 14), width=30)
        self.correo_entry_sesion.insert(0, "Correo Electrónico")
        self.correo_entry_sesion.pack(pady=10)

        #contraseña
        self.contraseña_entry_sesion = tk.Entry(self.inicio_sesion_frame, font=("Helvetica", 14), width=30, show="*")
        self.contraseña_entry_sesion.insert(0, "Contraseña")
        self.contraseña_entry_sesion.pack(pady=10)

        # iniciamos sesión
        btn_login = tk.Button(self.inicio_sesion_frame, text="Iniciar Sesión", font=("Verdana", 14), 
                              command=self.verificar_login, relief="raised", bd=3, bg="#FF69B4", fg="white")
        btn_login.pack(pady=20)

    def verificar_login(self):
        correo = self.correo_entry_sesion.get()
        contraseña = self.contraseña_entry_sesion.get()

        # Verificamos si el correo y la contrasenia coinciden
        if correo in self.usuarios and self.usuarios[correo] == contraseña:
            self.pantalla_lista_tareas()
        else:
            messagebox.showerror("Error", "Correo o contraseña incorrectos.")

    def pantalla_lista_tareas(self): # Saca la pantalla de inicio de sesión
        for widget in self.root.winfo_children():
            widget.destroy()

        # Creamos frame(atributos) para la lista de tareas
        self.lista_tareas_frame = tk.Frame(self.root, bg="#ffffff", width=400, height=500)
        self.lista_tareas_frame.pack_propagate(False) # evita que ajuste el tamanio al contenido
        self.lista_tareas_frame.pack()

        # Etiqueta de lista de tareas con una fuente chiquita
        lista_tareas_label = tk.Label(self.lista_tareas_frame, text="Tu Lista de Tareas", 
                                      font=("Comic Sans MS", 16, "bold"), bg="#ffffff")
        lista_tareas_label.pack(pady=20)

        # Cuadro de entrada para nuevas tareas
        self.entry_tarea = tk.Entry(self.lista_tareas_frame, width=30, font=("Helvetica", 14))
        self.entry_tarea.pack(pady=10)

        # mostramos las tareas
        self.lista_tareas = tk.Listbox(self.lista_tareas_frame, font=("Helvetica", 14), width=30, height=10)
        self.lista_tareas.pack(pady=10)

        frame_botones = tk.Frame(self.lista_tareas_frame)
        frame_botones.pack(pady=10)

        btn_agregar = tk.Button(frame_botones, text="Agregar", command=self.agregar_tarea)
        btn_agregar.grid(row=0, column=0, padx=5)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=self.eliminar_tarea)
        btn_eliminar.grid(row=0, column=1, padx=5)

        btn_completar = tk.Button(frame_botones, text="Completar", command=self.completar_tarea)
        btn_completar.grid(row=0, column=2, padx=5)

    def agregar_tarea(self):
        tarea = self.entry_tarea.get() #obtenemos el texto que ingresa el usuario
        if tarea != "":
            self.lista_tareas.insert(tk.END, tarea)
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def eliminar_tarea(self):
        try:
            indice = self.lista_tareas.curselection()[0]
            self.lista_tareas.delete(indice)
        except IndexError:
            messagebox.showerror("Error", "Selecciona una tarea para eliminar.")

    def completar_tarea(self):
        try:
            indice = self.lista_tareas.curselection()[0]
            tarea = self.lista_tareas.get(indice)
            self.lista_tareas.delete(indice)
            self.lista_tareas.insert(tk.END, f"{tarea} ✔")
        except IndexError:
            messagebox.showerror("Error", "Selecciona una tarea para completar.")

if __name__ == "__main__":
    # Crear la ventana principal de la aplicación
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()





