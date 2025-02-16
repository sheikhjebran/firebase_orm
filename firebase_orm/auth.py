from firebase_admin import auth


class FirebaseAuth:
    @staticmethod
    def verify_token(id_token):
        try:
            decoded_token = auth.verify_id_token(id_token)
            return decoded_token
        except Exception:
            return None

    @staticmethod
    def create_user(email, password):
        return auth.create_user(email=email, password=password)

    @staticmethod
    def get_user(uid):
        return auth.get_user(uid)
