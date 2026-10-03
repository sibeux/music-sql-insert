import tkinter as tk
from tkinter import messagebox

class ClipboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clipboard Helper")
        self.root.geometry("520x420")
        self.root.minsize(400, 300)

        # Main frame layout
        frame = tk.Frame(root, padx=12, pady=12)
        frame.pack(fill=tk.BOTH, expand=True)

        # Button container
        btn_frame = tk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=(0, 10))

        # Paste Button
        self.paste_btn = tk.Button(
            btn_frame,
            text="📋 Paste (New Line)",
            font=("Segoe UI", 10, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            padx=12,
            pady=6,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.paste_content
        )
        self.paste_btn.pack(side=tk.LEFT, padx=(0, 8))

        # Copy Button
        self.copy_btn = tk.Button(
            btn_frame,
            text="📑 Copy All",
            font=("Segoe UI", 10, "bold"),
            bg="#10b981",
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            padx=12,
            pady=6,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.copy_all_content
        )
        self.copy_btn.pack(side=tk.LEFT, padx=(0, 8))

        # Clear Button
        self.clear_btn = tk.Button(
            btn_frame,
            text="🗑️ Clear",
            font=("Segoe UI", 10),
            bg="#ef4444",
            fg="white",
            activebackground="#dc2626",
            activeforeground="white",
            padx=12,
            pady=6,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.clear_content
        )
        self.clear_btn.pack(side=tk.RIGHT)

        # Status / Feedback label
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = tk.Label(
            frame,
            textvariable=self.status_var,
            font=("Segoe UI", 9),
            fg="#6b7280",
            anchor="w"
        )
        self.status_label.pack(fill=tk.X, pady=(0, 6))

        # Text area with scrollbar
        text_container = tk.Frame(frame)
        text_container.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(text_container)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_area = tk.Text(
            text_container,
            wrap=tk.WORD,
            font=("Consolas", 10),
            yscrollcommand=self.scrollbar.set,
            padx=8,
            pady=8
        )
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.text_area.yview)

    def paste_content(self):
        try:
            clipboard_text = self.root.clipboard_get()
            if not clipboard_text:
                self.show_status("Clipboard is empty.")
                return

            current_text = self.text_area.get("1.0", tk.END)
            
            # If text area already has content (other than the default trailing newline), add a newline
            if current_text.strip():
                if not current_text.endswith("\n"):
                    self.text_area.insert(tk.END, "\n")
                self.text_area.insert(tk.END, clipboard_text + "\n")
            else:
                self.text_area.insert(tk.END, clipboard_text + "\n")

            self.text_area.see(tk.END)
            self.show_status("Pasted from clipboard.")
        except tk.TclError:
            self.show_status("Clipboard is empty or contains non-text data.")

    def copy_all_content(self):
        text_to_copy = self.text_area.get("1.0", tk.END).strip()
        if not text_to_copy:
            self.show_status("Nothing to copy!")
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(text_to_copy)
        self.show_status("All text copied to clipboard!")

    def clear_content(self):
        self.text_area.delete("1.0", tk.END)
        self.show_status("Cleared text area.")

    def show_status(self, message):
        self.status_var.set(message)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClipboardApp(root)
    root.mainloop()
