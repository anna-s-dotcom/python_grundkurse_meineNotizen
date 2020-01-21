import sqlite3


class BlogsDB:
    def __init__(self, name):
        self.filename = name + '.db'
        self.__createDB()

#Tabelle mit den Werten erstellen, id wird automatisch erstellt

    def __createDB(self):
        with sqlite3.connect(self.filename) as con:
            c = con.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS user(username TEXT PRIMARY KEY, email TEXT );""")

            c.execute("""CREATE TABLE IF NOT EXISTS
                        blogs(id INTEGER PRIMARY KEY,
                                author TEXT, content TEXT,
                                FOREIGN KEY (author)
                                REFERENCES user(username));""")
            c.close()


#user hinzufügen, commit nach dem execute
    def insert_user(self, username, email):
        with sqlite3.connect(self.filename) as con:
            c = con.cursor()
            try:
                c.execute("""INSERT INTO user(username,email) VALUES (?, ?);""", (username,email))

            except Exception as e:
                print(e)

            con.commit()
            c.close()




#user werden verändert# try ,except - hier nachschauen

    def update_user(self,name,email):
        with sqlite3.connect(self.filename) as con:
            c = con.cursor()

            c.execute("""UPDATE user SET email = ?
                         WHERE username = ?;""", (name,email))

            con.commit()
            c.close()


#user werden gelöscht / wie lösche ich gleichzeotig acuh blogs - hier nachschauen wen ich gelöscht habe
    def delate_user(self,name):
        with sqlite3.connect(self.filename) as con:
            c = con.cursor()
            c.execute('DELETE FROM blogs WHERE author = ?;', (name,))
            c.execute('DELETE FROM user WHERE username = ?;', (name,))

            con.commit()
            c.close()



#blogs werden hinzugefügt- warum muss hier foreign key sein

    def insert_blogs(self, author, content):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreign_keys = ON")
            c = con.cursor()
            try:
                c.execute("""INSERT INTO blogs(author,content) VALUES (?, ?);""", (author,content))
            except Exception as e:
                print(e)

            con.commit()
            c.close()

#blogs werden verändert

    def update_blogs(self,content,id):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreign_keys = ON")
            c = con.cursor()

            c.execute("""UPDATE blogs SET content=?
                         WHERE id = ?;""", (content,id))

            con.commit()
            c.close()




#tabellen auslesen
    def selectAll(self, table):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreign_keys = ON")
            c = con.cursor()
            if table == 'user':
                c.execute('SELECT * FROM user')
            elif table == 'blog':
                c.execute('SELECT * FROM blog')

            entries = c.fetchall()
            c.close()
        return entries

#eingabe eines users /ausgabe aller blogs, hier nachschauen
    def alleblogs_des_users(self,user):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreign_keys = ON")
            c = con.cursor()
            c.execute("""SELECT id,content FROM blogs
                        WHERE author = ?;""",(user,))
#immer ein tulpel, was das bedeutet
            blogs=c.fetchall()
            con.commit()
            c.close()

            for blog in blogs:
                print("ID:", blog[0])
                print()
                print(blog[1])
                print()
#eingabe eines blogs - user, was ist fetchone
    def user_des_blogs(self,id):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreign_keys = ON")
            c = con.cursor()
            c.execute("""SELECT author FROM blogs WHERE id= ?;""", (id,))

            user=c.fetchone()

            con.commit()
            c.close()

            try:
                print(user[0])
            except:
                print("Blog ID nicht vergeben")


if __name__ =="__main__":
#user werden hinzugefügt
    my_db =BlogsDB("projekttag2")
    #my_db.createDB()
    #
    # username="Monika"
    # email="anna-sz@gmx.net"
    my_db.insert_user("Monika","anna-sz@gmx.net")
    my_db.update_user("Monika","olek-sz@gmx.net")
    #my_db.delate_user()
    my_db.insert_blogs("Monika", "Hallo world!")
    my_db.update_blogs("UUUU",3)
    my_db.alleblogs_des_users("Monika")
    my_db.user_des_blogs("1")
