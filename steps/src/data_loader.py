import pandas as pd
from sqlalchemy import create_engine, exc

class DataLoader:
    """DataLoader class encapsulates the details of connecting to a database 
        and loading data into a pandas DataFrame.
    """

    def __init__(self,db_uri:str):
        """
        Initializes DataLoader class with a database URI and creates an SQLAlchemy engine.
        
        Args:
            db_uri (str): The database URI.
        """
        self.db_uri = db_uri,
        self.engine = create_engine("postgresql://postgres:postgrsun123@localhost:5432/RETAILPRICEDB")
        self.data = None

    def load_data(self, table_name:str) -> pd.DataFrame:
        """
        Loads data from the specified table to the dataframe, which is stored as an instance variable self.data

        Args:
            table_name: Name of the table to read from.

        Returns:
            pd.DataFrame: Data from the table.
        """
        query = "SELECT * FROM " + table_name
        try:
            self.data = pd.read_sql(query,self.engine)
            return self.data
        except Exception as e:
            raise e
    
    def get_data(self) -> pd.DataFrame:
        """
        Return the data that was loaded into the class instance.

        Returns:
            pd.DataFrame: Data from the table.
        """
        if self.data is not None:
            return self.data
        else:
            raise ValueError("No data loaded yet. Please run load_data() first.")
        