from etl.loaders.BankLoader import BankLoader

column_list = ["Bank ID","Bank Name"]
column_rules = {"Bank ID":"unique required","Bank Name":"required"}
table_data = {
  "name":"banks",
  "mapper":{
    "bank_id":"Bank ID",
    "bank_name":"Bank Name"
  }
}

bank_loader = BankLoader()
bank_loader.run_etl(column_list,column_rules,table_data)