# import transaction from django.db
from django.db import transaction

class UnitOfWork:
    def __enter__(self):
        # Begin a new transaction
        self.txn = transaction.atomic()
        self.txn.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # If an exception occurred, the transaction would be rolled back
        if exc_type:
            self.txn.__exit__(exc_type, exc_val, exc_tb)
            return False  
        else:
            # Else commit the transaction
            self.txn.__exit__(None, None, None)
            return True
