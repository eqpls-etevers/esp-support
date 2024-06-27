# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from typing import Annotated, Literal, List, Any
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, BackgroundTasks, Query, Depends
from common import getConfig, Logger, MultiTask, AsyncRest
from .controls import Control
from common import ID, ModelStatus

from schema.sample.model import Blog, Message

#===============================================================================
# SingleTone
#===============================================================================
config = getConfig('../module.ini')
Logger.register(config)
api = FastAPI(title=config['default']['title'], separate_input_output_schemas=False)
ctrl = Control(api, config)

#===============================================================================
# API Interfaces
#===============================================================================
@api.get('/test1')
async def test1():
    return await Blog.searchModels()