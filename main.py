import logging
import os
import sys
import smtplib

from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)
msg = MIMEMultipart()
THEMA = 'дайте доступ'
msg['Subject'] = THEMA

def send(message):

    sender = os.getenv('SENDER')
    s = 'mikushnerev@yandex.ru'
    password = os.getenv('PASSWORD')

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()

    try:
        server.login(sender, password)
        logger.info('в аккаунт вошли')
        mesg = MIMEText(message).as_string()
        server.sendmail(sender, s, f'Subject: {sub}\n{mesg}')
        logger.info('смс отправлено')
        server.quit()
    except Exception as e:
        logger.error(f'смс не отправлено\n{e}')
        server.quit()


def main():
    message = 'ку'
    send(message)


if __name__ == '__main__':
    main()