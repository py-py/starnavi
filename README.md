# starnavi 

Quickstart:
1. pip install -r requirements.txt 
2. python manage.py migrate
3. python manage.py add_superuser
4. python manage.py runserver
5. python bot.py

Some configs are in .env
### For check result:
- curl http://localhost:8000/api/posts/
- curl http://localhost:8000/api/users/


### API Docs:
http://localhost:8000/api/docs/

### Admin(dadmin/dadmin01):
http://localhost:8000/admin/ 

### Example for displaying of using CLEARBIT and EMAILHUNTER services:
curl -X POST \
  http://localhost:8000/api/signup/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "username": "alexclearbit",
  "password": "password",
  "email": "alex@clearbit.com"
}'

### Docker
- docker build -t starnavi . --no-cache
- docker run --name starnavi -d -p 8000:8000 starnavi