import sqlalchemy


engine = sqlalchemy.create_engine('postgresql+psycopg2://:@localhost:5432/postgres')
connection = engine.connect()


code = """
SELECT name FROM album
    WHERE year = 2018;
"""
res = connection.execute(code).fetchall()
print(f'Альбомы, вышедшие в 2018 году: {"; ".join([i[0] for i in res])}')


code = """
SELECT name, length FROM track
    ORDER BY length;
"""
res = connection.execute(code).fetchall()
print(f'Самый продолжительный трек: {res[-1][0]} ({res[-1][1]} сек.)')


code = """
SELECT name FROM track
    WHERE length >= 210;
"""
res = connection.execute(code).fetchall()
print(f'Треки продолжительнее 3,5 мин.: {"; ".join([i[0] for i in res])}')


code = """
SELECT name FROM collection
    WHERE year BETWEEN 2018 AND 2020;
"""
res = connection.execute(code).fetchall()
print(f'Сборники, вышедшие с 2018 по 2020 гг.: {"; ".join([i[0] for i in res])}')


code = """
SELECT name FROM author
    WHERE name NOT LIKE '%% %%';
"""
res = connection.execute(code).fetchall()
print(f'Исполнители, чье имя состоит из 1-го слова: {"; ".join([i[0] for i in res])}')


code = """
SELECT name FROM track
    WHERE name LIKE '%%My%%' OR name LIKE '%%Мой%%';
"""
res = connection.execute(code).fetchall()
print(f'Треки, содержащие слово "My"/"Мой": {"; ".join([i[0] for i in res])}')
