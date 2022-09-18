# Contributing

## Testing

Tests are run using the python package `tox`.

```bash
tox -e unit  # Unit tests
tox -e static  # Static analysis
tox -e lint  # Linting
```

## Deploying locally

Run the server using uvicorn:
```bash
cd src
uvicorn main:app --reload
```
