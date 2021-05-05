import json
import logging
import time
from datetime import datetime

import pytz
import requests

# get the standard UTC time
UTC = pytz.utc

# it will get the time zone
# of the specified location
IST = pytz.timezone('Asia/Kolkata')

logging.basicConfig(filename='/home/ec2-user/output.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('Loading function.')

pin_codes = ['411027']

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}'

telegram_token = 'update me'

telegram_url = f"https://api.telegram.org/bot{telegram_token}"

chat_ids = ['update me']

while True:
    output = []
    try:

        for pin_code in pin_codes:
            response = requests.get(url.format(pin_code, datetime.now(IST).strftime('%d-%m-%Y')))

            if response.ok:

                jData = json.loads(response.content)

                for center in jData['centers']:
                    for session in center['sessions']:
                        if (session['available_capacity'] > 0) and (session['min_age_limit'] == 18):
                            output.append(
                                f"date : {session['date']} , center : {center['name']} , availability : {session['available_capacity']}, pin_code : {pin_code}, min_age_limit : {session['min_age_limit']}")
        if len(output) > 0:
            logger.info(output)
            for chat_id in chat_ids:
                params = {"chat_id": chat_id, "text": str(output)}
                r = requests.get(telegram_url + "/sendMessage", params=params)
        else:
            logger.info("No vaccines available")

    except Exception as e:
        logger.error(e)

    time.sleep(30)
