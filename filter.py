from snowflake.snowpark.functions import col

def filter_by_menu(session, table_name, menu_type):
  df = session.table(table_name)
  return df.filter(col("menu_type") == menu_type)
';
