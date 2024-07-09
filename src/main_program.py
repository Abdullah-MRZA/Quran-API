from rich import print
import load_quran
# from PIL import Image, ImageDraw, ImageFont, ImageFilter


def main() -> None:
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


if __name__ == "__main__":
    main()
