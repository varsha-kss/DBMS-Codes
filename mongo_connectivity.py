from pymongo.mongo_client import MongoClient

connectionURL = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.4"


class Connection:
    def __init__(self, connectionURL):
        self.client = MongoClient(connectionURL)
        self.db = None
        self.collection = None
        try:
            self.client.admin.command("ping")
            print("connected to mongoDB succesfully !")
        except Exception as e:
            print("connection failed with error : ", e)

    def show_databases(self):
        databases = self.client.list_database_names()
        for i in range(len(databases)):
            print("{0}. {1}".format(i + 1, databases[i]))

    def set_database(self, dbName):
        self.db = self.client[dbName]

    def set_collection(self, collectionName):
        self.collection = self.db[collectionName]

    def show_collections(self):
        collections = self.db.list_collection_names()
        for i in range(len(collections)):
            print("{0}. {1}".format(i + 1, collections[i]))

    def list_documents(self):
        results = self.collection.find({})
        print("rollno\tname\t\tbranch\t\tattendance\tage")
        for doc in results:
            print(
                "{0}\t{1}\t\t{2}\t\t{3}\t{4}".format(
                    doc["rollno"],
                    doc["name"],
                    doc["branch"],
                    doc["attendance"],
                    doc["age"],
                )
            )

    def create_document(self):
        print("\nenter new student details")
        name = input("name of student : ")
        rollno = int(input("roll number : "))
        age = int(input("age : "))
        branch = input("branch : ")
        attendance = int(input("attendance : "))

        newStudent = {
            "name": name,
            "rollno": rollno,
            "age": age,
            "branch": branch,
            "attendance": attendance,
        }
        self.collection.insert_one(newStudent)

        print("\nnew Student added !")

    def delete_document(self):
        rollno = int(input("\nenter roll number of student to remove : "))
        query = {"rollno": rollno}
        self.collection.delete_one(query)

        print("\n student removed Successfully!")

    def update_document(self):
        rollno = int(input("\nenter roll num of student to update : "))
        attendance = int(input("enter new attendance : "))
        self.collection.update_one(
            {"rollno": rollno}, {"$set": {"attendance": attendance}}
        )

        print("\nstudent updated Successfully!")

    def close(self):
        self.client.close()


client = Connection(connectionURL)
while True:
    print("\n\t\t\tStudent Database\t\t\t")
    print("1. Show all Students")
    print("2. Add new Student")
    print("3. edit Student information")
    print("4. delete Student information")
    print("5. change/select database")
    print("6. change/delete collection")

    ch = int(input("\nenter option : "))

    if ch == 1:
        client.list_documents()

    elif ch == 2:
        client.create_document()

    elif ch == 3:
        client.update_document()
    elif ch == 4:
        client.delete_document()

    elif ch == 5:
        client.show_databases()
        dbName = input("enter name of database : ")
        client.set_database(dbName)

    elif ch == 6:
        client.show_collections()
        collectionName = input("enter collection name : ")
        client.set_collection(collectionName)

    elif ch > 6:
        client.close()
        print("thank you !")
        break
