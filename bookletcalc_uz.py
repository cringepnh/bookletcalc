"""
BookletCalc - Kitobcha (booklet) uchun sahifalarni hisoblash dasturi
Двусторонняя печать буклетом на A4 (2 страницы на лист)

Bu dastur printerda qo'lda ikki tomonlama chop etish uchun
sahifalar tartibini hisoblaydi.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
import os
import sys


def hisoblash_sahifalar(jami_sahifalar: int) -> tuple[str, str]:
    """
    Kitobcha uchun sahifalar tartibini hisoblash.
    
    Booklet formatida har bir varaq 4 ta sahifa o'rnini egallaydi:
    - Oldi: 2 ta sahifa
    - Orqasi: 2 ta sahifa
    
    Args:
        jami_sahifalar: Hujjatdagi sahifalar soni
        
    Returns:
        tuple: (birinchi_bosma, ikkinchi_bosma) - vergul bilan ajratilgan sahifa raqamlari
    """
    # Varaqlar soni - 4 ga bo'lib, yuqoriga yaxlitlaymiz
    varaqlar_soni = math.ceil(jami_sahifalar / 4)
    
    # Jami pozitsiyalar soni (bo'sh sahifalarni hisobga olgan holda)
    jami_pozitsiyalar = varaqlar_soni * 4
    
    # Birinchi bosma (varaqlarning oldi tomoni)
    birinchi_bosma = []
    
    # Ikkinchi bosma (varaqlarning orqa tomoni)
    ikkinchi_bosma = []
    
    for varaq in range(varaqlar_soni):
        # Har bir varaq uchun sahifa raqamlarini hisoblaymiz
        
        # Oldi tomoni: [oxirgi - 2*varaq, 1 + 2*varaq]
        # Masalan, 8 sahifa: varaq 0 -> [8, 1], varaq 1 -> [6, 3]
        oldi_chap = jami_pozitsiyalar - (2 * varaq)
        oldi_ong = 1 + (2 * varaq)
        
        birinchi_bosma.append(oldi_chap)
        birinchi_bosma.append(oldi_ong)
        
        # Orqa tomoni: [2 + 2*varaq, oxirgi - 1 - 2*varaq]
        # Masalan, 8 sahifa: varaq 0 -> [2, 7], varaq 1 -> [4, 5]
        orqa_chap = 2 + (2 * varaq)
        orqa_ong = jami_pozitsiyalar - 1 - (2 * varaq)
        
        ikkinchi_bosma.append(orqa_chap)
        ikkinchi_bosma.append(orqa_ong)
    
    # Sahifa raqamlarini formatlash (faqat mavjud sahifalarni ko'rsatish)
    def formatlash(sahifalar: list[int]) -> str:
        """Sahifa raqamlarini vergul bilan ajratib formatlash, faqat haqiqiy sahifalar"""
        # Faqat mavjud sahifalarni olamiz (jami_sahifalar dan katta bo'lmaganlarni)
        mavjud = [s for s in sahifalar if s <= jami_sahifalar]
        return ",".join(str(s) for s in mavjud)
    
    return formatlash(birinchi_bosma), formatlash(ikkinchi_bosma)


def hisoblash_tugmasi_bosildi():
    """Hisoblash tugmasi bosilganda ishlovchi funksiya"""
    kiritilgan = kiritish_maydoni.get().strip()
    
    # Tekshirish: bo'sh yoki noto'g'ri qiymat
    if not kiritilgan:
        messagebox.showerror("Xato", "Iltimos, sahifalar sonini kiriting!")
        return
    
    try:
        jami = int(kiritilgan)
    except ValueError:
        messagebox.showerror("Xato", "Iltimos, faqat butun son kiriting!")
        return
    
    if jami < 1:
        messagebox.showerror("Xato", "Sahifalar soni 1 dan kam bo'lmasligi kerak!")
        return
    
    if jami > 10000:
        messagebox.showerror("Xato", "Sahifalar soni juda katta (maksimum 10000)!")
        return
    
    # Hisoblash
    birinchi, ikkinchi = hisoblash_sahifalar(jami)
    
    # Natijalarni ko'rsatish
    birinchi_bosma_matn.config(state="normal")
    birinchi_bosma_matn.delete("1.0", tk.END)
    birinchi_bosma_matn.insert("1.0", birinchi)
    birinchi_bosma_matn.config(state="normal")  # O'qish va nusxalash uchun
    
    ikkinchi_bosma_matn.config(state="normal")
    ikkinchi_bosma_matn.delete("1.0", tk.END)
    ikkinchi_bosma_matn.insert("1.0", ikkinchi)
    ikkinchi_bosma_matn.config(state="normal")
    
    # Ma'lumot
    varaqlar = math.ceil(jami / 4)
    jami_pozitsiyalar = varaqlar * 4
    bosh_sahifalar = jami_pozitsiyalar - jami
    
    if bosh_sahifalar > 0:
        malumot_yorliq.config(text=f"Jami: {jami} sahifa, {varaqlar} varaq. ({bosh_sahifalar} ta bo'sh sahifa bo'ladi)")
    else:
        malumot_yorliq.config(text=f"Jami: {jami} sahifa, {varaqlar} varaq kerak")


def nusxalash_birinchi():
    """Birinchi bosma natijasini clipboard'ga nusxalash"""
    matn = birinchi_bosma_matn.get("1.0", tk.END).strip()
    if matn:
        oyna.clipboard_clear()
        oyna.clipboard_append(matn)
        messagebox.showinfo("Tayyor", "1-chi bosma nusxalandi!")


