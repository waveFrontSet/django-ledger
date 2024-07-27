# A small ledger app in Django

## Getting up and running

`docker compose up -d --build` will fire up three containers:

- One permanent container each for the database and a webserver serving the
  django app and
- One temporary container to apply migrations.

Because the provided `Dockerfile` uses `manage.py` as its entrypoint, you may
use the following command to fire up the interactive django shell to interact
with models:

``` sh
docker compose run web shell
```

## Running tests

Because docker compose builds the `development` target of the `Dockerfile`, `pytest`
and all necessary dev dependencies are installed. You may run tests in the already
running `web` container via

``` sh
docker compose exec web pytest
```
