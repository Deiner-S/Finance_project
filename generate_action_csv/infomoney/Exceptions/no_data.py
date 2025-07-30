class NoData(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)  # isso define a mensagem padrão da exceção
        self.message = "Data not found"