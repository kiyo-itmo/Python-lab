import xml.dom.minidom as minidom

#  Xu ly XML: dictionary NumCode - CharCode
def show_currencies():
    dom = minidom.parse('currency.xml') # Функция для чтения и разбора XML-файла.

    elements = dom.getElementsByTagName("Valute") #Получить все элементы с тегом «Valute».

    currencies = {}

    for node in elements:
        num_code = node.getElementsByTagName("NumCode")[0].firstChild.data.strip()
        char_code = node.getElementsByTagName("CharCode")[0].firstChild.data.strip()

        currencies[num_code] = char_code

    print("Словарь NumCode - CharCode:", currencies)
    print("Количество валют:", len(currencies))
    print("Код валюты 840:",currencies.get("840", "Валюта не найдена"))
if __name__ == "__main__":
    show_currencies()
