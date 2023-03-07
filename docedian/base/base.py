from __future__ import annotations
from abc import ABC, abstractmethod


class Document(ABC):
    """
    Declara la interfaz de los documentos.
    """

    @abstractmethod
    def get_document(self) -> str:
        """
        Retorna el documento en formato XML
        """
        pass

    @abstractmethod
    def get_document_name(self) -> str:
        """
        Retorna el nombre del documento
        """
        pass

    @abstractmethod
    def get_document_type(self) -> str:
        """
        Retorna el tipo de documento
        """
        pass

    @abstractmethod
    def get_document_version(self) -> str:
        """
        Retorna la version del documento
        """
        pass

    @abstractmethod
    def get_document_schema(self) -> str:
        """
        Retorna el esquema del documento
        """
        pass

    @abstractmethod
    def get_document_schema_version(self) -> str:
        """
        Retorna la version del esquema del documento
        """
        pass

    @abstractmethod
    def get_document_schema_location(self) -> str:
        """
        Retorna la ubicacion del esquema del documento
        """
        pass

    @abstractmethod
    def get_document_signature(self) -> str:
        """
        Retorna la firma del documento
        """
        pass

    @abstractmethod
    def get_document_signature_version(self) -> str:
        """
        Retorna la version de la firma del documento
        """
        pass

    @abstractmethod
    def get_document_signature_schema(self) -> str:
        """
        Retorna el esquema de la firma del documento
        """
        pass

    @abstractmethod
    def get_document_signature_schema_version(self) -> str:
        """
        Retorna la version del esquema de la firma del documento
        """
        pass

    @abstractmethod
    def get_document_signature_method(self) -> str:
        """
        Retorna el metodo de firma del documento
        """
        pass

    @abstractmethod
    def get_document_signature_method_version(self) -> str:
        """
        Retorna la version del metodo de firma del documento
        """
        pass

    @abstractmethod
    def get_document_signature_method_schema(self) -> str:
        """
        Retorna el esquema del metodo de firma del documento
        """
        pass

    @abstractmethod
    def get_document_signature_method_transform(self) -> str:
        """
        Retorna la transformacion del metodo de firma del documento
        """
        pass

    @abstractmethod
    def get_document_signature_method_transform_version(self) -> str:
        """
        Retorna la version de la transformacion del metodo de firma del documento
        """
        pass

    @abstractmethod
    def get_document_signature_method_transform_schema(self) -> str:
        """
        Retorna el esquema de la transformacion del metodo de firma del documento
        """
        pass


class DocumentBuilder(ABC):
    """
    Declara la interfaz para crear los documentos.
    """

    @abstractmethod
    def build_document(self) -> None:
        """
        Construye el documento
        """
        pass

    @abstractmethod
    def build_document_name(self) -> None:
        """
        Construye el nombre del documento
        """
        pass

    @abstractmethod
    def build_document_type(self) -> None:
        """
        Construye el tipo de documento
        """
        pass

    @abstractmethod
    def build_document_version(self) -> None:
        """
        Construye la version del documento
        """
        pass

    @abstractmethod
    def build_document_schema(self) -> None:
        """
        Construye el esquema del documento
        """
        pass

    @abstractmethod
    def build_document_schema_version(self) -> None:
        """
        Construye la version del esquema del documento
        """
        pass

    @abstractmethod
    def build_document_schema_location(self) -> None:
        """
        Construye la ubicacion del esquema del documento
        """
        pass

    @abstractmethod
    def build_document_signature(self) -> None:
        """
        Construye la firma del documento
        """
        pass

    @abstractmethod
    def build_document_signature_version(self) -> None:
        """
        Construye la version de la firma del documento
        """
        pass

    @abstractmethod
    def build_document_signature_schema(self) -> None:
        """
        Construye el esquema de la firma del documento
        """
        pass

    @abstractmethod
    def build_document_signature_schema_version(self) -> None:
        """
        Construye la version del esquema de la firma del documento
        """
        pass

    @abstractmethod
    def build_document_signature_method(self) -> None:
        """
        Construye el metodo de firma del documento
        """
        pass

    @abstractmethod
    def build_document_signature_method_version(self) -> None:
        """
        Construye la version del metodo de firma del documento
        """
        pass

    @abstractmethod
    def build_document_signature_method_schema(self) -> None:
        """
        Construye el esquema del metodo de firma del documento
        """
        pass

    @abstractmethod
    def build_document_signature_method_transform(self) -> None:
        """
        Construye la transformacion del metodo de firma del documento
        """
        pass


