class Customer:
    """顧客用クラス
    
    Attributes:
        name (str): 顧客名
        address (str): 住所
    
    """

    def __init__(self, name: str, address:str):
        self.name = name
        self.address = address