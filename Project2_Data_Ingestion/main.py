import schedule
import time
from datetime import datetime, timedelta
import requests
from sqlalchemy import Column, Float, Integer, MetaData, String, Table, create_engine

count = 0
engine = create_engine('sqlite:///database.db')
metadata_obj = MetaData()
pi_values = Table('pi_values', metadata_obj,
    Column('factor', Integer),
    Column('pi', Float),
    Column('time', String(60), primary_key=True)
)
sqlite_connection = engine.connect()
if not engine.dialect.has_table(sqlite_connection, 'pi_values'):  # If table don't exist, Create the database table
    pi_values.create(engine)
else:
    # Clear the table if it already exists
    delt = pi_values.delete().where(1 == 1)
    result = sqlite_connection.execute(delt)
sqlite_connection.close()

def job():
    curr_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
    global count
    api_response = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi").json()
    sqlite_connection = engine.connect()
    ins = pi_values.insert().values(factor = api_response['factor'], pi = api_response['pi'], time = api_response['time'])
    result = sqlite_connection.execute(ins)
    sqlite_connection.close()
    count += 1
    print(api_response,"\t", curr_time)

def main():
    global count
    # Schedule the job to run every minute at :00
    schedule.every().minute.at(":30").do(job)
    if count >= 60:
        schedule.clear()
        return

# Start running at the top of the hour
schedule.every().hour.at("59:50").do(main)
print("Time until start of job: ", (int(schedule.idle_seconds()/60)) , " minutes ", ((int(schedule.idle_seconds()))%60), " seconds")
while True:
    schedule.run_pending()
