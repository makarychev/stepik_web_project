gunicorn -c hello.py -b 0.0.0.0:8080 hello:wsgi_application