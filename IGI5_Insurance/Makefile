DJANGO_SERVER := python3 manage.py

run-server:
	$(DJANGO_SERVER) runserver

migrate:
	$(DJANGO_SERVER) makemigrations && $(DJANGO_SERVER) migrate

superuser:
	$(DJANGO_SERVER) createsuperuser