import sqlite3

def menu_choice():
    choise = int(input("Your choice: "))
    if choise == 0:
        #word.delete_TABLE()
        Dictionary.create_basedata()
        # word.create_basedata()
    if choise == 1:
        word.show_records()
    if choise == 2:
        word.record_data_basedata()
    if choise == 3:
        word.update_eng_slovar()
    if choise == 4:
        word.delete_eng_slovar()
    if choise ==  5:
        word.delete_all()
    if choise == 6:
        print("Good bye!")
        return True

class Dictionary:
    """ Class Dictionary"""
    name_BD = "w003.dat"
    name_TABLE = "dictionary"
    name_COLUMN_1 = "eng"
    name_COLUMN_2 = "rus"
    sql = f"""CREATE TABLE {name_TABLE} 
             ({name_COLUMN_1}, {name_COLUMN_2},
              CONSTRAINT unq UNIQUE({name_COLUMN_1},{name_COLUMN_2}))"""
    __slots__ = ["eng", "rus"]

    def __init__(self):
        self.eng = ""
        self.rus = ""

    @classmethod
    def create_basedata(cls):
        """Create base data for dictionary"""
        conn = sqlite3.connect(cls.name_BD)
        cursor = conn.cursor()
        cursor.execute(cls.sql)
        print(f"Base data created in file: {cls.name_BD}")

    def record_data_basedata(self):
        """  Record into base data """
        while True:
            print("to exit enter: < quit >")
            eng = str(input("Enter the word in English: "))
            if eng == "quit":
                break
            rus = str(input("Enter the word in Russian: "))
            conn = sqlite3.connect(self.name_BD)
            cursor = conn.cursor()
            sql = f""" INSERT INTO dictionary VALUES ('{eng}','{rus}') """
            try:
                cursor.execute(sql)
                conn.commit()
            except sqlite3.IntegrityError:
                print("Such a bunch of words is already in the dictionary! ")
            finally:
                input("Press Enter to continue...")

    def update_eng_slovar(self):
        """ Update record in dictionary"""
        old_engl = str(input("Enter the word you want to change: "))
        new_engl = str(input("Enter a new word: "))
        new_rus = str(input("Enter the translation of the new word in russsian: "))
        conn = sqlite3.connect(self.name_BD)
        cursor = conn.cursor()
        sql = f""" UPDATE dictionary SET eng = '{new_engl}', rus = '{new_rus}'
                            WHERE eng = '{old_engl}'"""
        try:
            cursor.execute(sql)
            conn.commit()
        except sqlite3.IntegrityError:
            print("Such a bunch of words is already in the dictionary! ")
        finally:
            input("Press Enter to continue...")

    def delete_eng_slovar(self):
        """Delete record in TABLE"""
        conn = sqlite3.connect(self.name_BD)
        cursor = conn.cursor()
        delete_eng = str(input("Enter the word you want to delete: "))
        sql = f"DELETE FROM dictionary WHERE eng = '{delete_eng}'"
        try:
            cursor.execute(sql)
            conn.commit()
        except sqlite3.IntegrityError:
            print("Such a bunch of words is already in the dictionary! ")
        finally:
            input("Press Enter to continue...")

    def delete_all(self):
        """Delete all record in Base data"""
        conn = sqlite3.connect(self.name_BD)
        cursor = conn.cursor()
        sql = f"DELETE FROM dictionary"
        try:
            cursor.execute(sql)
            conn.commit()
        except sqlite3.IntegrityError:
            print("Such a bunch of words is already in the dictionary! ")
        finally:
            input("Press Enter to continue...")

    def delete_TABLE(self):
        """Delete TABLE in Base data"""
        conn = sqlite3.connect(self.name_BD)
        cursor = conn.cursor()
        sql = f"DROP TABLE dictionary"
        try:
            cursor.execute(sql)
            conn.commit()
        except sqlite3.IntegrityError:
            print("Such a bunch of words is already in the dictionary! ")
        finally:
            input("Press Enter to continue...")

    def show_records(self):
        """selection of display of sorted records """
        print("Menu: ")
        print("0 - Show all records order by id")
        print("1 - Show order by english")
        print("2 - Show order by russian")
        choise = int(input("Your choice: "))
        if choise == 0:
            word.print_alldata_basedata()
        if choise == 1:
            word.print_engl_basedata()
        if choise == 2:
            word.print_rus_basedata()

    def print_alldata_basedata(self):
        """Print all record from Base data"""
        conn = sqlite3.connect(self.name_BD)
        cursor = conn.cursor()
        sql = "SELECT rowid, eng, rus  FROM dictionary ORDER BY rowid"
        #cursor.execute(sql)
        #print(cursor.fetchall())
        print("========  Dictionary  ==========")
        for row in cursor.execute(sql):
            print(f"=  {row}  ")
        print(28 * "=")
        input("Press Enter to continue...")

    def print_engl_basedata(self):
        """Print sorted records from Base data"""
        conn = sqlite3.connect(self.name_BD)
        cursor = conn.cursor()
        sql = "SELECT eng, rus  FROM dictionary ORDER BY eng"
        # cursor.execute(sql)
        # print(cursor.fetchall())
        print("========  English ==========")
        for row in cursor.execute(sql):
            print(f"=  {row}  ")
        print(28*"=")
        input("Press Enter to continue...")

    def print_rus_basedata(self):
        """Print sorted records from Base data"""
        conn = sqlite3.connect(self.name_BD)
        cursor = conn.cursor()
        sql = "SELECT rus, eng  FROM dictionary ORDER BY rus"
        # cursor.execute(sql)
        # print(cursor.fetchall())
        print("========  Russian ==========")
        for row in cursor.execute(sql):
            print(f"=  {row}  ")
        print(28 * "=")
        input("Press Enter to continue...")

#=========== Main =====================
if __name__=='__main__':
    print("Eng-Ru Dictionary")
    word = Dictionary()
    while True:
        print("Menu: ")
        print("0 - Create new Base Data(BD)")
        print("1 - Show all records from BD")
        print("2 - Add record into BD")
        print("3 - Edit record in BD")
        print("4 - Delete record")
        print("5 - Delete all records")
        print("6 - Quit")

        if menu_choice():
            break





