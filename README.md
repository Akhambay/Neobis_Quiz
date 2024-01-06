# Project "Neobis_Quiz_Project"
Neobis_Quiz_Project is Django Rest Frame based web application. It allows users to read articles and take quizzes based on the articles. It also allows admins to add/edit articles and quizzes 
through admin panel. Users can search/filter articles and quizzes by category.

## Installation

1. Make sure you have Python version 3.x and pip installed
2. Clone the repository from GitHub:

```bash
git clone https://git@github.com:Akhambay/Neobis_Quiz.git
```
Install dependecies: 
```bash
pip install -r requirements.txt
```
Perform database migrations
```bash
python manage.py migrate
```
Start development server:
```bash
python manage.py runserver
```
Now your project is locally available at http://127.0.0.1:8000/
Also project is available at https://tokyo-backender.org.kg/
SSL Certificate is installed. Project is deployed to the DO server.

## Usage
The following functions are provided in the project:
1. Listing of all quizzes
2. Listing of all articles
3. Searching / filtering by category
4. Reading articles
5. Taking quizzes

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
assyl(dot)akhambay(at)gmail.com
