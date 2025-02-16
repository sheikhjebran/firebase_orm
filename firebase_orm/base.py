import firebase_admin
from firebase_admin import credentials, firestore
from .cache import CacheManager


class FirebaseORM:
    cache = CacheManager()

    def __init__(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate(
                "firebase_credentials.json")  # Change to your path
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.collection_name = None

    def get_all(self):
        """Retrieve all documents, using cache if available"""
        cache_key = f"{self.collection_name}_all"
        cached_data = self.cache.get(cache_key)
        if cached_data:
            return cached_data

        docs = [doc.to_dict()
                for doc in self.db.collection(self.collection_name).stream()]
        self.cache.set(cache_key, docs)
        return docs

    def get_by_id(self, doc_id):
        """Retrieve a document by ID"""
        cache_key = f"{self.collection_name}_{doc_id}"
        cached_data = self.cache.get(cache_key)
        if cached_data:
            return cached_data

        doc = self.db.collection(self.collection_name).document(doc_id).get()
        data = doc.to_dict() if doc.exists else None
        if data:
            self.cache.set(cache_key, data)
        return data

    def filter(self, field, operator, value):
        """Filter documents based on a condition"""
        query = self.db.collection(self.collection_name).where(
            field, operator, value).stream()
        return [doc.to_dict() for doc in query]

    def create(self, doc_id, data):
        self.db.collection(self.collection_name).document(doc_id).set(data)

    def update(self, doc_id, data):
        self.db.collection(self.collection_name).document(doc_id).update(data)

    def delete(self, doc_id):
        self.db.collection(self.collection_name).document(doc_id).delete()

    def get_paginated(self, order_by, limit, last_doc=None):
        """Paginate results with an optional starting document"""
        query = self.db.collection(
            self.collection_name).order_by(order_by).limit(limit)
        if last_doc:
            query = query.start_after(last_doc)
        docs = query.stream()
        return [doc.to_dict() for doc in docs]

    def run_transaction(self, doc_id, update_data):
        """Perform an atomic transaction"""
        def transaction_function(transaction, ref):
            snapshot = ref.get(transaction=transaction)
            if snapshot.exists:
                transaction.update(ref, update_data)

        doc_ref = self.db.collection(self.collection_name).document(doc_id)
        transaction = self.db.transaction()
        transaction_function(transaction, doc_ref)
