import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
admin_id = int(os.getenv("ADMIN_ID"))
IP_WHITELIST = [int(os.getenv("ADMIN_ID")), int(os.getenv("DAVID_ID"))]
host = os.getenv("PGHOST")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
GROUP_ID = int(os.getenv("GROUP_ID"))
GROUP_LINK = os.getenv("GROUP_LINK")
