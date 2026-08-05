import pandas as pd
from etl.common.logger import success_log, error_log
from etl.common.validate import Validate
from etl.common.database import DatabaseConnection

class BaseLoader(Validate):
  def __init__(self,path):
    self.path = path
    self.table = pd.DataFrame()
  def extract_and_validate_columns(self,column_list, column_rules):
      try:
        df = pd.read_csv(self.path)
        self.table = df[column_list].drop_duplicates().reset_index(drop=True)
        success_log(f"Extracted {column_list} from {self.path}")
        self.validate_data(self.table,column_rules)
      except FileNotFoundError:
        error_log("Error: The CSV file not found.")

      except pd.errors.EmptyDataError:
        error_log("Error: The CSV file is completely empty.")

      except pd.errors.ParserError:
        error_log("Error: Parsing failed. Check for irregular columns.")

      except Exception as e:
        error_log(f"An unexpected error occurred: {e}")

  def load_database(self,table_data):
    conn = DatabaseConnection.get_connection()
    table_name = table_data["name"]
    table_mappper = table_data["mapper"]
    table_column_list = []
    dataframe_column_list = []
    for key, value in table_mappper.items():
      table_column_list.append(key)
      dataframe_column_list.append(value)

    prepared_sql = f"INSERT INTO {table_name} ({",".join(table_column_list)}) VALUES ({",".join(["?"]*len(table_column_list))});"
    data = list(self.table.itertuples(index=False,name=None))
    
    try:
      cursor = conn.cursor()
      cursor.executemany(prepared_sql,data)
      conn.commit()
      success_log(f"Successfully loaded {len(data)} rows into {table_name}.")
    except Exception as e:
      conn.rollback()
      error_log(f"Failed to load data into {table_name}: {e}")
  
  def run_etl(self,column_list,column_rules,table_data):
    self.extract_and_validate_columns(column_list,column_rules)
    self.load_database(table_data)