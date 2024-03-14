from requests import get, post, delete
from datetime import datetime

print(get('http://localhost:5000/api/v2/user').json())
print(get('http://localhost:5000/api/v2/user/2').json())
print(get('http://localhost:5000/api/v2/user/999').json())
print(get('http://localhost:5000/api/v2/user/6').json())
print(get('http://localhost:5000/api/v2/user/q').json())
print(post('http://localhost:5000/api/v2/user', json={}).json())
print(post('http://localhost:5000/api/v2/user', json={'name': 'ur'}).json())
print(post('http://localhost:5000/api/v2/user', json={
    'name': 'Заголовок3',
    'about': 'Текст новости3',
    'email': 3,
    'hashed_password': 123,
    'created_date': datetime.now()}).json())
print(delete('http://localhost:5000/api/v2/user/999').json()) # новости с id = 999 нет в базе
print(delete('http://localhost:5000/api/v2/user/2').json())
