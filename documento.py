import re
from exception_documento_vazio import ExceptionDocumentoVazio
from exception_tamanho_documento_excedido import ExceptionTamanhoDocumentoExcedido
from enum_documento import EnumDocumento

class Documento:
    def __init__(self, documento, documento_formatado, tamanho_maximo_documento):
        self.documento = documento
        self.documento_formatado = documento_formatado
        self.tamanho_maximo_documento = tamanho_maximo_documento

    def formatarDocumento(self):
        print(f"Valor inicial: '{self.documento}' ")

        self.validarDocumentoVazio()

        self.documento_formatado = self.removeCaracteres(self.documento, ['-', '.', '/'])
        self.documento_formatado = self.removeDigitosVerificadores(self.documento_formatado, 2)

    def validarDocumentoVazio(self):
         if not self.documento:
            raise ExceptionDocumentoVazio("O documento está vazio, por favor digite um documento válido.")
         
    def validarTamanhoMaximoDocumento(self):
         if self.tamanho_maximo_documento < len(self.documento):
            raise ExceptionTamanhoDocumentoExcedido("O tamanho do documento foi excedido, por favor digite um documento válido.")
        
    def DefineTamanhoMaximoDocumento(self):
        if self.tamanho_maximo_documento == EnumDocumento.CPF:
            return 11
        else:
            return 0
        
    def removeCaracteres(self, texto, *caracteres_excluir):
        texto = self.removeLetras()

        for caractere in caracteres_excluir:
            texto = texto.replace(caractere, '')

        return texto
    
    def removeLetras(self):
        resultado = self.adicionaCaracter()

        resultado = re.sub(r'[^0-9]', '', resultado)
        print("Resultado remover letras:", resultado)

        return resultado
    
    def adicionaCaracter(self):
        tamanho_maximo_documento = 11
        resultado = self.documento.zfill(tamanho_maximo_documento)
        print("Resultado adiciona caracter:", resultado)
        return resultado
    
    def removeDigitosVerificadores(self, texto, quantidade):
        if len(texto) >= quantidade:
            return texto[:-quantidade]

        return ''
        
