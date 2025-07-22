class ErroExtractData(Exception):
    def __init__(self, mensagem="extract data process fail [NULL DATA or NOT DICT]"):
        super().__init__(mensagem)
    