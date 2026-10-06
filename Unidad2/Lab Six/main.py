import tkinter as tk
from tkinter import ttk

class SmartDevice:
    def __init__(self, name: str):
        self.name = name
        self.is_on = False

    def execute_action(self) -> str:
        raise NotImplementedError("Subclasses must implement execute_action().")

    def turn_off(self) -> str:
        raise NotImplementedError("Subclasses must implement turn_off().")

    def _toggle(self) -> str:
        self.is_on = not self.is_on
        return "encendido" if self.is_on else "apagado"


class SmartWatch(SmartDevice):
    def execute_action(self) -> str:
        status = self._toggle()
        if self.is_on:
            return f"{self.name}: sincronizando notificaciones y salud ({status})."
        return f"{self.name}: en modo ahorro de bateria ({status})."

    def turn_off(self) -> str:
        self.is_on = False
        return f"{self.name}: notificaciones y monitoreo detenidos (apagado)."


class AppleTV(SmartDevice):
    def execute_action(self) -> str:
        status = self._toggle()
        if self.is_on:
            return f"{self.name}: iniciando plataforma de streaming ({status})."
        return f"{self.name}: reproduccion detenida ({status})."

    def turn_off(self) -> str:
        self.is_on = False
        return f"{self.name}: reproduccion detenida y TV apagada."


class SmartBulb(SmartDevice):
    def __init__(self, name: str):
        super().__init__(name)
        self.brightness = 0

    def execute_action(self) -> str:
        self.is_on = not self.is_on
        self.brightness = 80 if self.is_on else 0
        status = "encendido" if self.is_on else "apagado"
        return f"{self.name}: brillo al {self.brightness}% ({status})."

    def turn_off(self) -> str:
        self.is_on = False
        self.brightness = 0
        return f"{self.name}: luz apagada (brillo al 0%)."


class SmartPlug(SmartDevice):
    def execute_action(self) -> str:
        status = self._toggle()
        if self.is_on:
            return f"{self.name}: energia habilitada para el dispositivo conectado ({status})."
        return f"{self.name}: energia cortada para ahorrar consumo ({status})."

    def turn_off(self) -> str:
        self.is_on = False
        return f"{self.name}: energia cortada para ahorrar consumo (apagado)."


class SmartSpeaker(SmartDevice):
    def execute_action(self) -> str:
        status = self._toggle()
        if self.is_on:
            return f"{self.name}: reproduciendo musica y esperando comandos ({status})."
        return f"{self.name}: reproduccion detenida ({status})."

    def turn_off(self) -> str:
        self.is_on = False
        return f"{self.name}: musica y comandos de voz desactivados (apagado)."

class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- 1. WINDOW SETTINGS---
        self.title("Smart Home")
        self.geometry("470x470")
        self.resizable(False, False)

        # --- 2. OBJECT REGISTRY---
        # Map a friendly Radiobutton label to an instantiated object:
        self.items = {
            "Smartwatch": SmartWatch("Apple Watch"),
            "Apple TV": AppleTV("Apple TV 4K"),
            "Foco Inteligente": SmartBulb("Foco Sala"),
            "Enchufe Inteligente": SmartPlug("Enchufe Cocina"),
            "Bocina Inteligente": SmartSpeaker("Bocina Sala"),
        }

        # Build visual components
        self._build_interface()

    def _build_interface(self):
        lbl_header = tk.Label(
            self,
            text="Smart Home",
            font=("Arial", 13, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=(12, 8))

        group_box = tk.LabelFrame(
            self,
            text="Dispositivos",
            font=("Arial", 9, "bold"),
            padx=15,
            pady=8
        )
        group_box.pack(fill="x", padx=20, pady=5)

        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        for key in self.items.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=2)

        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=(10, 8))

        btn_action = tk.Button(
            buttons_frame,
            text="Ejecutar",
            command=self._handle_action,
            font=("Arial", 10, "bold"),
            padx=12,
            pady=5
        )
        btn_action.pack(side="left", padx=5)

        btn_turn_off = tk.Button(
            buttons_frame,
            text="Apagar",
            command=self._handle_turn_off,
            font=("Arial", 10, "bold"),
            padx=12,
            pady=5
        )
        btn_turn_off.pack(side="left", padx=5)

        self.lbl_output = tk.Label(
            self,
            text="Selecciona un dispositivo y presiona Ejecutar.",
            font=("Arial", 10),
            bg="#f2f2f2",
            fg="#34495e",
            relief="groove",
            height=2,
            wraplength=350,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

        log_frame = tk.LabelFrame(
            self,
            text="Registro de actividad",
            font=("Arial", 9, "bold"),
            padx=8,
            pady=6
        )
        log_frame.pack(fill="both", expand=True, padx=20, pady=(5, 10))

        self.activity_log = tk.Listbox(
            log_frame,
            height=6,
            font=("Arial", 9),
            activestyle="none"
        )
        self.activity_log.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(
            log_frame,
            orient="vertical",
            command=self.activity_log.yview
        )
        scrollbar.pack(side="right", fill="y")
        self.activity_log.config(yscrollcommand=scrollbar.set)

    def _record_activity(self, message: str):
        self.activity_log.insert(tk.END, message)
        self.activity_log.see(tk.END)

    def _handle_action(self):
        # 1. Get the current key selected by the user
        chosen_key = self.selected_key.get()

        # 2. Retrieve the active polymorphic object
        active_object: SmartDevice = self.items[chosen_key]

        # 3. POLYMORPHIC EXECUTION:
        # No 'if/elif' logic needed. Python runs the appropriate implementation!
        result_message = active_object.execute_action()

        # 4. Display result in the UI
        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))
        self._record_activity(f"Ejecutar - {result_message}")

    def _handle_turn_off(self):
        chosen_key = self.selected_key.get()
        active_object: SmartDevice = self.items[chosen_key]
        result_message = active_object.turn_off()

        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))
        self._record_activity(f"Apagar - {result_message}")



# LAUNCHER
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()