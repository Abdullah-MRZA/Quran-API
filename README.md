# Quran-API
A program that provides easy access to the Quran (and its translation).

## How to use
The following example (also found in `main_program.py`) gives an overview of how it can be used:

```py
import load_quran

# for colours, import rich (using `pip install rich`), and uncomment the following line
# from rich import print

quran_data = load_quran.load_quran("quran.json")

# Now you can do something with this data
print(quran_data[0].surah_name_arabic)
print(quran_data[0].surah_name_english)
print(quran_data[0].revelation_location)
print(quran_data[0].total_verses_number)

fatiha_verses = quran_data[0].ayahs
print(fatiha_verses[0].arabic_text)
print(fatiha_verses[0].translation)

# print the arabic of surah fatiha
for verse_number in range(quran_data[0].total_verses_number):
    print(quran_data[0].ayahs[verse_number])
```