def nusxalash_ikkinchi():
    """Ikkinchi bosma natijasini clipboard'ga nusxalash"""
    matn = ikkinchi_bosma_matn.get("1.0", tk.END).strip()
    if matn:
        oyna.clipboard_clear()
        oyna.clipboard_append(matn)
        messagebox.showinfo("Tayyor", "2-chi bosma nusxalandi!")


# === ASOSIY OYNA ===
oyna = tk.Tk()
oyna.title("BookletCalc - Kitobcha uchun sahifalar tartibi")
oyna.geometry("500x400")
oyna.resizable(True, True)

# Minimal o'lcham
oyna.minsize(400, 350)

# Ikonka o'rnatish
def resurs_yoli(nisbiy_yol):
    """PyInstaller bilan ishlash uchun resurs yo'lini aniqlash"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, nisbiy_yol)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), nisbiy_yol)

try:
    oyna.iconbitmap(resurs_yoli('icon.ico'))
except:
    pass  # Ikonka topilmasa, standart ikonka ishlatiladi

# === KIRISH QISMI ===
kirish_freym = ttk.Frame(oyna, padding="10")
kirish_freym.pack(fill="x")

ttk.Label(kirish_freym, text="Sahifalar soni:", font=("Arial", 11)).pack(side="left")

kiritish_maydoni = ttk.Entry(kirish_freym, width=15, font=("Arial", 11))
kiritish_maydoni.pack(side="left", padx=10)

# Enter tugmasi bilan ham ishlash
kiritish_maydoni.bind("<Return>", lambda e: hisoblash_tugmasi_bosildi())

hisoblash_tugma = ttk.Button(kirish_freym, text="Hisoblash", command=hisoblash_tugmasi_bosildi)
hisoblash_tugma.pack(side="left")

# === MA'LUMOT YORLIG'I ===
malumot_yorliq = ttk.Label(oyna, text="", font=("Arial", 10), foreground="gray")
malumot_yorliq.pack(pady=5)

# === NATIJALAR QISMI ===

# Birinchi bosma
birinchi_freym = ttk.LabelFrame(oyna, text="1-chi bosma (oldi tomoni)", padding="10")
birinchi_freym.pack(fill="both", expand=True, padx=10, pady=5)

birinchi_bosma_matn = tk.Text(birinchi_freym, height=3, font=("Consolas", 10), wrap="word")
birinchi_bosma_matn.pack(fill="both", expand=True, side="left")

birinchi_scroll = ttk.Scrollbar(birinchi_freym, orient="vertical", command=birinchi_bosma_matn.yview)
birinchi_scroll.pack(side="right", fill="y")
birinchi_bosma_matn.config(yscrollcommand=birinchi_scroll.set)

birinchi_nusxa_tugma = ttk.Button(oyna, text="1-chi bosmani nusxalash", command=nusxalash_birinchi)
birinchi_nusxa_tugma.pack(pady=2)

# Ikkinchi bosma
ikkinchi_freym = ttk.LabelFrame(oyna, text="2-chi bosma (orqa tomoni)", padding="10")
ikkinchi_freym.pack(fill="both", expand=True, padx=10, pady=5)

ikkinchi_bosma_matn = tk.Text(ikkinchi_freym, height=3, font=("Consolas", 10), wrap="word")
ikkinchi_bosma_matn.pack(fill="both", expand=True, side="left")

ikkinchi_scroll = ttk.Scrollbar(ikkinchi_freym, orient="vertical", command=ikkinchi_bosma_matn.yview)
ikkinchi_scroll.pack(side="right", fill="y")
ikkinchi_bosma_matn.config(yscrollcommand=ikkinchi_scroll.set)

ikkinchi_nusxa_tugma = ttk.Button(oyna, text="2-chi bosmani nusxalash", command=nusxalash_ikkinchi)
ikkinchi_nusxa_tugma.pack(pady=2)

# === YO'RIQNOMA ===
yoriqnoma = ttk.Label(oyna, text="1. Sahifalar sonini kiriting\n2. 'Hisoblash' tugmasini bosing\n3. Natijani nusxalab, chop etish oynasiga joylashtiring", 
                       font=("Arial", 9), foreground="gray", justify="center")
yoriqnoma.pack(pady=10)

# === DASTURNI ISHGA TUSHIRISH ===
if __name__ == "__main__":
    oyna.mainloop()
