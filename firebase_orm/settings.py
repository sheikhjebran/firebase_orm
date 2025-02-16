import firebase_admin
from firebase_admin import credentials


def initialize_firebase():
    import os
    from django.conf import settings

    FIREBASE_CREDENTIALS = getattr(settings, "FIREBASE_CREDENTIALS", None)

    if FIREBASE_CREDENTIALS and not firebase_admin._apps:
        cred = credentials.Certificate(FIREBASE_CREDENTIALS)
        firebase_admin.initialize_app(cred)
