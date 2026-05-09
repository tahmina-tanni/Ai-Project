# ui/app.py
import tkinter as tk
from tkinter import scrolledtext
import os

class HealthAssistantUI:
    def __init__(self, root, graph):
        self.root = root
        self.graph = graph
        # Initialize state for 20 questions
        self.state = {"current_idx": 0, "responses": [], "is_finished": False}
        self.history_file = "chat_history.txt"

        # 1. WINDOW SETUP (HARD CONSTRAINTS)
        self.root.title("Smart Health Assistant")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#F0F2F5")

        # 2. UI ARCHITECTURE
        self._setup_ui()

        # 3. INITIALIZE LOGIC
        self.load_history_from_file()
        self.process_flow("") 

    def _setup_ui(self):
        """Builds UI with strict frame hierarchy to prevent overflow."""
        
        # --- TOP HEADER ---
        header = tk.Frame(self.root, bg="#0084FF", height=50)
        header.pack(side="top", fill="x")
        tk.Label(header, text="🩺 20-Point Health Audit", fg="white", 
                 bg="#0084FF", font=("Arial", 12, "bold"), pady=10).pack()

        # --- BOTTOM FRAME (Fixed & Always Visible) ---
        # Packed FIRST with side="bottom" to anchor it to the window floor
        self.bottom_frame = tk.Frame(self.root, bg="white", pady=10, padx=10)
        self.bottom_frame.pack(side="bottom", fill="x")

        # Action Buttons (Right)
        btn_container = tk.Frame(self.bottom_frame, bg="white")
        btn_container.pack(side="right")

        self.send_btn = tk.Button(
            btn_container, text="SEND", bg="#0084FF", fg="white",
            font=("Arial", 10, "bold"), relief="flat", 
            padx=15, pady=5, command=self.send, cursor="hand2"
        )
        self.send_btn.pack(side="right", padx=(5, 0))

        self.clear_btn = tk.Button(
            btn_container, text="CLEAR", bg="#E74C3C", fg="white",
            font=("Arial", 10, "bold"), relief="flat", 
            padx=15, pady=5, command=self.clear_chat, cursor="hand2"
        )
        self.clear_btn.pack(side="right", padx=5)

        # Entry Box (Left - Expands horizontally)
        self.user_entry = tk.Entry(
            self.bottom_frame, font=("Arial", 11), 
            bg="#F0F2F5", relief="flat", bd=0
        )
        self.user_entry.pack(side="left", fill="x", expand=True, ipady=8)
        self.user_entry.bind("<Return>", lambda e: self.send())
        self.user_entry.focus_set()

        # --- CHAT FRAME (Middle - Fills remaining space) ---
        # Packed after bottom_frame so it respects the bottom frame's space
        self.chat_frame = tk.Frame(self.root, bg="#F0F2F5")
        self.chat_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.chat_box = scrolledtext.ScrolledText(
            self.chat_frame, state='disabled', wrap="word",
            font=("Arial", 10), bg="white", relief="flat",
            padx=10, pady=10
        )
        self.chat_box.pack(fill="both", expand=True)

    def clear_chat(self):
        """Resets UI, Memory, and Persistence."""
        self.chat_box.config(state='normal')
        self.chat_box.delete("1.0", tk.END)
        self.chat_box.config(state='disabled')
        self.state = {"current_idx": 0, "responses": [], "is_finished": False}
        if os.path.exists(self.history_file):
            open(self.history_file, "w", encoding="utf-8").close()
        self.process_flow("")

    def load_history_from_file(self):
        if not os.path.exists(self.history_file): return
        try:
            with open(self.history_file, "r", encoding="utf-8") as f:
                data = f.read()
            if data:
                self.chat_box.config(state='normal')
                self.chat_box.insert("end", "--- PREVIOUS HISTORY ---\n", "sys")
                self.chat_box.insert("end", data + "\n")
                self.chat_box.insert("end", "--- NEW SESSION ---\n\n", "sys")
                self.chat_box.tag_config("sys", foreground="gray", font=("Arial", 9, "italic"))
                self.chat_box.config(state='disabled')
                self.chat_box.see("end")
        except: pass

    def save_to_file(self, sender, message):
        with open(self.history_file, "a", encoding="utf-8") as f:
            f.write(f"{sender}: {message}\n")

    def send(self):
        text = self.user_entry.get().strip()
        if not text: return
        self.display(f"You: {text}", "user")
        self.save_to_file("You", text)
        self.user_entry.delete(0, "end")
        self.root.after(300, lambda: self.process_flow(text))

    def process_flow(self, user_input):
        if user_input:
            self.state["responses"].append(user_input)
            self.state["current_idx"] += 1

        res = self.graph.invoke(self.state)
        self.state.update(res)
        
        bot_text = self.state.get('next_question', 'Assessment complete.')
        self.display(f"Bot: {bot_text}", "bot")
        
        if user_input: 
            self.save_to_file("Bot", bot_text)

    def display(self, text, tag):
        self.chat_box.config(state='normal')
        self.chat_box.insert("end", text + "\n\n", tag)
        self.chat_box.tag_config("user", foreground="#0084FF", font=("Arial", 10, "bold"))
        self.chat_box.tag_config("bot", foreground="#333333")
        self.chat_box.config(state='disabled')
        self.chat_box.see("end")