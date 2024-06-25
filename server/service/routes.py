# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from typing import Annotated, Literal, List, Any
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect, BackgroundTasks, Query
from common import getConfig, Logger, MultiTask, AsyncRest
from .controls import Control
from common import ID, ModelStatus

from schema.sample.model import Blog, Message
import httpx
import aiohttp

#===============================================================================
# SingleTone
#===============================================================================
config = getConfig('../module.conf')
Logger.register(config)
api = FastAPI(title=config['default']['title'], separate_input_output_schemas=False)
ctrl = Control(api, config)

#===============================================================================
# API Interfaces
#===============================================================================
@api.get('/test1')
async def test1():
    return await Blog.searchModels()

@api.get('/test2')
async def get_httpx():
    async with httpx.AsyncClient() as client:
        resp = await client.get('http://localhost:8081/uerp/v1/sample/model/blog')
        # print(resp.status_code)
        # print(resp.text)
    return {}

@api.get('/test3')
async def get_aiohttp():
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), raise_for_status=True) as session:
        resp = await session.get('http://localhost:8081/uerp/v1/sample/model/blog')
    return {}

