from US_Visa.configuration.mongo_db_connection import MongoDBClient
from US_Visa.constants import DATABASE_NAME
from US_Visa.exception import USvisaException
import pandas as pd
import sys
from typing import Optional
import numpy as np


class USvisaData:
    """
    This class helps export MongoDB records as a pandas DataFrame
    """

    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise USvisaException(e, sys)

    def export_collection_as_dataframe(
        self, collection_name: str, database_name: Optional[str] = None
    ) -> pd.DataFrame:

        try:

            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client.client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))

            # remove MongoDB internal id
            if "_id" in df.columns:
                df = df.drop(columns=["_id"])

            # replace 'na' strings with NaN
            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise USvisaException(e, sys)