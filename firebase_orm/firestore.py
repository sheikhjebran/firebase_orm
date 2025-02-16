from .base import FirebaseORM


class FirestoreModel(FirebaseORM):
    def __init__(self, collection_name):
        super().__init__()
        self.collection_name = collection_name

    def batch_create(self, data_list):
        """Batch create documents"""
        batch = self.db.batch()
        for doc_id, data in data_list:
            ref = self.db.collection(self.collection_name).document(doc_id)
            batch.set(ref, data)
        batch.commit()

    def batch_update(self, data_list):
        """Batch update documents"""
        batch = self.db.batch()
        for doc_id, data in data_list:
            ref = self.db.collection(self.collection_name).document(doc_id)
            batch.update(ref, data)
        batch.commit()
