# Technical Assessment

The backend in Django for the technical assessment for A2ODev.

## Steps to install and run the project:
Versions
```
Python: 3.11.14
pip: 23.1.2
```
Create virtual environment
```
python -m venv venv
```
Activate virutal environment (Windows)
```
.\venv\Scripts\activate
```
Install the dependencies
```
pip install -r requirements.txt
```
Run the migrations
```
python manage.py migrate
```
Run the server
```
python manage.py runserver
```
## Instructions
Django rest framework was used to create the API. The API consists of 2 routes: api/chess-problem and api/strings-problem. The problems are solved in the views folder.
  
