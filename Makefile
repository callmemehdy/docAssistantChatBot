
db_file		=	src/pop_db.py
agent_file	=	src/evaluate_queries.py


all: setup_db
	@echo "agent loading..."
	@python3 $(agent_file)

setup_db:
	@python3 $(db_file)

reset_db:
	@python3 $(db_file) --reset

