from pydantic import BaseModel
import uuid
from sqlmodel import create_engine,text,SQLModel,Field,Column
from typing import Optional,List