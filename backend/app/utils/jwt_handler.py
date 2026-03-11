from jose import jwt 
from datetime import datetime,timedelta,timezone
from dotenv import load_dotenv

import os

load_dotenv()

SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM=os.getenv('ALGORITHM')

def create_access_token(data:dict):
    to_encode=data.copy()

    expire=datetime.now(timezone.utcnow)+timedelta(hours=2)

    to_encode.update({'exp':expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
