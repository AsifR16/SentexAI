from etl.loaders.BaseLoader import BaseLoader

class BankLoader(BaseLoader):
  def __init__(self):
    super().__init__("data/raw/HI-Small_accounts.csv")