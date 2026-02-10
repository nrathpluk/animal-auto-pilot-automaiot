import customtkinter as ctk
import pyautogui
import time
import random
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class AnimalAutoPilot(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.setup_keybinds()
        self.title("🐾 Animal Auto Pilot")
        self.geometry("720x760")
        self.resizable(False, False)

        # ===== State =====
        self.is_running = False

        # ===== Click Sets =====
        self.set_A = [(693, 939), (649, 830), (828, 941), (782, 836), (960, 937),
                      (909, 825), (1094, 939), (1044, 837), (1224, 940), (1182, 827)]
        self.set_B = [(649, 830), (782, 836), (909, 825),
                      (1044, 837), (1182, 827)]
        self.set_C = [(693, 939), (828, 941), (960, 937),
                      (1094, 939), (1224, 940)]

        self.wait_minutes = 17

        self.build_ui()

    def setup_keybinds(self):
        self.bind("<Escape>", self.on_esc)
        self.bind("<Prior>", self.on_Prior)

    def on_Prior(self, event=None):
        self.start()

    def on_esc(self, event=None):
        self.stop()
    # ================= UI =================

    def build_ui(self):

        header = ctk.CTkFrame(self, height=60, corner_radius=0)
        header.pack(fill="x")

        ctk.CTkLabel(
            header,
            text="🐾 Animal Auto Pilot",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(side="left", padx=20)

        self.status_label = ctk.CTkLabel(
            header, text="● Idle", text_color="gray"
        )
        self.status_label.pack(side="right", padx=20)

        main = ctk.CTkFrame(self, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=20, pady=20)

        self.log = ctk.CTkTextbox(main)
        self.log.pack(fill="both", expand=True)

        actions = ctk.CTkFrame(main, fg_color="transparent")
        actions.pack(fill="x", pady=15)

        self.start_btn = ctk.CTkButton(
            actions, text="▶ Start", height=50, command=self.start
        )
        self.start_btn.pack(side="left", expand=True, fill="x", padx=5)

        self.stop_btn = ctk.CTkButton(
            actions, text="■ Stop", height=50,
            fg_color="#ef4444", state="disabled",
            command=self.stop
        )
        self.stop_btn.pack(side="left", expand=True, fill="x", padx=5)

        self.log_message("Ready 🚀")

    # ================= Core Logic =================

    def start(self):
        self.is_running = True
        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self.status_label.configure(text="● Running", text_color="green")

        threading.Thread(target=self.loop, daemon=True).start()

    def stop(self):
        self.is_running = False
        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.status_label.configure(text="● Idle", text_color="gray")
        self.log_message("Stopped")

    # ===== Click Helper =====
    def do_clicks(self, positions, name):
        self.log_message(f"Running {name}")
        for x, y in positions:
            if not self.is_running:
                return False
            rx = x + random.randint(-4, 4)
            ry = y + random.randint(-4, 4)
            pyautogui.moveTo(rx, ry, duration=random.uniform(0.5, 1.2))
            pyautogui.click()
            time.sleep(random.uniform(0.3, 0.7))
        return True

    # ===== Wait Helper =====
    def wait_minutes_block(self, minutes):
        self.log_message(f"Waiting {minutes} minutes...")
        for _ in range(minutes * 60):
            if not self.is_running:
                return False
            time.sleep(1)
        return True

    # ===== Main Loop =====
    def loop(self):
        while self.is_running:

            if not self.do_clicks(self.set_A, "Set A"):
                return
            if not self.wait_minutes_block(self.wait_minutes):
                return

            if not self.do_clicks(self.set_B, "Set B"):
                return
            if not self.wait_minutes_block(self.wait_minutes):
                return

            if not self.do_clicks(self.set_C, "Set C"):
                return
            # กลับไป Set A ทันที

    # ===== Log =====
    def log_message(self, msg):
        self.log.insert("end", f"{time.strftime('%H:%M:%S')}  {msg}\n")
        self.log.see("end")


if __name__ == "__main__":
    app = AnimalAutoPilot()
    app.mainloop()