class DocumentDirector():
    """
    Construye un objeto Document usando la interfaz DocumentBuilder.
    """

    def __init__(self, builder: DocumentBuilder) -> None:
        self._builder = builder

    def construct_document(self) -> None:
        self._builder.build_document()
        self._builder.build_document_name()
        self._builder.build_document_type()
        self._builder.build_document_version()
        self._builder.build_document_schema()
        self._builder.build_document_schema_version()
        self._builder.build_document_schema_location()
        self._builder.build_document_signature()
        self._builder.build_document_signature_version()
        self._builder.build_document_signature_schema()
        self._builder.build_document_signature_schema_version()
        self._builder.build_document_signature_method()
        self._builder.build_document_signature_method_version()
        self._builder.build_document_signature_method_schema()
        self._builder.build_document_signature_method_transform()

    @property
    def document(self) -> Document:
        return self._builder.document
    

class InvoiceBuilder(DocumentBuilder):
    """
    Construye un objeto Invoice usando la interfaz DocumentBuilder.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._invoice = Invoice()

    @property
    def document(self) -> Invoice:
        document = self._invoice
        self.reset()
        return document

    def build_document(self) -> None:
        self._invoice.document = 'Invoice'

    def build_document_name(self) -> None:
        self._invoice.document_name = 'Factura'

    def build_document_type(self) -> None:
        self._invoice.document_type = '01'

    def build_document_version(self) -> None:
        self._invoice.document_version = '1.0.0'

    def build_document_schema(self) -> None:
        self._invoice.document_schema = 'https://www.dian.gov.co/contratos/facturaelectronica/v1/Schema'

    def build_document_schema_version(self) -> None:
        self._invoice.document_schema_version = '1.0'

    def build_document_schema_location(self) -> None:
        self._invoice.document_schema_location = 'https://www.dian.gov.co/contratos/facturaelectronica/v1/Schema/facturaElectronica.xsd'

    def build_document_signature(self) -> None:
        self._invoice.document_signature = 'Signature'

    def build_document_signature_version(self) -> None:
        self._invoice.document_signature_version = '1.0.0'

    def build_document_signature_schema(self) -> None:
        self._invoice.document_signature_schema = 'http://www.w3.org/2000/09/xmldsig#'

    def build_document_signature_schema_version(self) -> None:
        self._invoice.document_signature_schema_version = '1.0'

    def build_document_signature_method(self) -> None:
        self._invoice.document_signature_method = 'SignatureMethod'

    def build_document_signature_method_version(self) -> None:
        self._invoice.document_signature_method_version = '1.0.0'

    def build_document_signature_method_schema(self) -> None:
        self._invoice.document_signature_method_schema = 'http://www.w3.org/2000/09/xmldsig#rsa-sha1'

    def build_document_signature_method_transform(self) -> None:
        self._invoice.document_signature_method_transform = 'Transform'

    def build_document_signature_method_transform_version(self) -> None:
        self._invoice.document_signature_method_transform_version = '1.0.0'


class CreditNoteBuilder(DocumentBuilder):
    """
    Construye un objeto CreditNote usando la interfaz DocumentBuilder.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._credit_note = CreditNote()

    @property
    def document(self) -> CreditNote:
        document = self._credit_note
        self.reset()
        return document

    def build_document(self) -> None:
        self._credit_note.document = 'CreditNote'

    def build_document_name(self) -> None:
        self._credit_note.document_name = 'Nota de crédito'

    def build_document_type(self) -> None:
        self._credit_note.document_type = '04'

    def build_document_version(self) -> None:
        self._credit_note.document_version = '1.0.0'

    def build_document_schema(self) -> None:
        self._credit_note.document_schema = 'https://www.dian.gov.co/contratos/facturaelectronica/v1/Schema'

    def build_document_schema_version(self) -> None:
        self._credit_note.document_schema_version = '1.0'

    def build_document_schema_location(self) -> None:
        self._credit_note.document_schema_location = 'https://www.dian.gov.co/contratos/facturaelectronica/v1/Schema/facturaElectronica.xsd'

    def build_document_signature(self) -> None:
        self._credit_note.document_signature = 'Signature'

    def build_document_signature_version(self) -> None:
        self._credit_note.document_signature_version = '1.0.0'

    def build_document_signature_schema(self) -> None:
        self._credit_note.document_signature_schema = 'http://www.w3.org/2000/09/xmldsig#'

    def build_document_signature_schema_version(self) -> None:
        self._credit_note.document_signature_schema_version = '1.0'

    def build_document_signature_method(self) -> None:
        self._credit_note.document_signature_method = 'SignatureMethod'

    def build_document_signature_method_version(self) -> None:
        self._credit_note.document_signature_method_version = '1.0.0'

    def build_document_signature_method_schema(self) -> None:
        self._credit_note.document_signature_method_schema = 'http://www.w3.org/2000/09/xmldsig#rsa-sha1'

    def build_document_signature_method_transform(self) -> None:
        self._credit_note.document_signature_method_transform = 'Transform'


