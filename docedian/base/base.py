from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, validator



class DocumentBuilder(ABC):
    """
    Declara la interfaz para crear los documentos.
    """

    def __init__(self) -> None:
        self._document = None

    @abstractmethod
    def build_document(self, data: Dict) -> None:
        """
        Construye el documento. Este metodo debe recibir como parametro el documento en formato Dict.
        """
        pass


class InvoiceBuilder(DocumentBuilder):
    """
    Construye un objeto Invoice usando la interfaz DocumentBuilder.
    NOTE: Esta clase se instancia en el modulo de la aplicacion que se encarga de construir los documentos. este construye la factura con la informacion base
    """

    def __init__(self) -> None:
        super().__init__()


    @property
    def document(self) -> Invoice:
        document = self._invoice
        self.reset()
        return document

    def build_document(self, data: Dict) -> None:
        """
        Construye el documento. Este metodo debe recibir como parametro el documento en formato Dict.
        """
        return Invoice(**data)

class InvoiceHeader(BaseModel):
    """
    Clase que va a representar el esquema de los datos de la cabecera de la factura.
    """
    document: str = Field(...)
    document_name: str = Field(...)
    prefix: str = Field(...)
    number: str = Field(...)
    date: datetime = Field(...)
    currency: str = Field(...)
    exchange_rate: Optional[float] = Field(None)

class InvoiceLine(BaseModel):
    """
    Clase que va a representar el esquema de los datos de la linea de la factura.
    """
    quantity: float = Field(...)
    price: float = Field(...)
    discount: float = Field(...)
    subtotal: float = Field(...)
    total: float = Field(...)


class Document(ABC):
    """
    """
    
    @abstractmethod
    def get_document(self) -> str:
        """
        NOTE: Retorna el documento en formato XML
        """
        pass

    @abstractmethod
    def get_document_name(self) -> str:
        """
        Retorna el nombre del documento
        """
        pass

class Invoice(Document, BaseModel):
    """
    Clase que representa un documento de tipo Invoice.
    """
    # Creo que va a ser mas facil si se divide tambien por secciones a alto nivel
    # Cabecera
    # PagosFactura
    # Observaciones
    # AdquirienteFactura
    # ImpuestosFactura
    # DetalleFactura
    # ResumenImpuestosFactura
    # TotalesFactura
    header: InvoiceHeader = Field(...)
    lines: List[InvoiceLine] = Field(...)


    def get_document(self) -> str:
        """
        Retorna el documento en formato XML
        """
        return self.data.get('document')

    def get_document_name(self) -> str:
        """
        Retorna el nombre del documento
        """
        return self._data.get('document_name')



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
    
# class InvoiceSchema(BaseModel):
#     """
#     Clase que representa el esquema de la factura.
#     """

#     document: str = Field(...)
#     document_name: str = Field(...)
#     document_type: str = Field(...)
#     document_version: str = Field(...)
#     document_schema: str = Field(...)
#     document_schema_version: str = Field(...)
#     document_schema_location: str = Field(...)
#     document_signature: str = Field(...)
#     document_signature_version: str = Field(...)
#     document_signature_schema: str = Field(...)
#     document_signature_method: str = Field(...)
#     document_signature_method_version: str = Field(...)
#     document_signature_method_schema: str = Field(...)
#     document_signature_method_transform: str = Field(...)
#     document_signature_method_transform_version: str = Field(...)
#     document_signature_method_transform_schema: str = Field(...)

#     class Config:
#         """
#         Configuracion del esquema de la factura.
#         """

#         schema_extra = {
#             "example": {
#                 "document": "XML",
#                 "document_name": "invoice",
#                 "document_type": "invoice",
#                 "document_version": "1.0",
#                 "document_schema": "invoice.xsd",
#                 "document_schema_version": "1.0",
#                 "document_schema_location": "http://www.example.com/invoice.xsd",
#                 "document_signature": "XML",
#                 "document_signature_version": "1.0",
#                 "document_signature_schema": "invoice.xsd",
#                 "document_signature_method": "XML",
#                 "document_signature_method_version": "1.0",
#                 "document_signature_method_schema": "invoice.xsd",
#                 "document_signature_method_transform": "XML",
#                 "document_signature_method_transform_version": "1.0",
#                 "document_signature_method_transform_schema": "invoice.xsd"
#             }
#         }