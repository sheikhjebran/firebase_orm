## How to install package

```sh
pip install firebase-admin
```

## Add fiebase Condig to setting.py

```python
FIREBASE_CREDENTIALS = "path/to/serviceAccountKey.json"
```

## Initialize Firebase in apps.py

```python
from django.apps import AppConfig
from firebase_orm.settings import initialize_firebase

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        initialize_firebase()

```

## Define a Django-like Model Using Firebase ORM

```python
from firebase_orm.firestore import FirestoreModel

class User(FirestoreModel):
    def __init__(self):
        super().__init__("users")

```

## Use Firebase ORM in Django Views

```python
from django.http import JsonResponse
from .models import User

def get_users(request):
    users = User().get_all()
    return JsonResponse(users, safe=False)

def create_user(request):
    user_model = User()
    user_model.create("user123", {"name": "John Doe", "email": "john@example.com"})
    return JsonResponse({"message": "User created"})

```

## Firebase Authentication in Django

```python
from django.http import JsonResponse
from firebase_orm.auth import FirebaseAuth

def verify_token(request):
    id_token = request.headers.get("Authorization")
    user = FirebaseAuth.verify_token(id_token)

    if user:
        return JsonResponse(user)
    return JsonResponse({"error": "Invalid token"}, status=401)

```

## use of filter

```python
users = User().filter("age", ">=", 18)
print(users)

```

## Batch functionality

```python
users = User()
users.batch_create([
    ("user1", {"name": "Alice", "age": 25}),
    ("user2", {"name": "Bob", "age": 30}),
])

```

## Pagination

```python
users = User().get_paginated(order_by="age", limit=10)
print(users)
```

## run Transaction

```python
User().run_transaction("user1", {"age": 26})

```
