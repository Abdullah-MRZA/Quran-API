from rich import print
import load_quran
# from PIL import Image, ImageDraw, ImageFont, ImageFilter


def main() -> None:
    quran_data = load_quran.load_quran("quran.json")


if __name__ == "__main__":
    main()
