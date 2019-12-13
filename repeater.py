import schedule
import time
from telstra_msg import SMSender
from datetime import datetime
from threading import Timer

class Repeater():

    # repeat after is in days.
    def add_repeat_sequence(self, date_from=datetime.today(),\
         repeat_after_days=1, at_time="09:30", msg="This is your alarm!!", to="0444444444"):


        right_now = int(datetime.today().timestamp())
        date_from = int(date_from.timestamp())

        if date_from < today:
            raise ValueError("date_from cannot be before today")
        else:
            time_diff = date_from - right_now

            t = Timer(time_diff, self.set_alarm, [repeat_after_days, at_time, msg, to])
            t.start()


    def set_alarm(self, day_diff, time_alarm, msg, to):

        self.send_alarm(msg, to)

        if day_diff <= 1:
            schedule.every().day.at(time_alarm).do(self.send_alarm, msg, to)
        else:
            schedule.every(day_diff).days.at(time_alarm).do(self.send_alarm, msg, to)

    
    def send_alarm(self, msg, to):
        sender = SMSender()
        sender.authenticate_client()
        sender.provision_client()
        sender.send_sms(to, msg)
        print("Alarm successfully sent!")
       

if __name__ == "__main__":
    
    repeat = Repeater()
    starting_date = datetime.today()
    repeat.add_repeat_sequence(date_from=starting_date, repeat_after_days=14, msg="Time to dance!", \
        to="+61444444444")

    while True:
        schedule.run_pending()
        time.sleep(1)



