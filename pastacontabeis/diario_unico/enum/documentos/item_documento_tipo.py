import enum

class ItemDocumentoTipo(enum.Enum):
    ITEM_CONTA_CONSUMO = "ITEM_CONTA_CONSUMO"
    MERCADORIA = "MERCADORIA"
    SERVICO = "SERVICO"
    COTA_CONDOMINIAL = "COTA_CONDOMINIAL"
    GUIA_IMPOSTO_RETIDO = "GUIA_IMPOSTO_RETIDO"
    DETALHE_FOLHA = "DETALHE_FOLHA"