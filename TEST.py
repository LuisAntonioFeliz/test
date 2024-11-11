import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Vertical Hospital")
ventana.geometry("450x300")

#clase pacientoes
class Pacientes(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=500, height=750)
        self.title("Pacientes")
        self.boton_cerrar = ttk.Button(
            self,
            text="Volver al Inicio",
            command=self.destroy
        )
        self.boton_cerrar.grid(row=0, column=0, padx=6, pady=6)
        #Registro del paciente
        self.lblNombre = ttk.Label(self, text="Nombre:",  font=("Arial", 14))
        self.lblNombre.grid(row=2, column=0, padx=6, pady=6, sticky="e")
        self.txtNombre = tk.Entry(self, font=("Arial", 14), width=25)
        self.txtNombre.grid(row=2, column=1, padx=6, pady=6, sticky="w")

        self.lblApellido = ttk.Label(self, text="Apellido:",  font=("Arial", 14))
        self.lblApellido.grid(row=3, column=0, padx=6, pady=6, sticky="e")
        self.txtApellido = tk.Entry(self, font=("Arial", 14), width=25)
        self.txtApellido.grid(row=3, column=1, padx=6, pady=6, sticky="w")

        self.lblRnc = ttk.Label(self, text="RNC:",  font=("Arial", 14))
        self.lblRnc.grid(row=4, column=0, padx=6, pady=6, sticky="e")
        self.txtRnc = tk.Entry(self, font=("Arial", 14), width=25)
        self.txtRnc.grid(row=4, column=1, padx=6, pady=6, sticky="w")

        self.lblEstado = ttk.Label(self, text="Estado:",  font=("Arial", 14))
        self.lblEstado.grid(row=5, column=0, padx=6, pady=6, sticky="e")
        self.txtEstado = tk.Entry(self, font=("Arial", 14), width=25)
        self.txtEstado.grid(row=5, column=1, padx=6, pady=6, sticky="w")
        
        #creando la tabla de los pacientes
        tablaPacientes = ttk.Treeview(self, columns=("nombre", "apellidos", "rnc", "estado"), show="headings")
        tablaPacientes.heading("nombre", text="Nombre(s)")
        tablaPacientes.heading("apellidos", text="Apellido(s)")
        tablaPacientes.heading("rnc", text="RNC")
        tablaPacientes.heading("estado", text="Estado")
        tablaPacientes.grid(row=6, column=1, padx=6, pady=6, sticky="nsew")

        #funcion para agregar los datos
        def agregar():
            
            valores = (
                self.txtNombre.get(),
                self.txtApellido.get(),
                self.txtRnc.get(),
                self.txtEstado.get()
            )

            tablaPacientes.insert(parent="", index=0, values=valores)

        #boton para insertar los datos
        btnAgregar = tk.Button(self, text="Agregar", font=("Arial", 16), command=agregar)
        btnAgregar.grid(row=6, column=0, padx=6, pady=16, sticky="n")

#clase trataminetos
class Tratamientos(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=500, height=750)
        self.title("Tratamientos")
        self.boton_cerrar = ttk.Button(
            self,
            text="Volver al Inicio",
            command=self.destroy
        )
        self.boton_cerrar.grid(row=0, column=0, padx=6, pady=6)

        #Registro del tratamiento
        self.lblCodigo = ttk.Label(self, text="Codigo:",  font=("Arial", 14))
        self.lblCodigo.grid(row=2, column=0, padx=6, pady=6, sticky="e")
        self.txtCodigo = ttk.Entry(self, font=("Arial", 14), width=25)
        self.txtCodigo.grid(row=2, column=1, padx=6, pady=6, sticky="w")

        self.lblNombre = ttk.Label(self, text="Nombre:",  font=("Arial", 14))
        self.lblNombre.grid(row=3, column=0, padx=6, pady=6, sticky="e")
        self.txtNombre = ttk.Entry(self, font=("Arial", 14), width=25)
        self.txtNombre.grid(row=3, column=1, padx=6, pady=6, sticky="w")

        self.lblMedico = ttk.Label(self, text="Medico:",  font=("Arial", 14))
        self.lblMedico.grid(row=4, column=0, padx=6, pady=6, sticky="e")
        self.txtMedico = ttk.Entry(self, font=("Arial", 14), width=25)
        self.txtMedico.grid(row=4, column=1, padx=6, pady=6, sticky="w")
        
        #creando la tabla de los pacientes
        tablaTratamiento = ttk.Treeview(self, columns=("codigo", "nombre", "medico"), show="headings")
        tablaTratamiento.heading("codigo", text="Codigo")
        tablaTratamiento.heading("nombre", text="Nombre del Tratamiento")
        tablaTratamiento.heading("medico", text="Medico")
        tablaTratamiento.grid(row=5, column=1, padx=6, pady=6, sticky="nsew")

        #funcion para agregar los datos
        def agregar():
            
            valores = (
                self.txtCodigo.get(),
                self.txtNombre.get(),
                self.txtMedico.get()
            )

            tablaTratamiento.insert(parent="", index=0, values=valores)


        #boton para insertar los datos
        btnAgregar = tk.Button(self, text="Agregar", font=("Arial", 16), command=agregar)
        btnAgregar.grid(row=5, column=0, padx=6, pady=16, sticky="n")
        
        self.focus()
        self.grab_set()

#Bienvenido/a
lblBienvenida = tk.Label(ventana, text="Bienvenido/a", font=("Arial", 22, "bold"))
lblBienvenida.grid(row=0, column=1, padx=150, pady=6, sticky="nsew")
lblBienvenida = tk.Label(ventana, text="Seleccione la opcion que desee realizar", font=("Arial", 18))
lblBienvenida.grid(row=1, column=1, padx=50, pady=16, sticky="nsew")

#Opiones a elegir
btnPacientes = tk.Button(ventana, text="Pacientes", font=("Arial", 16), command=Pacientes)
btnPacientes.grid(row=3, column=1, padx=6, pady=6, sticky="n")
btnTratamientos = tk.Button(ventana, text="Tratamientos", font=("Arial", 16), command=Tratamientos)
btnTratamientos.grid(row=4, column=1, padx=6, pady=6, sticky="n")

ventana.mainloop()