import unittest
from docedian.base import InvoiceBuilder

class TestBaseInvoice(unittest.TestCase):
    """
    Test the base invoice class
    """
    
    def test_build_invoice(self):
        """
        """
        data = {
            "header": {
                "document": "FV",
            },
            "document_name": "Factura",
            "serie": "FV",
            "number": "1",
            "date": "2019-01-01",
            "currency": "RON",
            "exchange_rate": 1,
        }
        invoice = InvoiceBuilder()
        invoice = invoice.build_document(data)
        print(invoice.header.document)