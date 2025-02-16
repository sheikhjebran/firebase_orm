from firebase_admin import db


class FirebaseRealtimeORM:
    def __init__(self, ref_name):
        self.ref = db.reference(ref_name)

    def get_all(self):
        return self.ref.get()

    def get_by_id(self, doc_id):
        return self.ref.child(doc_id).get()

    def create(self, doc_id, data):
        self.ref.child(doc_id).set(data)

    def update(self, doc_id, data):
        self.ref.child(doc_id).update(data)

    def delete(self, doc_id):
        self.ref.child(doc_id).delete()
