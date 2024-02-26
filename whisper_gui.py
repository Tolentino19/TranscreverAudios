import os
import tkinter as tk
from tkinter import filedialog
from whisper_transcribe import transcribe_folder

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self)
        self.start_button["text"] = "Começar a transcrever"
        self.start_button["command"] = self.start_transcription
        self.start_button.pack(side="top")

        self.done_button = tk.Button(self, text="Feito", state="disabled", command=self.open_output_folder)
        self.done_button.pack(side="top")

        self.status_label = tk.Label(self, text="")
        self.status_label.pack()

        self.quit = tk.Button(self, text="FECHAR", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def start_transcription(self):
        # Disable the start button
        self.start_button.config(state="disabled")

        self.input_folder = filedialog.askdirectory(title='Selecione a pasta de origem')
        self.output_folder = filedialog.askdirectory(title='Selecione a pasta destino')

        def update_status(message):
            # Update the status label
            self.status_label.config(text=message)
            self.status_label.update_idletasks()

        transcribe_folder(self.input_folder, self.output_folder, update_status)

        # Enable the "Done" button and disable the "Start" button
        self.done_button.config(state="normal")
        self.start_button.config(state="disabled")

    def open_output_folder(self):
        # Open the output folder
        os.startfile(self.output_folder)

        # Enable the "Start" button and disable the "Done" button
        self.start_button.config(state="normal")
        self.done_button.config(state="disabled")
