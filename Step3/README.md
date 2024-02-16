Database Upload:

prerequisites :
1. Install the required Python packages using pip:
    pip install sqlalchemy
2. Snowflake login Credentials
3. CSV File (Created by scrapig)


Configuration for User credentials
1. Open the file in a text editor.
2. Update the following variables with Snowflake account details:
    user: Snowflake username.
    password: Snowflake password.
    account_identifier: Snowflake account identifier.
    database_name: The name of the Snowflake database where data is to be uploaded.
3. Save and close the file.

Execution: 
    python snowflake_data_upload.py
    The script will connect to Snowflake, create a database (if it doesn't exist), create a table in the database, create a warehouse for processing data, create a stage for uploading files, upload the CSV file to the stage, and finally copy the data from the stage into the database table.

Confirmation: 
    Once the script execution is complete, you should see the message "Done" indicating that the process finished successfully.
