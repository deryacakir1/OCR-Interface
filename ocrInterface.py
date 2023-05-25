from tkinter import *
from PIL import Image, ImageTk
import pytesseract
from tkinter import filedialog
import tkinter.scrolledtext as tkst

class OCRApp:

    def __init__(self, master):
        self.master = master
        master.title("OCR Uygulaması")
        master.configure(bg='#ECECEC')
        master.geometry("850x600")


        #Arayüz Başlığı
        self.title_label = Label(master, text="OCR INTERFACE", font=("Tahoma", 28), bg="#ECECEC")
        self.title_label.pack(pady=20)

        # Resim seçme butonu
        self.select_image_button = Button(master, text="Select Image", command=self.select_image, bg='#B4B4B4', fg='#FFFFFF', font=("Tahoma", 10))
        self.select_image_button.pack(pady=10)

        # Resim ve OCR sonucu gösterme alanı
        self.image_text_frame = Frame(master)
        self.image_text_frame.pack(pady=10)

        self.image_label = Label(self.image_text_frame)
        self.image_label.pack(side=LEFT, padx=10)

        self.text_label = tkst.ScrolledText(self.image_text_frame, wrap=WORD, width=70, height=20, font=("Tahoma", 10), state=DISABLED)
        self.text_label.pack(side=LEFT, padx=10)

        # Çıkış butonu
        self.quit_button = Button(master, text="Exit", command=master.quit, bg='#FF0000', fg='#FFFFFF', font=("Tahoma", 10,"bold"))
        self.quit_button.pack(pady=10)


    def select_image(self):
        # Resim seçme işlemi
        file_path = filedialog.askopenfilename()
        if file_path:
            # Resmi gösterme işlemi
            image = Image.open(file_path)
            image = image.resize((800, 800))
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo

            # OCR işlemi
            text = pytesseract.image_to_string(image, lang='tur+eng', config='--psm 6')
            text = text.lower()
            self.text_label.delete("1.0", END)
            self.text_label.insert(END, text)

            # Metin kutusuna yazma işlemi
            self.text_label.config(state=NORMAL)
            self.text_label.delete("1.0", END)
            self.text_label.insert(END, text)
            self.text_label.config(state=DISABLED)


root = Tk()
app = OCRApp(root)
root.mainloop()

