from etl.loaders.BaseLoader import BaseLoader

class AccountLoader(BaseLoader):
  def __init__(self):
    super().__init__("data/raw/HI-Small_accounts.csv")

    self.column_list = ["Entity ID","Bank ID","Account Number"]
    self.column_rules = {"Entity ID":"required","Bank ID":"required","Account Number":"required"}
    self.table_data = {
    "name":"accounts",
        "mapper":{
            "entity_id":"Entity ID",
            "bank_id":"Bank ID",
            "account_number":"Account Number"
        }
    }

account_loader = AccountLoader()