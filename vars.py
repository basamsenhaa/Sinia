#𝐒нɑᎥ𝚝ɑη
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "20100739"))
API_HASH = environ.get("API_HASH", "3c15b7b5ded9f13b4fb269cfd796a639")
BOT_TOKEN = environ.get("BOT_TOKEN", "7606847523:AAEbbNUmQnQXJU0e0_W7oRr0B_iS7_iDGRA")
OWNER = int(environ.get("OWNER", "6749667797"))
CREDIT = "𝐒нɑᎥ𝚝ɑη"
AUTH_USER = os.environ.get('AUTH_USERS', '6749667797').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

