import schedule
import time
import subprocess
from datetime import datetime, timedelta
import logging
import random

# Configure logging
logging.basicConfig(filename='uscbeach61_execution.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def job():
    logging.info(f'Starting uscbeach61.py at {datetime.now()}')
    subprocess.call(['python', 'uscbeach61.py']) # replace the script with your own gemini script
    logging.info(f'Finished uscbeach61.py at {datetime.now()}')

# Define the start time as 20:00 on the current day (zou can replace anything in24 hour format )
start_time = datetime.combine(datetime.now(), datetime.strptime('04:16', '%H:%M').time())
logging.info(f'Start time: {start_time}')
print(start_time)
# Calculate the target time as 8 hours after the start time
target_time = start_time + timedelta(hours=10) #Running from the start time plus 8 hours
logging.info(f'target time: {target_time}')
print(target_time)
# Continuously check the current time against the start and target times
while True:
    current_time = datetime.now()
    if current_time > start_time and current_time < target_time:
        logging.info(f'Current time: {current_time}')
        # Schedule the job to run every 5 minutes
        schedule.every(10).to(20).minutes.do(job)
        # Run the job immediately
        job()
        # Run the scheduler until the target time is reached
        while datetime.now() < target_time:
            schedule.run_pending()
            time.sleep(1)
        break # Exit the loop once the target time is reached
    else:
        time.sleep(1) # Wait for 1 second before checking again

print("The target time has been reached.")
