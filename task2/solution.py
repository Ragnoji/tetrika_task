from bs4 import BeautifulSoup
import requests
import csv
from time import sleep

def get_letter_counts():
    counts = {chr(i): 0 for i in range(ord('А'), ord('Я'))}
    url = 'https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom=А#mw-pages'

    while True:
        sleep(0.1)
        page = requests.get(url)
        while page.status_code != 200:
            sleep(1)
            page = requests.get(url)

        soup = BeautifulSoup(page.text, 'html.parser')
        categories = soup.find_all('div', id='mw-pages')[0]
        lettered_categories = categories.find_all('div', class_='mw-category-group')
        for letter_category in lettered_categories:
            letter = letter_category.find('h3').get_text().upper()
            if letter not in counts.keys():
                return counts
            counts[letter] += len(letter_category.find_all('li'))
        url = 'https://ru.wikipedia.org' + categories.find('a', string='Следующая страница').get('href')


def write_counts(counts):
    with open('beasts.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(counts.items())


def parse_wiki_categories():
    write_counts(get_letter_counts())


if __name__ == '__main__':
    parse_wiki_categories()
    expected_sum = 21074  # Получено из результата скрипта, можно детальнее сверять, но тогда весь dict придется хардкодить
    s = 0
    with open('beasts.csv', 'r') as f:
        for li in f.readlines():
            s += int(li.strip().split(',')[1])
    assert s == expected_sum, f"Expected {expected_sum} categories starting with RU Alphabet, got {s}"