import pytest
from documento import Documento
from exception_documento_vazio import ExceptionDocumentoVazio
from exception_tamanho_documento_excedido import ExceptionTamanhoDocumentoExcedido
from enum_documento import EnumDocumento

def test_documento_formatar_documento():
    documento_testar = Documento("123-456.789", None, 11)
    documento_testar.formatarDocumento()
    assert documento_testar.documento_formatado == "123456789"

def test_documento_validar_documento_vazio():
    documento_testar = Documento("", None, 11)
    with pytest.raises(ExceptionDocumentoVazio) as excinfo:
        documento_testar.validarDocumentoVazio()

    assert "O documento está vazio" in str(excinfo.value)

def test_documento_validar_tamanho_maximo_documento():
    documento_testar = Documento("12345678901", None, 11)

    with pytest.raises(ExceptionTamanhoDocumentoExcedido) as excinfo:
        documento_testar.validarTamanhoMaximoDocumento()

    assert "O tamanho do documento foi excedido" in str(excinfo.value)

def test_documento_define_tamanho_maximo_documento():
    documento_testar_cpf = Documento("12345678901", None, EnumDocumento.CPF)
    documento_testar_outro = Documento("12345678901", None, EnumDocumento.OUTRO)
    
    assert documento_testar_cpf.DefineTamanhoMaximoDocumento() == 11

    assert documento_testar_outro.DefineTamanhoMaximoDocumento() == 0
