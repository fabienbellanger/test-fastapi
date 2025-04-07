# Test FastApi Python framework

## Installation

Create a virtual environment

```bash
python<version> -m venv <env name>
```

Activate the virtual environment

```bash
source <env name>/bin/activate
```

To deactivate the virtual environment:

```bash
deactivate
```

Freeze requirements

```bash
pip freeze > requirements.txt
```

Install dependancies

```bash
pip install -r requirements.txt
```

### Database

Create the database:

```bash
sqlite 3 app.db
sqlite 3 app.db < `schema.sql`
```

## pip

### Updating Python Packages on Windows or Linux

List of all outdated packages:

```bash
pip list --outdated
```

Edit `requirements.txt`, and replace all "==" with ">=".

Update

```bash
pip install -r requirements.txt --upgrade
pip freeze > requirements.txt
```

## Run

```bash
fastapi dev --reload
```

## Tests

```bash
pytest -v
```

## Todo

- [ ] Add authentication with `OAuth2` JWT:
  - https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
- [x] Use a database like `sqlite`:
  - https://medium.com/codenx/crafting-with-fastapi-sqlalchemy-and-pydantic-82ff305c5db1
  - https://fastapi.tiangolo.com/tutorial/sql-databases/
