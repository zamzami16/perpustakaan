import tkinter as tk
from tkinter import ttk, messagebox
from dataModel import dataModel


class _loginWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.login_trial = 0

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        self.label_login = tk.Label(
            self, text="Login", font=(("Arial", "Bold"), 14)
        )
        self.label_login.pack(padx=5, pady=5, fill="x", side="top", expand=1)
        self.label_login.pack_configure(expand=1)
        # self.label_login.grid_rowconfigure(0, weight=1)
        # self.label_login.grid_columnconfigure(0, weight=1)

        self.login_entry_frame = tk.Frame(self)
        elabel1 = tk.Label(self.login_entry_frame, text="User Name")
        elabel2 = tk.Label(self.login_entry_frame, text="Password")
        elabel1.grid(row=0, column=0, sticky=tk.W)
        elabel2.grid(row=1, column=0, sticky=tk.W)
        self.login_entry = []
        for i in range(2):
            elabel = tk.Label(self.login_entry_frame, text=":")
            if i == 1:
                entry = tk.Entry(
                    self.login_entry_frame, show="*", justify="left", width=25
                )
            else:
                entry = tk.Entry(
                    self.login_entry_frame, justify="left", width=25
                )
            elabel.grid(row=i, column=1)
            entry.grid(row=i, column=2)
            self.login_entry.append(entry)
        login_button = tk.Button(
            self.login_entry_frame,
            width=20,
            text="Login",
            font=("Arial", 9),
            command=self.login,
        )
        login_button.grid(row=2, column=2, padx=5, pady=5, sticky=tk.NSEW)

        self.login_entry_frame.pack(
            padx=5, pady=5, fill="x", side="bottom", expand=1
        )
        # self.login_entry_frame.grid_columnconfigure(2, weight=3)

    def login(self):
        """Login for petugas"""
        # print(self._get_form_entry(self.login_entry))
        # self.master._set_full_screen()
        if self.login_trial < 3:
            username, password = self._get_form_entry(self.login_entry)
            if (username == "zami") & (password == "zami123"):
                self.login_trial += 3
                self.master.whoiam = username
                self.master.login_frame.pack_forget()
                self.master._set_full_screen()
            else:
                self.login_trial += 1
                msg = f"Masukkan Username dan password dengan benar! \nPercobaan login ke-{self.login_trial} dari 3."
                messagebox.showerror("Login gagal", msg)
                if self.login_trial > 2:
                    self.master.destroy()
        else:
            self.master.destroy()

    def _get_form_entry(self, form_entry):
        value = []
        for entry in form_entry:
            value.append(entry.get())
        return value


class mainWindow(tk.Frame):
    """
    Add main window widged
    contain:
        - Tambah Rak Buku
        - Tambah Buku baru
        - Tambah Anggota
        - Peminjaman
        - Pengembalian

    """

    def __init__(self, parent):
        super().__init__(parent)

        title_label = tk.Label(
            self, text="Main Window", font=(("Arial", "Bold"), 14)
        )
        title_label.pack(pady=3)
        greetings = (
            f"Selamat datang di Management Perpustakaan {self.master.whoiam}!"
        )
        greetings_label = tk.Label(self, text=greetings, justify="center")
        greetings_label.pack()

        self.main_button_menu = tk.Frame(self)
        butt_add_rak_buku = tk.Button(
            self.main_button_menu,
            text="Tambah Rak Buku",
            width=25,
            command=self.launch_rak_buku_frame,
        )

        butt_add_buku_baru = tk.Button(
            self.main_button_menu,
            text="Tambah Buku Baru",
            width=25,
            command=self.launch_add_buku_frame,
        )

        butt_add_anggota_baru = tk.Button(
            self.main_button_menu, text="Tambah Anggota Baru", width=25
        )

        butt_add_peminjaman = tk.Button(
            self.main_button_menu, text="Peminjaman", width=25
        )

        butt_add_pengembalian = tk.Button(
            self.main_button_menu, text="Pengembalian", width=25
        )

        butt_add_rak_buku.pack(pady=3)
        butt_add_buku_baru.pack(pady=3)
        butt_add_anggota_baru.pack(pady=3)
        butt_add_peminjaman.pack(pady=3)
        butt_add_pengembalian.pack(pady=3)

        self.main_button_menu.pack(pady=3)

    def launch_rak_buku_frame(self):
        window = add_rak_buku_frame(self)
        window.grab_set()

    def launch_add_buku_frame(self):
        window = add_buku_frame(self)
        window.grab_set()


