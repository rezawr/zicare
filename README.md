
# Assestment by Zicare

Reza Wahyu Ramadhan
[![Built with FastAPI](https://img.shields.io/badge/built%20with-FastAPI-ff69b4.svg?logo=cookiecutter)](https://github.com/karec/cookiecutter-flask-restful)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Installation

Install my project within your git. then try to install the requirement of the projects by using syntax below

```bash
  pip install -r requirements.txt
```

Create Mariadb or Mysql DB, rename .env.sample -> .env and edit user,password,dbname. Then use the code below for start migrating your database.
```
   alembic upgrade head
```

then start the server

```
  uvicorn app.main:app --host 0.0.0.0 --port 8888 --reload
```

or

```
  uvicorn app.main:app --host 0.0.0.0 --port 8888
```

For the api documentation, you can access */docs* or using redoc by the url */redoc*

My Projects is built within project template with a little bit of improvisation. 

[Format](https://github.com/phalconvietnam/FastAPI-project-template).

*note : default credential is email : admin@example.com, and password : secret
##  My Answer

*will be in bahasa*

Untuk menyelesaikan permasalahan penentuan 5 tamiya tercepat atau secara general yang ingin dilakukan adalah melakukan sorting. Pada kasus ini saya memilih menggunakan algoritma Merge Sort. Pada algoritma ini memiliki:

Average Complexity = O(n × log n)

Worst Case = O(n × log n)

Best Case = O(n × log n)

Space Complexity = O(n)

Jadi jika ada 5 jalur maka bisa dilakukan multiple iterasi dalam 1 waktu yang sama.


