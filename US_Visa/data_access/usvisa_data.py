# Data -> DF

import sys
from typing import Optional
import numpy as np
import pandas as pd

from US_Visa.configuration.mongo_db_connection import MongoDBClient
from US_Visa.constants import DATABASE_NAME
from US_Visa.exception import USvisaException


class USvisaData:
    """
    This class helps to export entire MongoDB records as a pandas DataFrame
    """

    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise USvisaException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None):
        try:
            """
            Export entire collection as DataFrame
            """

            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise USvisaException(e, sys)