import pandas as pd
from etl.common.logger import success_log, error_log

class Validate():
  
  def build_rules(self,column_dict):
    rules = {}
    for key, value in column_dict.items():
      rules[key] = value.split()
    return rules
  
  def validate_data(self,dataframe, column_dict):
    rules = self.build_rules(column_dict)
    try:
      for key, value in rules.items():
        result = {key: []} 
        if ("required" in value):
          is_missing = dataframe[key].isna() | dataframe[key].astype(str).str.strip().eq('')
          result[key].append(not (is_missing.any()))

        if ("unique" in value):
          is_un = dataframe[key].is_unique
          result[key].append(is_un)

        if(False in result[key]):
          error_log(f"Column {key} cannot be validated.")
          raise Exception()
        success_log(f"Column {key} is successfully validated.")
    except Exception as e:
      error_log(f"Data validation error. Check validation rules!\n\n{e}")