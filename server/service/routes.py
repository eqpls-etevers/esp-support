# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from fastapi import FastAPI, Request
from common import setEnvironment, getConfig, Logger
from service.views import View


#===============================================================================
# SingleTone
#===============================================================================
setEnvironment('CONFIG', getConfig('server.conf'))
Logger.register(CONFIG)
app = FastAPI(title=CONFIG['default']['title'])
view = View()


@app.on_event('startup')
async def runStartUp(): await view.startup()


@app.on_event('shutdown')
async def runShutDown(): await view.shutdown()


#===============================================================================
# API Interfaces
#===============================================================================
@app.get('/test', tags=['Test'])
async def get_test(request:Request) -> dict:
    query = request.query_params._dict
    return await view.get_test(**query)