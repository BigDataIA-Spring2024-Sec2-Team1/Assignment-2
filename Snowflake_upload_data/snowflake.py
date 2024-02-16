#!/usr/bin/env python
import warnings
from sqlalchemy import create_engine

warnings.filterwarnings("ignore")

def main():
    user = 'rasikakole'
    password = 'Pass1234'
    account_identifier = 'sdojcsr-sw32599'
    database_name = 'rr_data'

    engine = create_engine(
        f"snowflake://{user}:{password}@{account_identifier}/"
    )

    with engine.connect() as connection:
        # Create database
        connection.execute(f"CREATE OR REPLACE DATABASE {database_name};")

        # Create table
        connection.execute("""CREATE OR REPLACE TABLE reading_details (
            title STRING,
            topic STRING,
            year STRING,
            level STRING,
            introduction STRING,
            learning_outcomes STRING,
            summary STRING,
            overview STRING
            )""")

        # Create warehouse
        connection.execute("""CREATE OR REPLACE WAREHOUSE rr_data_wh WITH
           WAREHOUSE_SIZE='X-SMALL'
           AUTO_SUSPEND = 180
           AUTO_RESUME = TRUE
           INITIALLY_SUSPENDED=TRUE;
           """)

        # Create stage and upload files
        connection.execute("USE DATABASE rr_data")
        connection.execute("""CREATE STAGE REFRESHER_READINGS DIRECTORY = ( ENABLE = true );""")
        connection.execute("""PUT file:///tmp/refresher_readings.csv @rr_data.public.refresher_readings;""")

        # Copy stage to table
        connection.execute("USE WAREHOUSE rr_data_wh")
        connection.execute("""COPY INTO reading_details
          FROM @rr_data.public.refresher_readings
          FILE_FORMAT = (type = csv field_optionally_enclosed_by='"')
          PATTERN = '.*refresher_readings.csv.gz'
          ON_ERROR = 'skip_file';""")
    
    print("Done")
    engine.dispose()

if __name__ == "__main__":
    main()
