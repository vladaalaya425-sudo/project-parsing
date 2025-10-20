import xlsxwriter
from parsing_02 import array, top_books

def writer():
    try:
        book = xlsxwriter.Workbook(r"c:\Users\Lenovo\Desktop\Projects\Books.xlsx")
        
        page = book.add_worksheet("Книги")
        page_2 = book.add_worksheet("Топ книг")

        row = 0

        page.set_column("A:A", 30)
        page.set_column("B:B", 10)
        page.set_column("C:C", 50)
        page.set_column("D:D", 50)
        page.set_column("E:E", 50)
        page_2.set_column("A:A", 30)
        page_2.set_column("B:B", 10)
        page_2.set_column("C:C", 50)
        page_2.set_column("D:D", 50)
        page_2.set_column("E:E", 50)

        for item in array():
            page.write(row, 0, item[0])
            page.write(row, 1, item[1])
            page.write(row, 2, item[2])
            page.write(row, 3, item[3])
            page.write(row, 4, item[4])
            row += 1
        
        row = 0

        for item in top_books:
            page_2.write(row, 0, item["title"])
            page_2.write(row, 1, item["price"])
            page_2.write(row, 2, item["text"])
            page_2.write(row, 3, item["url_img"])
            page_2.write(row, 4, item["url"])
            row += 1

        print(f"Файл сохранен: Books.xlsx")
        book.close()
    except Exception as e:
        print(f"[Ошибка создания Excel] {e}")

if __name__ == "__main__":
    writer()
