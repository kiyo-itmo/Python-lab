import csv


# Dem ten sach dai hon 30 ky tu
def count_titles(books):
    count = 0

    for row in books:
        if len(row[1]) > 30:
            count += 1

    print("Книг с названием длиннее 30 символов:", count)

# Tim sach theo tac gia, gia khong qua 200
def search_by_author(books):
    search = input("Введите автора: ").strip().lower()

    if not search:
        print("Вы не ввели имя автора")
        return

    count = 0

    for row in books:
        title = row[1]
        author = row[2]

        try:
            price = float(row[6].replace(",", "."))
        except ValueError:
            continue

        if search in author.lower() and price <= 200:
            count += 1
            print(f"{count}. {author}. {title} - {price:g} ")

    if count == 0:
        print("Поиск не дал результатов")
    else:
        print("Найдено книг:", count)

#4 Tao 20 tai lieu tham khao
def write_references(books):
    count = 0

    with open("references.txt", "w", encoding="utf-8") as output:
        for row in books:
            title = row[1]
            author = row[2]
            year = row[3].strip()

            if not (year.isdigit() and len(year) == 4):
                continue

            count += 1

            output.write(
                f"{count}. {author}. {title} - {year}\n"
            )

            if count == 20:
                break

    print(f"Записано ссылок: {count} (файл {"references.txt"})")

    if count != 20:
        print("Предупреждение: найдено менее 20 корректных записей")
if __name__ == "__main__":
    with open('books-en.csv', encoding='cp1251') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)  # Пропускаем заголовок
        books = list(reader)
    #task1
    count_titles(books)
    #task2
    search_by_author(books)
    #task3
    write_references(books)

    

        
