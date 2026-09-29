import os
import sys
import subprocess
import threading
import queue
import re
import tkinter as tk
from tkinter import ttk, messagebox

# Mapping 4 folder ke destinasi rclone
UPLOAD_TARGETS = [
    {
        "id": "1-indopride",
        "name": "1. IndoPride",
        "local_rel": "1-indopride",
        "remote": "b2remote:cybeat-sibeux/files/music/indopride",
    },
    {
        "id": "2-Anisong",
        "name": "2. Anisong",
        "local_rel": "2-Anisong",
        "remote": "b2remote:cybeat-sibeux/files/music/anisong",
    },
    {
        "id": "4-worldwide",
        "name": "4. Worldwide",
        "local_rel": "4-worldwide",
        "remote": "b2remote:cybeat-sibeux/files/music/worldwide",
    },
    {
        "id": "5-instrumental",
        "name": "5. Instrumental",
        "local_rel": "5-instrumental",
        "remote": "b2remote:cybeat-sibeux/files/music/instrumental",
    }
]

class MusicUploaderApp(tk.Tk):
    def __init__(self, base_dir):
        super().__init__()
        self.base_dir = base_dir
        self.title("Music Uploader to Backblaze B2 (Rclone)")
        self.geometry("900x680")
        self.minsize(800, 580)
        
        self.is_running = False
        self.current_process = None
        self.log_queue = queue.Queue()
        
        self.setup_ui()
        self.after(100, self.process_log_queue)

    def setup_ui(self):
        self.configure(bg="#1e1e2e")
        
        style = ttk.Style(self)
        if "clam" in style.theme_names():
            style.theme_use("clam")
            
        style.configure(".", background="#1e1e2e", foreground="#cdd6f4", font=("Segoe UI", 9))
        style.configure("Horizontal.TProgressbar", 
                        troughcolor="#313244", 
                        background="#89b4fa", 
                        lightcolor="#89b4fa", 
                        darkcolor="#89b4fa", 
                        bordercolor="#1e1e2e")

        # Top Header
        top_frame = tk.Frame(self, bg="#282a36", padx=20, pady=12)
        top_frame.pack(fill=tk.X)
        
        lbl_title = tk.Label(top_frame, text="☁️ Backblaze B2 Music Batch Uploader", 
                             font=("Segoe UI", 13, "bold"), bg="#282a36", fg="#89b4fa")
        lbl_title.pack(anchor="w")
        
        lbl_sub = tk.Label(top_frame, text=f"Base Directory: {self.base_dir}", 
                           font=("Consolas", 8), bg="#282a36", fg="#9399b2")
        lbl_sub.pack(anchor="w", pady=(2, 0))

        # Folder List / Status Grid
        folder_frame = tk.LabelFrame(self, text="  Target Upload Folders & Status  ", 
                                     bg="#1e1e2e", fg="#a6adc8", font=("Segoe UI", 9, "bold"), padx=15, pady=10)
        folder_frame.pack(fill=tk.X, padx=15, pady=10)

        self.folder_status_labels = {}
        for idx, item in enumerate(UPLOAD_TARGETS):
            row = tk.Frame(folder_frame, bg="#1e1e2e")
            row.pack(fill=tk.X, pady=3)
            
            lbl_name = tk.Label(row, text=item["name"], font=("Segoe UI", 9, "bold"), 
                                width=18, anchor="w", bg="#1e1e2e", fg="#cdd6f4")
            lbl_name.pack(side=tk.LEFT)
            
            lbl_dest = tk.Label(row, text=f"➜ {item['remote']}", font=("Consolas", 8), 
                                width=48, anchor="w", bg="#1e1e2e", fg="#6c7086")
            lbl_dest.pack(side=tk.LEFT, padx=5)
            
            lbl_stat = tk.Label(row, text="● Pending", font=("Segoe UI", 9), 
                                width=15, anchor="e", bg="#1e1e2e", fg="#bac2de")
            lbl_stat.pack(side=tk.RIGHT)
            
            self.folder_status_labels[item["id"]] = lbl_stat

        # Progress Section
        prog_frame = tk.Frame(self, bg="#1e1e2e", padx=15)
        prog_frame.pack(fill=tk.X)

        self.lbl_progress_status = tk.Label(prog_frame, text="Status: Ready to upload.", 
                                            font=("Segoe UI", 9, "bold"), bg="#1e1e2e", fg="#a6e3a1")
        self.lbl_progress_status.pack(anchor="w", pady=(0, 4))

        self.lbl_speed_info = tk.Label(prog_frame, text="Speed: - | Transferred: - | ETA: -", 
                                       font=("Segoe UI", 8), bg="#1e1e2e", fg="#bac2de")
        self.lbl_speed_info.pack(anchor="w", pady=(0, 4))

        self.progress_bar = ttk.Progressbar(prog_frame, orient="horizontal", mode="determinate", 
                                            style="Horizontal.TProgressbar")
        self.progress_bar.pack(fill=tk.X, pady=(0, 10))

        # Real-time Console Log Terminal
        log_frame = tk.LabelFrame(self, text="  Live Rclone Console Output  ", 
                                  bg="#1e1e2e", fg="#a6adc8", font=("Segoe UI", 9, "bold"), padx=10, pady=6)
        log_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))

        self.txt_log = tk.Text(log_frame, bg="#11111b", fg="#cdd6f4", font=("Consolas", 9), 
                               wrap="word", relief=tk.FLAT, padx=8, pady=8)
        scroll_y = ttk.Scrollbar(log_frame, orient="vertical", command=self.txt_log.yview)
        self.txt_log.configure(yscrollcommand=scroll_y.set)

        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.txt_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Bottom Button Bar
        btn_frame = tk.Frame(self, bg="#1e1e2e", padx=15, pady=8)
        btn_frame.pack(fill=tk.X)

        self.btn_run = tk.Button(btn_frame, text="▶ RUN UPLOAD ALL", bg="#a6e3a1", fg="#11111b",
                                 font=("Segoe UI", 10, "bold"), relief=tk.FLAT, padx=20, pady=6,
                                 cursor="hand2", command=self.start_upload)
        self.btn_run.pack(side=tk.RIGHT, padx=5)

        self.btn_stop = tk.Button(btn_frame, text="⏹ Stop", bg="#f38ba8", fg="#11111b",
                                  font=("Segoe UI", 10, "bold"), relief=tk.FLAT, padx=15, pady=6,
                                  cursor="hand2", state=tk.DISABLED, command=self.stop_upload)
        self.btn_stop.pack(side=tk.RIGHT, padx=5)

        self.btn_clear = tk.Button(btn_frame, text="Clear Log", bg="#313244", fg="#cdd6f4",
                                   font=("Segoe UI", 9), relief=tk.FLAT, padx=12, pady=6,
                                   cursor="hand2", command=self.clear_log)
        self.btn_clear.pack(side=tk.LEFT)

    def log(self, text, tag=None):
        self.txt_log.insert(tk.END, text + "\n")
        self.txt_log.see(tk.END)

    def clear_log(self):
        self.txt_log.delete("1.0", tk.END)

    def start_upload(self):
        if self.is_running:
            return
        
        self.is_running = True
        self.btn_run.config(state=tk.DISABLED, bg="#45475a")
        self.btn_stop.config(state=tk.NORMAL)
        self.clear_log()
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = len(UPLOAD_TARGETS) * 100

        # Reset folder statuses
        for item in UPLOAD_TARGETS:
            self.folder_status_labels[item["id"]].config(text="● Pending", fg="#bac2de")

        threading.Thread(target=self.run_upload_thread, daemon=True).start()

    def stop_upload(self):
        if self.current_process and self.current_process.poll() is None:
            self.current_process.terminate()
            self.log("⚠️ Upload proses dihentikan oleh user.")
        self.is_running = False

    def run_upload_thread(self):
        total_folders = len(UPLOAD_TARGETS)
        
        for idx, target in enumerate(UPLOAD_TARGETS):
            if not self.is_running:
                break
                
            folder_id = target["id"]
            folder_name = target["name"]
            local_path = os.path.join(self.base_dir, target["local_rel"])
            remote_dest = target["remote"]
            
            # Update folder status
            self.log_queue.put(("status_lbl", (folder_id, "⏳ Uploading...", "#f9e2af")))
            self.log_queue.put(("overall_status", f"Processing {idx+1}/{total_folders}: {folder_name}"))
            self.log_queue.put(("log", f"\n======================================================="))
            self.log_queue.put(("log", f"🚀 Starting Upload [{idx+1}/{total_folders}]: {folder_name}"))
            self.log_queue.put(("log", f"📂 Local:  {local_path}"))
            self.log_queue.put(("log", f"☁️ Remote: {remote_dest}"))
            self.log_queue.put(("log", f"======================================================="))

            if not os.path.exists(local_path):
                self.log_queue.put(("log", f"❌ Error: Folder lokal '{local_path}' tidak ditemukan!"))
                self.log_queue.put(("status_lbl", (folder_id, "❌ Not Found", "#f38ba8")))
                continue

            cmd = ["rclone", "copy", local_path, remote_dest, "-P", "--stats", "1s"]
            
            try:
                self.current_process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    universal_newlines=True,
                    creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
                )
                
                # Regex patterns for parsing rclone -P stats
                # Example: Transferred:   12.345 MiB / 100.00 MiB, 12%, 2.50 MiB/s, ETA 35s
                pct_pattern = re.compile(r'(\d+)%')
                stats_pattern = re.compile(r'Transferred:.*?(ETA \S+|\d+s|\d+m|\d+h)', re.IGNORECASE)

                for line in self.current_process.stdout:
                    clean_line = line.strip()
                    if clean_line:
                        self.log_queue.put(("log", clean_line))
                        
                        # Parse progress stats
                        if "Transferred:" in clean_line:
                            pct_match = pct_pattern.search(clean_line)
                            current_item_pct = int(pct_match.group(1)) if pct_match else 0
                            
                            # Calculate overall progress
                            overall_progress = (idx * 100) + current_item_pct
                            self.log_queue.put(("progress", overall_progress))
                            self.log_queue.put(("speed", clean_line))

                self.current_process.wait()
                exit_code = self.current_process.returncode

                if exit_code == 0:
                    self.log_queue.put(("status_lbl", (folder_id, "✔ Completed", "#a6e3a1")))
                    self.log_queue.put(("log", f"✅ Berhasil upload: {folder_name}"))
                else:
                    self.log_queue.put(("status_lbl", (folder_id, f"❌ Failed ({exit_code})", "#f38ba8")))
                    self.log_queue.put(("log", f"❌ Upload gagal dengan kode keluar {exit_code}."))

            except Exception as e:
                self.log_queue.put(("status_lbl", (folder_id, "❌ Error", "#f38ba8")))
                self.log_queue.put(("log", f"❌ Terjadi kesalahan: {str(e)}"))

        self.is_running = False
        self.log_queue.put(("done", None))

    def process_log_queue(self):
        try:
            while True:
                msg_type, data = self.log_queue.get_nowait()
                if msg_type == "log":
                    self.log(data)
                elif msg_type == "status_lbl":
                    folder_id, text, color = data
                    self.folder_status_labels[folder_id].config(text=text, fg=color)
                elif msg_type == "overall_status":
                    self.lbl_progress_status.config(text=f"Status: {data}", fg="#89b4fa")
                elif msg_type == "progress":
                    self.progress_bar["value"] = data
                elif msg_type == "speed":
                    self.lbl_speed_info.config(text=data)
                elif msg_type == "done":
                    self.progress_bar["value"] = len(UPLOAD_TARGETS) * 100
                    self.lbl_progress_status.config(text="Status: Semua upload selesai!", fg="#a6e3a1")
                    self.btn_run.config(state=tk.NORMAL, bg="#a6e3a1")
                    self.btn_stop.config(state=tk.DISABLED)
                    messagebox.showinfo("Selesai", "Batch upload ke-4 folder telah selesai diproses!")
        except queue.Empty:
            pass
        finally:
            self.after(100, self.process_log_queue)

def main():
    base_dir = r"c:\Users\Nasrul Wahabi\Downloads\Music\UPLOAD"
    if not os.path.exists(base_dir):
        base_dir = os.path.abspath(os.path.dirname(__file__))
    app = MusicUploaderApp(base_dir)
    app.mainloop()

if __name__ == "__main__":
    main()
