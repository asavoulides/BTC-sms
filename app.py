import api
import schedule
import time 

def run():
    api.send_sms(f'⭐ Bitcoin: {api.prev_change()} at {api.add_commas(api.current_price())}' )
    api.send_sms(f'⭐ {api.get_news()}')

run()
#schedule.every().day.at("14:25").do(run)

