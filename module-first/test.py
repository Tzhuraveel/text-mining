import csv
from typing import TextIO, List


def breakdown_text_from_file(file: TextIO, word_count: int = 150) -> List[List[str]]:
    franko_text = file.read()
    text_split = franko_text.split()
    return [text_split[i:i + word_count] for i in range(0, len(text_split), word_count)]


def convert_text_to_csv(shevchenko_franko_file, file_path: str, author: str, label: int):
    with open(file_path, 'rt', encoding='utf-8') as text_file:
        chunks = breakdown_text_from_file(text_file)
        csv_writer = csv.writer(shevchenko_franko_file)

        for chunk in chunks:
            text_row = ' '.join(chunk)
            csv_writer.writerow([text_row, label, author])


def converter():
    shevchenko_franko_file = open('shevchenko-franko.csv', 'wt', encoding='utf-8-sig', newline="")
    convert_text_to_csv(shevchenko_franko_file, 'texts/Franko.txt', 'Franko', 1)
    convert_text_to_csv(shevchenko_franko_file, 'texts/Shevchenko.txt', 'Shevchenko', 2)
    shevchenko_franko_file.close()


converter()
