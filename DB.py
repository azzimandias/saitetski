import psycopg2

# подключение к базе данных
con = psycopg2.connect(host="",
                       database="",
                       user="",
                       password="")

# указатель
cur = con.cursor()


# закрыть подключение
con.close()
