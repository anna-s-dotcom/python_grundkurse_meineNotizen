import sqlite3

class Country_db:
    def __init__(self,name):
        self.filename=name + ".db"
        self.createDB()

#verbindung mit der Datenbank
    def createDB(self):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreingn_keys=ON")
            c=con.cursor()
#id ist eindeutig als primary key
            c.execute("""CREATE TABLE IF NOT EXISTS
            countries(name TEXT PRIMARY KEY, population INTEGER,
            capital TEXT );""")



            c.execute("""CREATE TABLE IF NOT EXISTS cities(id INTEGER
            PRIMARY KEY, name TEXT, country TEXT, capital INTEGER, FOREIGN KEY (country) REFERENCES countries(name));""")

            c.close()



    def insert_country(self,name,population,capital):
        with sqlite3.connect(self.filename) as con:
                con.execute("PRAGMA foreingn_keys=ON")
                c=con.cursor()
                try:
                    c.execute("INSERT INTO countries(name,population,capital) VALUES (?, ?,?);",
                    (name,population,capital))
                except:
                    pass

                con.commit() #"tue es"
                c.close()

    def insert_cities(self,name,country,capital):
        with sqlite3.connect(self.filename) as con:
                con.execute("PRAGMA foreingn_keys=ON")
                c=con.cursor()
                try:
                    c.execute("INSERT INTO cities(name,country,capital) VALUES (?, ?,?);",
                    (name,country,capital))
                except:
                    pass

                con.commit() #"tue es"
                c.close()

    def selectAll(self,table):
        with sqlite3.connect(self.filename) as con:
                con.execute("PRAGMA foreingn_keys=ON")
                c=con.cursor()
                if table=="countries":
                    c.execute("SELECT* FROM countries")

                elif table=="cities":
                    c.execute("SELECT* FROM cities")

                entries=c.fetchall()
                c.close()
        return entries

    def selectCountry(self,country):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreingn_keys=ON")
            c=con.cursor()

            c.execute("SELECT* FROM countries WHERE name=?;",
            (country,))

            country=c.fetchone()

            c.close()
        return country

    def wrongCities(self):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreingn_keys=ON")
            c=con.cursor()
            c.execute("SELECT capital FROM countries;")
            correct=c.fetchall()

            c.execute("SELECT name from cities WHERE capital=1")
            maybe_correct=c.fetchall()
            c.close()
            not_correct=[]
            for elem in maybe_correct:
                if elem not in correct:not_correct.append(elem)
            return(not_correct)





    # def vergleich(self):
    #     with sqlite3.connect(self.filename) as con:
    #         con.execute("PRAGMA foreingn_keys=ON")
    #         c=con.cursor()
    #
    #     try:
    #         c.execute("SELECT name, country FROM cities WHERE name=capital?")
    #     except:
    #         print("Wrong")


my_db=Country_db("country")

name=("Frankreich")
population=83
capital=("Paris")


my_db.insert_country(name,population,capital)
my_db.insert_cities(capital,name,1)

countries=my_db.selectAll("cities")
print(countries)

print(my_db.wrongCities())
