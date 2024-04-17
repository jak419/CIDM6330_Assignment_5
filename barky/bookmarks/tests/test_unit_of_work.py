from django.test import TestCase
from unittest.mock import patch
from bookmarks.unit_of_work import UnitOfWork

class UnitOfWorkTest(TestCase):
    @patch('bookmarks.unit_of_work.transaction.atomic')
    def test_unit_of_work_commit(self, mock_transaction):
        with UnitOfWork():
            pass

        mock_transaction.assert_called_once()

    @patch('bookmarks.unit_of_work.transaction.atomic')
    def test_unit_of_work_rollback(self, mock_transaction):
        with self.assertRaises(Exception):
            with UnitOfWork():
                raise Exception("Test Exception")

        mock_transaction.assert_called_once()
