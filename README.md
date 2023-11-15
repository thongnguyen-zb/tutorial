# Sample DRF to test vesrioning

## Useful commands

```
# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

pip install -r requirements.txt

# Make migrations
python manage.py makemigrations

# Migrate the database
python manage.py migrate

# Run the server
python manage.py runserver
```
