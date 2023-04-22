import api
import schedule
import time 

def run():
    print("hello world")


schedule.every().day.at("18:30").do(run)

while True:
    schedule.run_pending()
    time.sleep(1)