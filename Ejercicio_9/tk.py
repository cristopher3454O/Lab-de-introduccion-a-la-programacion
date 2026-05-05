import tkinter as tk
from tkinter import messagebox


class LoginApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Login Tkinter")
        self.root.geometry("360x220")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f7fb")

        self.usuario_correcto = "admin"
        self.contrasena_correcta = "admin2026"

        self._crear_interfaz()

    def _crear_interfaz(self) -> None:
        frame = tk.Frame(self.root, bg="#ffffff", padx=25, pady=25)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        titulo = tk.Label(
            frame,
            text="Iniciar sesión",
            font=("Arial", 16, "bold"),
            bg="#ffffff",
            fg="#1f2937"
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        tk.Label(
            frame,
            text="Usuario",
            font=("Arial", 11),
            bg="#ffffff",
            fg="#374151"
        ).grid(row=1, column=0, sticky="w", pady=5)

        self.entry_usuario = tk.Entry(frame, width=24, font=("Arial", 11))
        self.entry_usuario.grid(row=1, column=1, pady=5)

        tk.Label(
            frame,
            text="Contraseña",
            font=("Arial", 11),
            bg="#ffffff",
            fg="#374151"
        ).grid(row=2, column=0, sticky="w", pady=5)

        self.entry_contrasena = tk.Entry(frame, width=24, font=("Arial", 11), show="*")
        self.entry_contrasena.grid(row=2, column=1, pady=5)

        boton = tk.Button(
            frame,
            text="Ingresar",
            width=18,
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            bd=0,
            cursor="hand2",
            command=self.validar_login
        )
        boton.grid(row=3, column=0, columnspan=2, pady=(18, 0))

        self.entry_usuario.bind("<Return>", self.validar_login_evento)
        self.entry_contrasena.bind("<Return>", self.validar_login_evento)

    def validar_login_evento(self, event: tk.Event) -> None:
        self.validar_login()

    def validar_login(self) -> None:
        usuario = self.entry_usuario.get().strip()
        contrasena = self.entry_contrasena.get().strip()

        if usuario == self.usuario_correcto and contrasena == self.contrasena_correcta:
            messagebox.showinfo("Acceso concedido", "Bienvenido, administrador.")
            self.mostrar_panel()
        else:
            messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos.")

    def mostrar_panel(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.root, bg="#ffffff", padx=30, pady=30)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            frame,
            text="Sesión iniciada",
            font=("Arial", 18, "bold"),
            bg="#ffffff",
            fg="#111827"
        ).pack(pady=(0, 10))

        tk.Label(
            frame,
            text="Usuario autenticado: admin",
            font=("Arial", 11),
            bg="#ffffff",
            fg="#4b5563"
        ).pack(pady=(0, 15))

        tk.Button(
            frame,
            text="Cerrar sesión",
            width=18,
            font=("Arial", 11, "bold"),
            bg="#dc2626",
            fg="white",
            activebackground="#b91c1c",
            activeforeground="white",
            bd=0,
            cursor="hand2",
            command=self.reiniciar
        ).pack()

    def reiniciar(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()
        self._crear_interfaz()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()