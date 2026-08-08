from etl.loaders.BaseLoader import BaseLoader

class BankLoader(BaseLoader):
  def __init__(self):
    super().__init__("data/raw/HI-Small_accounts.csv")


    self.column_list = ["Bank ID","Bank Name"]
    self.column_rules = {"Bank ID":"unique required","Bank Name":"required"}
    self.table_data = {
      "name":"banks",
      "mapper":{
        "bank_id":"Bank ID",
        "bank_name":"Bank Name"
      }
    }

bank_loader = BankLoader()