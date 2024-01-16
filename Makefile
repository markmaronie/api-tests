## format_code:      Apply formatters
format_code:
	poetry run isort --settings-file .isort.cfg .
	poetry run black --config pyproject.toml .
