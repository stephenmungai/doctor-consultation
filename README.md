# doctor-consultation
REQUIEREMENTS
An installation of python 3.8 on your computer
INSTALLATION
Clone the github repository to a folder of your liking
Open the folder using VSCode
Using the VSCode terminal run the following commands:
pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

Fill in the username,email,password as this will be the admin credentials
To run the server use:

python manage.py runserver
Admin Console
To access the admin console use the following url: http://127.0.0.1:8000/admin. Log in with the credentilas in section 1 part 3
