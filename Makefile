run:
	python blog/manage.py runserver

make-migrate:
	python blog/manage.py makemigrations

migrate:
	python blog/manage.py migrate

freeze:
	pip freeze > requirements.txt

shell:
	python blog/manage.py shell_plus --print-sql

flake:
	flake8 ./blog
