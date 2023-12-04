- instalar msqlclient
- em settings colocar as configurações do bd

 settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME":'db_mysite',
        "USER": 'ROOT',
        "PASSAWORD": '',
        "HOST": 'localhost',
        "PORT": '3306',
    }
}

- colocar o DEBUG= False
- Se quiser colocar ip ED_HOST = ['projet-dajang.fly.dev']

Pega todos os arquivos estaicos e junto numa pasta só:
-python manage.py collectstatic 

-terminei o projeto fazer isso colcar um securty key melhor, colcar um Bd de dados melhor

### SOBRE O SERVIDOR WEB
- Tem um intercambio entre django o Gunicorn: Responsavel por traduzir o codigo python para o servidor

pip install gunicorn



bibliotac no python que cria adi aleatório:  uuid ja vem no python.




