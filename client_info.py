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



@notifications_app.on_event('shutdown')
async def shutdown_event():
    await notifications_app.state.redis.close()


redis_client=redis.Redis(host='localhost',port='6379',decode_responses=True)






class NOTIFICATIONS:



    async def getting_the_master_data(self,order:list[dict],session:AsyncSession):



        main_orders=order


        for orders in main_orders:
            stock_name=orders['STOCK_NAME']
            current_ltp=orders['LTP']
            ws_object=orders['WEBSOCKET_OBJECT']



        new_order_set={
            'STOCK_NAME':stock_name,
            'LTP':current_ltp,
            'WEBSOCKET_OBJECT':ws_object
        }


        await notifications_app.state.redis.set('client_order_history',json.dumps(new_order_set),ex=3600)
        await notifications_app.state.redos.publish('notifications_data',json.dumps(new_order_set))


    async def the_main_subsriber(self):



        main_input=notifications_app.state.redis.pubsub()
        await main_input.subscribe(main_input)

        async for incli in main_input.listen():
            main_responses=incli
            data_load=json.loads(main_responses)


            for m in data_load:
                client_webscoket_object=m['WEBSOCKET_OBJECT']
                stock_name=m['STOCK_NAME']
                entry_price=m['ENTRY_PRICE']

            main_info={
                'YOUR_STOCK':stock_name,
                'ENTRY_PRICE':entry_price
            }

            await client_webscoket_object.send_json(main_info)


            


        
n=NOTIFICATIONS()
@router.websocket('/client/live/data/')


async def placing_the_orders(websocket:WebSocket,session:AsyncSession):

    order_database=[]
    client_mssgs=await websocket.receive_text()


    if client_mssgs:
        mssg_loading=json.loads(client_mssgs)


        for m in mssg_loading:
            stock_names=m['STOCK_NAME']
            entry_price=m['ENTRY_PRICE']

        latest_orders={
            'STOCK_NAME':stock_names,
            'ENTRY_PRICE':entry_price,
            'CLIENT_WEBSOCKET_OBJECT':websocket
        }

        order_database.append(latest_orders)
    engine_response=await n.getting_the_master_data(order_database)


    if engine_response is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,details='UNABLE TO PROCESS THE ORDERS')

notifications_app.include_router(router)










            
























        





