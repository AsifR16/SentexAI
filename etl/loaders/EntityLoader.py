from etl.loaders.BaseLoader import BaseLoader

class EntityLoader(BaseLoader):
  def __init__(self):
    super().__init__("data/raw/HI-Small_accounts.csv")

    self.column_list = ["Entity ID","Entity Name"]
    self.column_rules = {"Entity ID":"unique required","Entity Name":"required"}
    self.table_data = {
    "name":"entities",
        "mapper":{
            "entity_id":"Entity ID",
            "entity_name":"Entity Name"
        }
    }

entity_loader = EntityLoader()