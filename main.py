import random, schedule, time

from twilio.rest import Client
from secrets import cellphone, twilio_account, twilio_token, twilio_number

GOOD_MORNING_QUOTES = [
    "Good Morning Mackenzie! Hope You Have An Amazing Day <3",
    "Good Morning babe! Hope you slept well <3",
    "Hope you have a great day today babe, text me when you wake up!",
    "I love you so much, I know you will kill it today!",
    "I miss you, text me when you wake up babe",
    "I hope you have a great day today!",
    "I can't wait to see you! Text me when you wake up <3"
]

GOOD_EVENING_QUOTES = [
    "Good Evening Love",
    "Sleep Tight My Love!",
    "Goodnight sweetie, dream about the beauty of our relationship!",
    "Love you! I hope you dream about me tonight <3"
]


def send_message(quotes_list=GOOD_MORNING_QUOTES):

    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to=cellphone,
                           from_=twilio_number,
                           body=quote
                           )


# send a message in the morning
schedule.every().day.at("07:00").do(send_message, GOOD_MORNING_QUOTES)

# send a message in the evening
# schedule.every().day.at("20:00").do(send_message, GOOD_EVENING_QUOTES)

# testing
# schedule.every().day.at("13:55").do(send_message, GOOD_EVENING_QUOTES)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)