class add_rak_buku_frame(tk.Toplevel):
    """Add rak buku view"""

    def __init__(self, parent):
        super().__init__(parent)

        self.resizable(0, 0)
        self.title("Rak Buku")
        width = int(self.winfo_screenwidth() / 4)
        height = int(self.winfo_screenheight() / 4)
        self.geometry("%dx%d+%d+%d" % (width - 50, height, 500, 320))

        title = tk.Label(
            self, text="Input Rak Buku", font=(("Arial", "Bold"), 14)
        )
        title.pack(pady=3)

        self.bbox_frame = tk.Frame(self)
        # data.add_rak_buku('B612', 'block B')
        elabel1 = tk.Label(self.bbox_frame, text="Kode Rak")
        elabel2 = tk.Label(self.bbox_frame, text="Lokasi Rak")
        elabel1.grid(row=0, column=0, sticky=tk.W)
        elabel2.grid(row=1, column=0, sticky=tk.W)

        self.add_rak_buku_entry = []
        for i in range(2):
            elabel = tk.Label(self.bbox_frame, text=":")

            entry = tk.Entry(
                self.bbox_frame, justify="left", width=25
            )

            elabel.grid(row=i, column=1, padx=3, pady=3)
            entry.grid(row=i, column=2, padx=3, pady=3)

            self.add_rak_buku_entry.append(entry)

        self.bbox_frame.pack(pady=8)

        self.butt_frame = tk.Frame(self)
        butt = tk.Button(self.butt_frame, text="Add Rak", width=15, command=self.add_rak)
        butt.pack(pady=5, padx=5, side='right')
        butt = tk.Button(self.butt_frame, text="Quit", width=15, command=self.destroy)
        butt.pack(pady=5, padx=5, side='left')

        self.butt_frame.pack(pady=5)
    
    def add_rak(self):
        """Tambahkan rak ke DB"""
        kode_rak, lokasi_rak = self.master.master._get_form_entry(self.add_rak_buku_entry)
        # print(val)
        if (kode_rak != '') & (lokasi_rak != ''):
            print("sip")

            resp = self.master.master.database.add_rak_buku(kode_rak, lokasi_rak)
            if resp:
                messagebox.showinfo('berhasil', "Rak berhasil ditambahkan!")
                self.master.master._clear_form_entry(self.add_rak_buku_entry)
            else:
                messagebox.showinfo("gagal", "Data gagal ditambahkan!")
        else:
            messagebox.showerror("Masukkan Kode Rak", "Masukkan Data dengan benar.")


class add_buku_frame(tk.Toplevel):
    """Add Buku Frame"""
    # data.add_buku('fisdas1', 'Fisika dasar 1', 'Tipler Paul A.', 'Mc Grill', 2006, 5, 'B612')
    def __init__(self, parent):
        super().__init__(parent)

        self.resizable(0, 0)
        self.title("Add Buku")
        width = int(self.winfo_screenwidth() / 4)
        height = int(self.winfo_screenheight() / 4)
        self.geometry("%dx%d+%d+%d" % (width - 50, height+75, 500, 400))

        title = tk.Label(
            self, text="Input Data Buku", font=(("Arial", "Bold"), 14)
        )
        title.pack(pady=3)

        self.bbox_frame = tk.Frame(self)
        label_ = ('Kode Buku', 'Judul Buku', 'Pengarang', 'Penerbit', 'Tahun Terbit', 'Stock', 'Kode Rak')
        self.add_buku_entry = []
        for i in range(7):
            tk.Label(self.bbox_frame, text=label_[i]).grid(row=i, column=0, sticky=tk.W)
            tk.Label(self.bbox_frame, text=':').grid(row=i, column=1, sticky=tk.W)
            entry = tk.Entry(self.bbox_frame, justify='left', width=25)
            entry.grid(row=i, column=2, padx=3, pady=3)
            self.add_buku_entry.append(entry)
        self.bbox_frame.pack()

        self.butt_frame = tk.Frame(self)
        butt = tk.Button(self.butt_frame, text="Add Data Buku", width=15, command=self.add_data_buku)
        butt.pack(pady=5, padx=5, side='right')
        butt = tk.Button(self.butt_frame, text="Quit", width=15, command=self.destroy)
        butt.pack(pady=5, padx=5, side='left')
        self.butt_frame.pack(pady=5)

    def add_data_buku(self):
        val = self.master.master._get_form_entry(self.add_buku_entry)
        print(len(val))
        if len(val) == 7:
            print("sip")

            resp = self.master.master.database.add_buku(val[0], val[1], val[2], val[3], val[4], int(val[5]), val[6])
            if resp:
                messagebox.showinfo('berhasil', "Data Buku berhasil ditambahkan!")
                self.master.master._clear_form_entry(self.add_buku_entry)
            else:
                messagebox.showinfo("gagal", "Data gagal ditambahkan!")
        else:
            messagebox.showerror("Masukkan Entry", "Masukkan Data dengan benar.")



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login")
        # self.attributes('-fullscreen', True)
        self.database = dataModel()
        self.whoiam = None
        self.geometry("250x130")
        self.resizable(0, 0)
        self.login_frame = _loginWindow(self)
        self.login_frame.pack(fill="y")
        self.login_frame.pack_configure(fill="y")

    def _set_full_screen(self):
        self.resizable(0, 0)
        self.title("Management Perpustakaan")
        width = self.winfo_screenwidth() / 4
        height = self.winfo_screenheight() / 4
        self.geometry("%dx%d" % (width - 50, height + 30))
        # print(self.whoiam)
        self.main_window_frame = mainWindow(self)
        self.main_window_frame.pack(fill="both")
    
    def _get_form_entry(self, form_entry):
        """Get data from form entry"""
        value = []
        for entry in form_entry:
            value.append(entry.get())
        return value
    
    def _clear_form_entry(self, form_entry):
        """Clear all value in form entry"""
        for entry in form_entry:
            entry.delete(0, 'end')


if __name__ == "__main__":
    app = App()
    app.eval("tk::PlaceWindow . center")
    app.mainloop()
