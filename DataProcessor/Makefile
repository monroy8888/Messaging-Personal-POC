# Variables
DOCKER_COMPOSE = docker-compose
FLASK_APP = $(DOCKER_COMPOSE) run --rm flask_app


# Build the image
build:
	$(DOCKER_COMPOSE) build

# Run the image
up:
	$(DOCKER_COMPOSE) up -d --build
# Run & build the image/Container

run:
	$(DOCKER_COMPOSE) up --build

# Show Docker logs
logs:
	$(DOCKER_COMPOSE) logs -f

# Clean up all unused Docker resources
stop:
	$(DOCKER_COMPOSE) stop

# Execute a shell inside the preprocessor-app container
bash-one:
	docker exec -it my_python3.11_app bash

# Execute a shell inside the preprocessor-app container
bash-two:
	docker exec -it my_python2.7_app bash

#Run 3.11 with pdb
pdb-one:
	docker attach my_python3.11_app

#Run 2.7 with pdb
pdb-two:
	docker attach my_python2.7_app


#MIGRATIONS
# Command to create the initial migrations
migrate-init:
	$(FLASK_APP) flask db init

# Command to generate a new migration automatically
migrate-revision:
	$(FLASK_APP) flask db migrate -m "Migration description"

# Command to apply pending migrations
migrate-upgrade:
	$(FLASK_APP) flask db upgrade

# Command to roll back the last applied migration.
migrate-downgrade:
	$(FLASK_APP) flask db downgrade

# Command to show the current status of migrations.
migrate-status:
	$(FLASK_APP) flask db current

# Command to show the history of applied migrations
migrate-history:
	$(FLASK_APP) flask db history

# Command to clean and delete migrations (be careful: this will delete the migrations history)
migrate-clean:
	rm -rf migrations

# Command to clean and remove migrations and the database (be careful: this will remove all data)
migrate-reset: migrate-clean migrate-init
