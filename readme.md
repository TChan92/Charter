This is a personal project of mine to create a better, more interactive way of comparing Javascript graphing libraries.

Requirements: Postgresql, pip, python3.6

If you want to run the code yourself:
1. Clone the repository and cd into it
2. Create virtualenv (optional)
3. pip install -r requirements.txt
4. The following environment variables must be set:
  * DJANGO_SETTINGS_MODULE=Charter.settings
  * SECRET_KEY
  * The following 5 are all relating to Postgres
  * DB_NAME
  * USERNAME
  * PASSWORD
  * HOSTNAME
  * PORT
5. Install Postgres
6. Install Memcached
7. python manage.py runserver

Roadmap:
* Host on S3 bucket
* Add more chart types
* Add more charting libraries
* Add more library specific options
* Add real data from open dataset
* Add editable source code
* Add personal notes on each library
* Use React
