# Como rodar o projeto

1. Instale um virtualenv na pastado projeto
2. Instale os pacotes via pip

```
pip install -r requirements.txt
```

3. Instale o pacote no intepretador local

```
python setup.py develop
```

```
python manage.py makemigrations
```

```
python manage.py migrate
```


```
python manage.py createsuperuser
```

4. Teste se funcionou

```
python manage.py runserver
```
