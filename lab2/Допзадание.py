import csv

#  Nha xuat ban khong trung lap
def unique_publishers(books):
    publishers = set()

    for row in books:
        publishers.add(row[4])

    print("Количество издательств:", len(publishers))

    for name in sorted(publishers):
        print(name)


# Top 20 sach pho bien nhat
def top_20_books(books):
    book_list = []

    for row in books:
        try:
            downloads = int(row[5])
        except ValueError:
            continue

        book_list.append([row[1], row[2], downloads])

    top_20 = sorted(
        book_list,
        key=lambda book: book[2],
        reverse=True
    )[:20]

    print("Самые популярные книги (по количеству скачиваний):")

    for number, book in enumerate(top_20, start=1):
        print(
            f"{number}. {book[0]} - {book[1]} - "
            f"{book[2]} скачиваний"
        )

    print("Количество книг:", len(top_20))
if __name__ == "__main__":
    with open('books-en.csv', encoding='cp1251') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)  # Пропускаем заголовок
        books = list(reader)

    unique_publishers(books)
    #top_20_books(books)