class DebitNoteBuilder(DocumentBuilder):
    """
    Construye un objeto DebitNote usando la interfaz DocumentBuilder.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._debit_note = DebitNote()

    @property
    def document(self) -> DebitNote:
        document = self._debit_note
        self.reset()
        return document

    def build_document(self) -> None:
        self._debit_note.document = 'DebitNote'

    def build_document_name(self) -> None:
        self._debit_note.document_name = 'Nota de débito'

    def build_document_type(self) -> None:
        self._debit_note.document_type = '05'

    def build_document_version(self) -> None:
        self._debit_note.document_version = '1.0.0'

    def build_document_schema(self) -> None:
        self._debit_note.document_schema = 'https://www.dian.gov.co/contratos/facturaelectronica/v1/Schema'

    def build_document_schema_version(self) -> None:
        self._debit_note.document_schema_version = '1.0'

    def build_document_schema_location(self) -> None:
        self._debit_note.document_schema_location = 'https://www.dian.gov.co/contratos/facturaelectronica/v1/Schema/facturaElectronica.xsd'

    def build_document_signature(self) -> None:
        self._debit_note.document_signature = 'Signature'

    def build_document_signature_version(self) -> None:
        self._debit_note.document_signature_version = '1.0.0'

    def build_document_signature_schema(self) -> None:
        self._debit_note.document_signature_schema = 'http://www.w3.org/2000/09/xmldsig#'

    def build_document_signature_schema_version(self) -> None:
        self._debit_note.document_signature_schema_version = '1.0'

    def build_document_signature_method(self) -> None:
        self._debit_note.document_signature_method = 'SignatureMethod'

    def build_document_signature_method_version(self) -> None:
        self._debit_note.document_signature_method_version = '1.0.0'

    def build_document_signature_method_schema(self) -> None:
        self._debit_note.document_signature_method_schema = 'http://www.w3.org/2000/09/xmldsig#rsa-sha1'

    def build_document_signature_method_transform(self) -> None:
        self._debit_note.document_signature_method_transform = 'Transform'


class SupportDocumentBuilder(DocumentBuilder):
    """
    Construye un objeto SupportDocument usando la interfaz DocumentBuilder.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._support_document = SupportDocument()

    @property
    def document(self) -> SupportDocument:
        document = self._support_document
        self.reset()
        return document

    def build_document(self) -> None:
        self._support_document.document = 'SupportDocument'

    def build_document_name(self) -> None:
        self._support_document.document_name = 'Documento soporte'

    def build_document_type(self) -> None:
        self._support_document.document_type = '06'

    def build_document_version(self) -> None:
        self._support_document.document_version = '1.0.0'

    def build_document_schema(self) -> None:
        self._support_document.document_schema = 'https://www.dian.gov.co/contratos/facturaelectronica/v1/Schema'

    def build_document_schema_version(self) -> None:
        self._support_document.document_schema_version = '1.0'

    def build_document_schema_location(self) -> None:
        self._support_document.document_schema_location = 'https://www.dian.gov.co/contratos/facturaelectronica/v1/Schema/facturaElectronica.xsd'

    def build_document_signature(self) -> None:
        self._support_document.document_signature = 'Signature'

    def build_document_signature_version(self) -> None:
        self._support_document.document_signature_version = '1.0.0'

    def build_document_signature_schema(self) -> None:
        self._support_document.document_signature_schema = 'http://www.w3.org/2000/09/xmldsig#'

    def build_document_signature_schema_version(self) -> None:
        self._support_document.document_signature_schema_version = '1.0'

    def build_document_signature_method(self) -> None:
        self._support_document.document_signature_method = 'SignatureMethod'

    def build_document_signature_method_version(self) -> None:
        self._support_document.document_signature_method_version = '1.0.0'

    def build_document_signature_method_schema(self) -> None:
        self._support_document.document_signature_method_schema = 'http://www.w3.org/2000/09/xmldsig#rsa-sha1'

    def build_document_signature_method_transform(self):
        self._support_document.document_signature_method_transform = 'Transform'


