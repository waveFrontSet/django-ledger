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

## Models

We've implemented the ledger using two models: One `Party` model identifying the sender
or recipient of a financial transaction and `Transaction` for the transaction data.

Noteworthy comments and thoughts:

- It is possible that the sender and the recipient are the same party. This has
  no impact on the computed balances, but it might pollute the database. We may
  prevent this by implementing [custom model
  validation](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.clean)
- We assume that the only request patterns are for a single party and any given
  date. If no date is given, we take the current date (on the server) as the
  default.
- It is possible for transactions to lie in the future.
