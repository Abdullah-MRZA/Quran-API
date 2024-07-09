import json
from dataclasses import dataclass

# import arabic_reshaper
# from bidi.algorithm import get_display


"""
(Example output)
In [3]: with open("quran_en.json") as f:
   ...:     import json
   ...:     a = f.read()
   ...:     b = json.loads(a)
   ...:     b = json.dumps(b, indent=4)
   ...:     print(b[:1000])
   ...: 
[
    {
        "id": 1,
        "name": "\u0627\u0644\u0641\u0627\u062a\u062d\u0629",
        "transliteration": "Al-Fatihah",
        "translation": "The Opener",
        "type": "meccan",
        "total_verses": 7,
        "verses": [
            {
                "id": 1,
                "text": "\u0628\u0650\u0633\u06e1\u0645\u0650 \u0671\u0644\u0644\u0651\u064e\u0647\u0650 \u0671\u0644\u0631\u0651\u064e\u062d\u06e1\u0645\u064e\u0670\u0646\u0650 \u0671\u0644\u0631\u0651\u064e\u062d\u0650\u064a\u0645\u0650",
                "translation": "In the name of Allah, the Entirely Merciful, the Especially Merciful"
            },
            {
                "id": 2,
                "text": "\u0671\u0644\u06e1\u062d\u064e\u0645\u06e1\u062f\u064f \u0644\u0650\u0644\u0651\u064e\u0647\u0650 \u0631\u064e\u0628\u0651\u0650 \u0671\u0644\u06e1\u0639\u064e\u0670\u0644\u064e\u0645\u0650\u064a\u0646\u064e",
                "translation": "[All] praise is [due] to Allah, Lord of the worlds"
"""


@dataclass()
class ayah_data:
    arabic_text: str
    translation: str


@dataclass
class surah_data:
    surah_name_english: str
    surah_name_arabic: str
    revelation_location: str
    total_verses_number: int
    ayahs: list[ayah_data]


def load_quran(filename: str) -> list[surah_data]:
    quran_data: list[surah_data] = []

    with open("quran.json", encoding="utf-8") as f:
        quran = json.loads(f.read())
        for surah in quran:
            quran_data.append(
                surah_data(
                    surah["transliteration"],
                    surah["name"],
                    surah["type"],
                    surah["total_verses"],
                    [
                        ayah_data(ayah["text"], ayah["translation"])
                        for ayah in surah["verses"]
                    ],
                )
            )

    # print(quran_data)

    return quran_data
