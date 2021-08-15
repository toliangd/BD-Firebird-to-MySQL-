import fdb # модуль для Firebird
import os.path # модуль для isfile
import pyodbc # модуль для MSSql

""" Подключение к БД FireBird """
conF = fdb.connect(dsn='localhost:f:/program/DB/FireBird/FB.FDB',
                   user='SYSDBA',
                   password='123QWEasd')
curF = conF.cursor() #объект делающий запосы и принимающий ответы от БД

curF.execute("SELECT firstname FROM FIRSTNAME") #берем значения из столбца "firstname" таблицы "FIRSTNAME"
firstname = curF.fetchall()
curF.execute("SELECT surname FROM SURNAME") #
surname = curF.fetchall()

""" Проверка вывода из БД """
print(firstname,
      '\n',
      surname)

""" Проверка наличия файлов """
if os.path.isfile('F:\\program\\DB\\firstname.txt') == False and os.path.isfile('F:\\program\\DB\\surname.txt') == False:

      """ Запись имен в файл """
      f = open('F:\\program\\DB\\firstname.txt', 'w')
      for i in firstname:
            f.write(str(i[0]) + '\n')
      f.close()

      """ Запись фамилий в файл """
      f = open('F:\\program\\DB\\surname.txt', 'w')
      for i in surname:
            f.write(str(i[0]) + '\n')
      f.close()

else:
      print('files exist')

curF.close()

""" Подключение к MSSql (использую удаленный сервер)"""
conM = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=192.168.15.30;'
                      'DATABASE=FnSn;'
                      'UID=SA;'
                      'PWD=123QWEasd')
curM = conM.cursor()

"""строки файла - элементы списка"""
sn = open('F:\\program\\DB\\surname.txt', 'r')
LineS = [line.strip() for line in sn]

fn = open('F:\\program\\DB\\firstname.txt', 'r')
LineF = [line.strip() for line in fn]

""" Проверка списка """
print(LineF, LineS)

""" Заполнение БД MSSql """
if len(LineF) == len(LineS):
    for i in range(len(LineF)):

        curM.execute("INSERT INTO name (firstname, surname) VALUES ({},{})".format("'" + LineF[i] + "'", "'" + LineS[i] + "'"))
        conM.commit()
else:
    print('БД FireBird разной мощности')

""" Вывод из MSSql """
curM.execute("SELECT * FROM name")
print(curM.fetchall())

curM.close()