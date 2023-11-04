import mysql.connector as mc

options = {
    "host": "localhost",
    "user": "root",
    "password": "Suj@y543",
    "database": "test",
}


class Connection:
    def __init__(self, options):
        try:
            self.client = mc.connect(**options)
            self.cursor = self.client.cursor()
            if self.client.is_connected():
                print(f"connected to database succssfully !")
        except self.client.error as err:
            print(f"failed to connect error : {err}")

    def list_rows(self):
        self.cursor.execute("SELECT * FROM publisher")
        results = self.cursor.fetchall()

        print("bookID\tBook Name\t\tAuthor\t\tprice")
        for row in results:
            print(
                "{0}\t{1}\t\t\t\t{2}\t\t{3}".format(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                )
            )

    def create_row(self):
        print("\nenter new book details")
        bookName = input("name of book : ")
        author = input("name of Author : ")
        price = float(input("price of book : "))

        self.cursor.execute(
            "INSERT INTO publisher(book_name,author,price) VALUES(%s,%s,%s)",
            (bookName, author, price),
        )
        self.client.commit()

        print("\nnew book added !")

    def delete_row(self):
        bookID = int(input("\nenter id of book to remove : "))
        self.cursor.execute(f"delete from publisher where book_id={bookID}")
        self.client.commit()
        print("\n book removed Successfully!")

    def update_row(self):
        bookID = int(input("\nenter book id to update : "))

        price = float(input("price of book : "))
        query = "update publisher set price={0} where book_id={1}".format(price, bookID)
        self.cursor.execute(query)
        self.client.commit()

        print("\nbook data updated Successfully!")

    def search_row(self):
        authorName = input("enter name of author : ")
        self.cursor.execute(
            f"SELECT * FROM publisher WHERE author LIKE '%{authorName}%'"
        )
        results = self.cursor.fetchall()
        print("bookID\tBook Name\t\tAuthor\t\tprice")
        for row in results:
            print(
                "{0}\t{1}\t\t\t\t{2}\t\t{3}".format(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                )
            )

    def close(self):
        self.client.close()
        self.cursor.close()


client = Connection(options)
while True:
    print("\n\t\t\tLibrary\t\t\t")
    print("1. Show all books")
    print("2. Add new Book")
    print("3. update Book information")
    print("4. delete Book information")
    print("5. search Book information")

    ch = int(input("\nenter option : "))

    if ch == 1:
        client.list_rows()

    elif ch == 2:
        client.create_row()

    elif ch == 3:
        client.update_row()
    elif ch == 4:
        client.delete_row()

    elif ch == 5:
        client.search_row()

    elif ch > 6:
        client.close()
        print("thank you !")
        break
