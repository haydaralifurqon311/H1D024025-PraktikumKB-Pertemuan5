import tkinter as tk
from tkinter import messagebox

GEJALA = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Airliur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Beratbadan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bolamata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh dimulut",
    "G29": "Benjolan dileher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Letih lesu",
    "G37": "Demam"
}

PENYAKIT = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nafasoring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"]
}

class AplikasiDiagnosaTHT:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Penyakit THT")
        self.root.geometry("800x600")
        
        # Title Label
        title_label = tk.Label(root, text="Sistem Pakar Diagnosa Penyakit THT", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)
        
        instruction_label = tk.Label(root, text="Centang gejala yang Anda alami di bawah ini:", font=("Helvetica", 12))
        instruction_label.pack(pady=5)
        
        # Frame for checkboxes using a Canvas and Scrollbar to allow scrolling
        frame_container = tk.Frame(root)
        frame_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.canvas = tk.Canvas(frame_container)
        scrollbar = tk.Scrollbar(frame_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Mouse wheel scrolling
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        self.checkbox_vars = {}
        row, col = 0, 0
        for kode, gejala in GEJALA.items():
            var = tk.IntVar()
            chk = tk.Checkbutton(self.scrollable_frame, text=f"{kode} - {gejala}", variable=var, font=("Helvetica", 10), justify="left")
            chk.grid(row=row, column=col, sticky="w", padx=10, pady=5)
            self.checkbox_vars[kode] = var
            col += 1
            if col > 1:  # Display in 2 columns
                col = 0
                row += 1
                
        # Diagnosis Button
        btn_diagnosa = tk.Button(root, text="Diagnosa Penyakit", command=self.diagnosa, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10)
        btn_diagnosa.pack(pady=20)
        
    def diagnosa(self):
        gejala_terpilih = [kode for kode, var in self.checkbox_vars.items() if var.get() == 1]
        
        if not gejala_terpilih:
            messagebox.showwarning("Peringatan", "Silakan pilih minimal 1 gejala yang dialami.")
            return
        
        hasil = []
        for penyakit, gejala_penyakit in PENYAKIT.items():
            cocok = set(gejala_terpilih).intersection(set(gejala_penyakit))
            if len(cocok) > 0:
                persentase = (len(cocok) / len(gejala_penyakit)) * 100
                hasil.append((penyakit, persentase, len(cocok), len(gejala_penyakit), cocok))
                
        hasil.sort(key=lambda x: x[1], reverse=True)
        
        if not hasil:
            messagebox.showinfo("Hasil Diagnosa", "Tidak ditemukan penyakit yang cocok dengan gejala Anda.")
        else:
            pesan = f"Gejala yang dipilih: {', '.join(gejala_terpilih)}\n\nKemungkinan Penyakit:\n"
            for penyakit, persentase, jumlah_cocok, total_gejala, cocok in hasil:
                if persentase > 0:
                    pesan += f"- {penyakit}: {persentase:.0f}% ({jumlah_cocok}/{total_gejala} gejala cocok)\n"
            
            # Create a custom dialog for better formatting if it's too long
            self.tampilkan_hasil_window(pesan)

    def tampilkan_hasil_window(self, pesan):
        top = tk.Toplevel(self.root)
        top.title("Hasil Diagnosa")
        top.geometry("500x400")
        
        lbl = tk.Label(top, text="Hasil Diagnosa Sistem Pakar", font=("Helvetica", 14, "bold"))
        lbl.pack(pady=10)
        
        text_area = tk.Text(top, wrap=tk.WORD, font=("Helvetica", 11))
        text_area.insert(tk.INSERT, pesan)
        text_area.configure(state='disabled')
        text_area.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        btn_close = tk.Button(top, text="Tutup", command=top.destroy, font=("Helvetica", 10), bg="#f44336", fg="white")
        btn_close.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiDiagnosaTHT(root)
    root.mainloop()
