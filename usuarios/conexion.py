import mysql.connector


def conectar():
    database = mysql.connector.connect(
      host = "localhost",
      user = "root",
      passwd = "",
      database = "leml_python",
    )
    cursor = database.cursor(buffered=True)
    return [database,cursor]