class CreditNoteSupportDocumentBuilder(DocumentBuilder):
    """
    Construye un objeto CreditNoteSupportDocument usando la interfaz DocumentBuilder.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._credit_note_support_document = CreditNoteSupportDocument()

    @property
    def document(self) -> CreditNoteSupportDocument:
        document = self._credit_note_support_document
        self.reset()
        return document

    def build_document(self) -> None:
        self._credit_note_support_document.document = 'CreditNoteSupportDocument'

    def build_document_name(self) -> None:
        self._credit_note_support_document.document_name = 'Documento soporte de nota de crédito'

    def build_document_type(self) -> None:
        self._credit_note_support_document.document_type = '07'

    def build_document_version(self) -> None:
        self._credit_note_support_document.document_version = '1.0.0'

    def build_document_schema(self) -> None:
        self._credit_note_support_document.document_schema = 'https://www.dian.gov.co/contratos/facturaelectronica/v1/Schema'

    def build_document_schema_version(self) -> None:
        self._credit_note_support_document.document_schema_version = '1.0'

    def build_document_schema_location(self) -> None:
        self._credit_note_support_document.document_schema_location = 'https://www.dian.gov.co/contratos/facturaelectronica/v1/Schema/facturaElectronica.xsd'

    def build_document_signature(self) -> None:
        self._credit_note_support_document.document_signature = 'Signature'

    def build_document_signature_version(self) -> None:
        self._credit_note_support_document.document_signature_version = '1.0.0'

    def build_document_signature_schema(self) -> None:
        self._credit_note_support_document.document_signature_schema = 'http://www.w3.org/2000/09/xmldsig#'

    def build_document_signature_schema_version(self) -> None:
        self._credit_note_support_document.document_signature_schema_version = '1.0'

    def build_document_signature_method(self) -> None:
        self._credit_note_support_document.document_signature_method = 'SignatureMethod'

    def build_document_signature_method_version(self) -> None:
        self._credit_note_support_document.document_signature_method_version = '1.0.0'

    def build_document_signature_method_schema(self) -> None:
        self._credit_note_support_document.document_signature_method_schema = 'http://www.w3.org/2000/09/xmldsig#rsa-sha1'


class PayrollDocumentBuilder(DocumentBuilder):
    """
    Construye un objeto PayrollDocument usando la interfaz DocumentBuilder.
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._payroll_document = PayrollDocument()

    @property
    def document(self) -> PayrollDocument:
        document = self._payroll_document
        self.reset()
        return document

    def build_document(self) -> None:
        self._payroll_document.document = 'PayrollDocument'

    def build_document_name(self) -> None:
        self._payroll_document.document_name = 'Documento soporte de nómina'

    def build_document_type(self) -> None:
        self._payroll_document.document_type = '08'

    def build_document_version(self) -> None:
        self._payroll_document.document_version = '1.0.0'

    def build_document_schema(self) -> None:
        self._payroll_document.document_schema = 'https://www.dian.gov.co/contratos/facturaelectronica/v1/Schema'

    def build_document_schema_version(self) -> None:
        self._payroll_document.document_schema_version = '1.0'

    def build_document_schema_location(self) -> None:
        self._payroll_document.document_schema_location = 'https://www.dian.gov.co/contratos/facturaelectronica/v1/Schema/facturaElectronica.xsd'

    def build_document_signature(self) -> None:
        self._payroll_document.document_signature = 'Signature'

    def build_document_signature_version(self) -> None:
        self._payroll_document.document_signature_version = '1.0.0'

    def build_document_signature_schema(self) -> None:
        self._payroll_document.document_signature_schema = 'http://www.w3.org/2000/09/xmldsig#'

    def build_document_signature_schema_version(self) -> None:
        self._payroll_document.document_signature_schema_version = '1.0'

    def build_document_signature_method(self) -> None:
        self._payroll_document.document_signature_method = 'SignatureMethod'

    def build_document_signature_method_version(self) -> None:
        self._payroll_document.document_signature_method_version = '1.0.0'

    def build_document_signature_method_schema(self) -> None:
        self._payroll_document.document_signature_method_schema = 'http://www.w3.org/2000/09/xmldsig#rsa-sha1'




Ambiente = {
    '1': '1 - Produccion',
    '2': '2 - Pruebas',
}


TipoDocumento = {
    '11': '11 - Registro civil',
    '12': '12 - Tarjeta de identidad',
    '13': '13 - Cédula de ciudadanía',
    '21': '21 - Tarjeta de extranjería',
    '22': '22 - Cédula de extranjería',
    '31': '31 - NIT',
    '41': '41 - Pasaporte',
    '42': '42 - Documento de identificación extranjero',
    '47': '47 - PEP',
    '50': '50 - NIT de otro país',
    '91': '91 - NUIP * ',
}


class Dianbase():

    @classmethod
    def compute_check_digit(cls, rut: str, identification_type: str) -> str:
        """
        @param rut(str): Rut without check digit
        @param identification_type(str): Identification type

        @return result(str): Return the check digit of the rut
        """
        result = 0
        if identification_type == '31':
            factor = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]
            rut_ajustado=str(rut).rjust( 15, '0')
            total = sum(int(rut_ajustado[14-i]) * factor[i] for i in range(14)) % 11
            if total > 1:
                result =  11 - total
            else:
                result = total
        else:
            result = 0

        return result