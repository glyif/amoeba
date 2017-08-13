# amoeba

## safer way to store sensitive app settings

amoeba helps devs to store their app settings as environmental variables without the pain of setting individually

## Installing
### pip
```bash
pip install -i https://testpypi.python.org/pypi amoeba
```

## Using
To use amoeba, you'll need to create a `.env` file. This file can be anywhere, you just need to be able to pass in the file path to ameoba.

Example:
```
root-dir/   # arbitrary working directory name
  twix-main.py
  .env
  twix_bar/
    __init__.py
    twix.py
    bar.py
```

If you need to import .env in your `twix-main.py` file, the path will be `"./.env"`

### .env example
```
# .env
SECRET_API=2f05ee74-609d-4dbc-83ba-49cbff11fb18
TWIX_SECRET=cae68073-ca0f-4264-b80d-7da509030f7e
JU_DEEP_SECRET=3930f2ee-f48d-457d-b189-68d94c07f58e
```

### export .env variables into env variables
```python
# twix-main.py
import os
from amoeba import set_env

set_env("./.env")

# test printing envs
print(os.environ.get("SECRET_API"))
print(os.environ.get("TWIX_SECRET"))
print(os.environ.get("JU_DEEP_SECRET"))

