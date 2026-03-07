import sys
import os
import pymongo
import certifi

from dotenv import load_dotenv
from US_Visa.exception import USvisaException
from US_Visa.logger import logging
from US_Visa.constants import DATABASE_NAME, MONGODB_URL_KEY

# Load environment variables
load_dotenv()

# certificate authority file (prevents TLS timeout issues)
ca = certifi.where()


class MongoDBClient:
    """
    Establish connection with MongoDB database
    """

    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:

                mongo_db_url = os.getenv(MONGODB_URL_KEY)

                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")

                MongoDBClient.client = pymongo.MongoClient(
                    mongo_db_url,
                    tlsCAFile=ca
                )

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name

            logging.info("MongoDB connection successful")

        except Exception as e:
            raise USvisaException(e, sys)