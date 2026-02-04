# BookletCalc 📖

**Booklet Page Calculator** — A simple utility for manual duplex booklet printing.

<p align="center">
  <a href="#english">English</a> •
  <a href="#русский">Русский</a> •
  <a href="#ozbek">O'zbek</a>
</p>

---

## 🌟 About

I created this simple program to help my mom print booklets on her printer that doesn't support automatic duplex printing. She's not very tech-savvy, and constantly calculating page orders for booklet printing was frustrating for her.

**BookletCalc** solves this problem by automatically calculating the correct page order for:
- **First pass** (front side of all sheets)
- **Second pass** (back side after flipping the paper)

The program is available in **three languages** to help users worldwide:
- 🇺🇿 Uzbek (O'zbek)
- 🇷🇺 Russian (Русский)  
- 🇬🇧 English

---

## 📥 Download

### Ready-to-use executables (no Python required):

| Language | Download |
|----------|----------|
| 🇺🇿 O'zbek | [BookletCalc_UZ.exe](https://github.com/cringepnh/bookletcalc/releases/download/v1.0.0/BookletCalc_UZ.exe) |
| 🇷🇺 Русский | [BookletCalc_RU.exe](https://github.com/cringepnh/bookletcalc/releases/download/v1.0.0/BookletCalc_RU.exe) |
| 🇬🇧 English | [BookletCalc_EN.exe](https://github.com/cringepnh/bookletcalc/releases/download/v1.0.0/BookletCalc_EN.exe) |

Just download and run — no installation needed!

---

## 🖨️ How to Use

1. **Open your document** (PDF, Word, etc.) and note the total number of pages
2. **Run BookletCalc** and enter the number of pages
3. **Click "Calculate"** (Hisoblash / Рассчитать)
4. **Copy the first pass** numbers to your print dialog
5. **Print the first pass** (front sides)
6. **Flip the printed pages** and put them back in the printer tray
7. **Copy the second pass** numbers and print again

### Print Settings
Make sure to set in your print dialog:
- **Pages per sheet: 2**
- **Orientation: Landscape** (usually automatic)

---

## 🛠️ Building from Source

### Requirements
- Python 3.10+
- tkinter (included with Python on Windows)

### Run directly:
```bash
python bookletcalc_uz.py   # Uzbek
python bookletcalc_ru.py   # Russian
python bookletcalc_en.py   # English
```

### Build executables:
```bash
pip install pyinstaller

python -m PyInstaller --onefile --windowed --icon=icon.ico --add-data "icon.ico;." --name BookletCalc_UZ bookletcalc_uz.py
python -m PyInstaller --onefile --windowed --icon=icon.ico --add-data "icon.ico;." --name BookletCalc_RU bookletcalc_ru.py
python -m PyInstaller --onefile --windowed --icon=icon.ico --add-data "icon.ico;." --name BookletCalc_EN bookletcalc_en.py
```

The executables will be in the `dist/` folder.

---

## 📐 How Booklet Printing Works

When printing a booklet on A4 paper with 2 pages per sheet:
- Each physical sheet holds **4 page positions** (2 front + 2 back)
- Pages must be arranged so they read in order when folded
- If your document has 18 pages, you need 5 sheets (20 positions, 2 blank)

**Example for 8 pages:**
```
1st Pass (front): 8,1,6,3
2nd Pass (back):  2,7,4,5
```

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 💝 Acknowledgments

Made with love for my mom and everyone who struggles with manual duplex printing!

---

<h2 id="english">🇬🇧 English</h2>

BookletCalc is a simple page calculator for booklet printing. Enter your total pages, and it will tell you which pages to print in each pass for manual duplex printing.

<h2 id="русский">🇷🇺 Русский</h2>

BookletCalc — простой калькулятор страниц для печати буклетом. Введите общее количество страниц, и программа покажет порядок печати для ручной двусторонней печати.

<h2 id="ozbek">🇺🇿 O'zbek</h2>

BookletCalc — kitobcha chop etish uchun sahifalar hisoblagichi. Sahifalar sonini kiriting va dastur qo'lda ikki tomonlama chop etish uchun tartibni ko'rsatadi.
