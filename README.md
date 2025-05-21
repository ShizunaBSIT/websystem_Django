# Webhosting Render Link
[https://websystem-django.onrender.com](https://websystem-django-rlpz.onrender.com)

# How to access and run the project
On the repository's main page, look for the green "<> Code" Button and if you have Github Desktop, choose "Open with Github Desktop"

### Create a Virtual Environment
```python -m venv venv```

### Navigate to the project directory
Once done cloning the repository and you opened your visual studio code on the github repository
open your terminal and navigate to the wandermart directory

```cd wandermart```

### Install requirements
```pip install -r requirements.txt```

### .env configuration
<details>
  <summary>.env Variables</summary>
SECRET_KEY = 'django-insecure-y_ci^(vn9ftaolkbf=o$v-zk(2hu0nwdjx9a=b3cuitb4p5lw%'

DEBUG = 1

ALLOWED_HOSTS = "*"

DATABASE_URL = "postgresql://django_postgre_jn1r_user:nfRIbAyoj7VK35PLHhAo8oNLkLFUqSX7@dpg-d0kt1gruibrs739qn83g-a.singapore-postgres.render.com/django_postgre_jn1r"

CLOUDINARY_API_KEY = "166145672319393" <br>
CLOUDINARY_CLOUD = "da0w1naw1" <br>
CLOUDINARY_API_SECRET = "ScvuCUZPlEF93zZoDTHohVIfsn0"
</details>

### Run server
```python manage.py runserver```
