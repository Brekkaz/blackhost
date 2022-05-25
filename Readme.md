### Comando para formatear el codigo con normas pep8

docker-compose run --rm web black .

### Comando para crear las tablas

docker-compose run --rm web python ./app/db/create_tables.py

### Comando para eliminar las tablas

docker-compose run --rm web python ./app/db/drop_tables.py

### Comando para ejecutar los seeders

docker-compose run --rm web python ./app/db/seeders.py
