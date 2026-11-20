import requests as rq
import pandas as pd
import csv 
import json
from datetime import datetime,timedelta
import time
from sqlalchemy import text
from fastapi import WebSocket,WebSocketDisconnect

from  fastapi import FastAPI,APIRouter,HTTPException,status,Depends,BackgroundTasks,Request
from typing import List,Annotated
from sqlmodel import select,desc
from fastapi.responses import JSONResponse
from sqlmodel import SQLModel
#from models import ORDERPLACING,USERVERIFY,USERACCOUNT,TOKENS,DATASET,WEB
from concurrent.futures import ProcessPoolExecutor
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
#from schemas import USERDATABASE,ORDER_DATABASE,STRADLLE_ORDER_DATABASE
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer,oauth2
import random
from sqlalchemy.orm import sessionmaker
import jwt
from redis.asyncio import Redis 
import redis
import websockets 
from redis.asyncio import Redis
import asyncio
import httpx

notifications_app=FastAPI()

router=APIRouter()
@notifications_app.on_event('startup')

async def startup():
    notifications_app.state.redis=Redis(host='localhost',port=6379,decode_responses=True)
    





class NOTIFICATIONS:



    async def getting_the_master_data(self,order:dict,session:AsyncSession):


        main_orders=order

        for ord in main_orders:

            stock_name=ord['STOCK_NAME']
            new_order={
                'STOCK_NAME':ord['STOCK_NAME'],
                'LTP':ord['LTP']
            }









        





