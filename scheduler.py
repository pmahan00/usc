import schedule
import time
import subprocess
from datetime import datetime, timedelta

def job():
    subprocess.call(['python', 'uscbasic.py'])

# Schedule the job to run every 30 minutes
schedule.every(30).minutes.do(job)

# Calculate the end time for the scheduling
end_time = datetime.now().replace(hour=7, minute=0, second=0, microsecond=0)

# Run the scheduler until the end time
while datetime.now() < end_time:
    schedule.run_pending()
    time.sleep(1)
