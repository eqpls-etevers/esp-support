# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from common import MeshControl, asleep

from service.driver.wolken import Wolken

from schema.adapter.vmware.docs import Knowledgebase
from schema.adapter.atlassian.confluence import Space, Page
from schema.adapter.wolken import Ticket


#===============================================================================
# Implement
#===============================================================================
class Control(MeshControl):

    def __init__(self, api, config):
        MeshControl.__init__(self, api, config, background=True)
        self.wolken = Wolken(
            config['wolken']['url'],
            config['wolken']['origin'],
            config['wolken']['username'],
            config['wolken']['password']
        )

    async def startup(self):
        await self.registerModel(Ticket, 'uerp')

    async def shutdown(self):
        await self.wolken.disconnect()
    
    async def syncTickets(self):
        tickets = await self.wolken.getTicketList()
        if 'data' in tickets and 'SearchResultList' in tickets['data']:
            for ticket in tickets['data']['SearchResultList']:
                ticketId = ticket['requestId']
                count = await Ticket.countModels(filter=f'ticketId:{ticketId}', archive='true')
                if count.result == 0:
                    await Ticket(
                        ticketId=ticket['requestId'],
                        title=ticket['requestDesc'],
                        username=ticket['requestedUserName'],
                        email=ticket['requestedEmail'],
                        source=ticket['sourceDesc'],
                        created=ticket['createdOn'],
                        priority=ticket['priorityName'],
                        status=ticket['requestStatus']
                    ).createModel()
    
    async def syncWolken(self):
        try:
            if not self.wolken.conneted: self.wolken.connect()
            await self.syncTickets()
        except Exception as e:
            self.wolken.disconnect()
            LOG.ERROR(e)
        else:
            LOG.INFO('wolken data is synced')
        
    
    async def background(self):
        await self.syncWolken()
        await asleep(10)

    #===========================================================================
    # Interface
    #===========================================================================
