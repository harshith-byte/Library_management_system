# Library_management_system

## About Project
- Library Management System is all about managing Books by appling CRUD operations.
- Docker Container is used to run this project
- 

- In this project we have 2 Database tables 
  - Account
  - Book
  - User (Default django model)
  
- Frontend
  - HTML
  - CSS
  - JS 

- API'S 
  ```
  - 0.0.0.0:8000/api/                                   API Overview
  - 0.0.0.0:8000/api/savebook/                          API To CREATE new Book Object
  - 0.0.0.0:8000/adminviewapi/                          API To READ all books and dump in ADMIN page
  - 0.0.0.0:8000/api/updatebook/<str:pk>/<str:pk>/      API To UPDATE specific Book object from ADMIN page
  ```
- Backend
  - MySQL
  
- Framework
  - Django and Django rest-framework 

- Django provides it's default admin panel where superuser can create, update or delete data

## Steps to Run the Project(only for win/linux):

- Install docker and docker-compose *if not installed*
  - [docker-installation](https://docs.docker.com/compose/install/)

- Pull git repo to local machine 
```
  - git clone git@github.com:harshith-byte/Library_management_system.git
```

- open terminal and Change directory to main
```
  - cd lms/
```

- permisssion for the data had to changed
```
  - sudo chmod -R 777 data
```

- run docker-compose to start MySQL database 
```
  - docker-compose up db
```

- run docker-compose to start Application 
```
  - docker-compose up web
```

- Open any browser and type :
```
  - 0.0.0.0:8000/
```

- To stop docker type in terminal
```
  - ctrl+c
```

- To create a superuser in django
```
  - docker-compose web run python manage.py createsuperuser
```

- To Turn down docker
```
  - docker-compose down
```
