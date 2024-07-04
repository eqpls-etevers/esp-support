# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
import aiohttp


#===============================================================================
# Implement
#===============================================================================
class Wolken:
    
    def __init__(self, url, origin, username, password):
        self.url = url
        self.origin = origin
        self.username = username
        self.password = password
        self.session = aiohttp.ClientSession(url)
        self.connected = False
        self.headers = {'Origin': self.origin}
    
    async def connect(self):
        self.connected = False
        async with self.session.post('/account_service/authenticate', headers=self.headers, data={
                'authType': 'null',
                'username': self.username,
                'password': self.password
            }) as res:
            if res.status != 200: raise Exception(f'could not connect wolken: {res.status}')
            try: await res.json()
            except: raise Exception(f'could not connect wolken: {res.status} and unknown data')
        self.connected = True
    
    async def disconnect(self):
        try:
            if self.connected: await self.session.close()
        except: pass
        self.connected = False
    
    async def getTicketList(self):
        async with self.session.post('/dynamic_views/search/list', headers=self.headers, data={
                'data': '{"searchDetails":{"filterBy":1,"formula":"","conditionExpression":"1","validation":false,"precedence":"AND","sortByOrderByDetails":{"sortBy":"rm.request_id","orderBy":"desc"}},"searchType":6,"filterCondition":"","conditionExpression":"","precedence":"AND","columnDisplayDetails":[{"aliasName":"requestIdFormatted","attributeTypeId":0,"columnId":"rm.attribute_2","createdDate":0,"createdUserId":0,"customColumn":[{"aliasName":"requestId","columnId":"rm.request_id"},{"aliasName":"hyperLinkTeam","columnId":"rm.team_id"},{"aliasName":"hyperLinkAssignee","columnId":"rm.assigned_id"},{"aliasName":"hyperLinkRequestType","columnId":"rm.request_type_id"}],"fieldId":1,"fieldName":"Ticket ID","flex":false,"hyperLink":"1","hyperLinkParameters":{"type":"OVERLAY","newTabDetails":{"isNewTabAllowed":true,"url":"wolken/esd/case-view","params":[{"paramKey":"caseId","paramValue":"requestId"}]},"overlayDetails":{"params":[{"paramKey":"overlayNameKey","paramValue":"requestIdFormatted","isStatic":""},{"paramKey":"overlayPrimaryKey","paramValue":"requestId","isStatic":""}]}},"nonRemovable":true,"reportId":6,"sectionId":1,"sequence":0,"setId":1,"tableAllias":"rm","uiFieldName":"Ticket Id","updateConfigDetails":{"isEditable":false,"isSortable":true,"sortDetails":{"sortKey":"rm.request_id","isDefault":true},"filterDetails":{"attributeId":18}},"updatedDate":0,"updatedUserId":0,"uniqueFieldId":"11","excelDownloadable":true},{"aliasName":"requestDesc","attributeTypeId":0,"columnId":"rm.request_desc","createdDate":0,"createdUserId":0,"customColumn":"","fieldId":41,"fieldName":"Ticket Subject","flex":false,"hyperLink":"","hyperLinkParameters":"","nonRemovable":false,"reportId":6,"sectionId":1,"sequence":1,"setId":62,"tableAllias":"rm","uiFieldName":"Subject","updateConfigDetails":"","updatedDate":0,"updatedUserId":0,"uniqueFieldId":"141","excelDownloadable":true},{"aliasName":"requestedUserName","attributeTypeId":0,"columnId":"requester.user_fname","createdDate":0,"createdUserId":0,"customColumn":[{"aliasName":"requestedUserId","columnId":"rm.req_by"},{"aliasName":"requestedLName","columnId":"requester.user_lname"},{"aliasName":"requestedEmail","columnId":"requester.user_ps_no"}],"fieldId":6,"fieldName":"Contact","flex":false,"hyperLink":"1","hyperLinkParameters":{"type":"ROUTE","quickInfoDetails":{"apiParams":{"methodType":"GET","paramDetails":[{"paramKey":"userId","paramValue":"requestedUserId","sequence":0}],"dataResponseKey":"user","type":"keyValue","gridDisplayName":[{"aliasName":"userMasterVO.userFullName","fieldName":"Name","hyperLink":"","hyperLinkParameters":""},{"aliasName":"userMasterVO.roleName","fieldName":"Role","hyperLink":"","hyperLinkParameters":"","type":""},{"aliasName":"userMasterVO.userEmail","fieldName":"Email","hyperLink":"","hyperLinkParameters":"","type":""},{"aliasName":"userMasterVO.primaryUnitName","fieldName":"Company","hyperLink":"","hyperLinkParameters":""},{"aliasName":"userMasterVO.managerUserName","fieldName":"Manager","hyperLink":"","hyperLinkParameters":""}],"title":"Contact"},"apiUrl":"user","overlayHeight":"45vh","overlayWidth":"70vh"},"routeDetails":{"checkForAccess":true,"routerName":"add_user","route_path":"wolken/esd/dynamic_filter/add_user","paramType":"STATE","params":[{"paramKey":"userId","paramValue":"requestedUserId"},{"paramKey":"isView","isDefault":true,"paramValue":true}]}},"nonRemovable":false,"reportId":6,"sectionId":1,"sequence":2,"setId":5,"tableAllias":"requester","uiFieldName":"Contact","updateConfigDetails":{"isEditable":false,"isSortable":true,"sortDetails":{"sortKey":"requester.user_fname","isDefault":false},"filterDetails":{"attributeId":19}},"updatedDate":0,"updatedUserId":0,"uniqueFieldId":"16","excelDownloadable":true},{"aliasName":"sourceDesc","attributeTypeId":0,"columnId":"sm.source_desc","createdDate":0,"createdUserId":0,"customColumn":"","fieldId":10,"fieldName":"Origin","flex":false,"hyperLink":"","hyperLinkParameters":"","nonRemovable":false,"reportId":6,"sectionId":1,"sequence":3,"setId":9,"tableAllias":"sm","uiFieldName":"Origin","updateConfigDetails":{"isEditable":false,"isSortable":true,"sortDetails":{"sortKey":"sm.source_desc","isDefault":false},"filterDetails":{"attributeId":12}},"updatedDate":0,"updatedUserId":0,"uniqueFieldId":"110","excelDownloadable":true},{"aliasName":"createdOn","attributeTypeId":0,"columnId":"rm.created_timestamp","createdDate":0,"createdUserId":0,"customColumn":"","fieldId":2,"fieldName":"Created On","flex":false,"hyperLink":"","hyperLinkParameters":"","nonRemovable":false,"reportId":6,"sectionId":1,"sequence":4,"setId":2,"tableAllias":"rm","uiFieldName":"Created On","updateConfigDetails":{"isEditable":false,"isSortable":true,"sortDetails":{"sortKey":"rm.created_timestamp","isDefault":false},"filterDetails":{"attributeId":14}},"updatedDate":0,"updatedUserId":0,"uniqueFieldId":"12","excelDownloadable":true},{"aliasName":"priorityName","attributeTypeId":0,"columnId":"pm.priority_name","createdDate":0,"createdUserId":0,"customColumn":"","fieldId":11,"fieldName":"Priority","flex":false,"hyperLink":"","hyperLinkParameters":"","nonRemovable":false,"reportId":6,"sectionId":1,"sequence":5,"setId":10,"tableAllias":"pm","uiFieldName":"Priority","updateConfigDetails":{"isEditable":false,"isSortable":true,"sortDetails":{"sortKey":"pm.priority_name"},"filterDetails":{"attributeId":9},"groupBy":"pm.priority_id"},"updatedDate":0,"updatedUserId":0,"uniqueFieldId":"111","excelDownloadable":true},{"aliasName":"requestStatus","attributeTypeId":0,"columnId":"rsm.status_name","createdDate":0,"createdUserId":0,"customColumn":[{"aliasName":"subStatusName","columnId":"rss.sub_status_name"}],"fieldId":12,"fieldName":"Ticket Status","flex":false,"hyperLink":"","hyperLinkParameters":"","nonRemovable":false,"reportId":6,"sectionId":1,"sequence":6,"setId":11,"tableAllias":"rsm","uiFieldName":"Status","updateConfigDetails":{"isEditable":false,"isSortable":true,"sortDetails":{"sortKey":"rsm.status_name","isDefault":false},"filterDetails":{"attributeId":4}},"updatedDate":0,"updatedUserId":0,"uniqueFieldId":"112","excelDownloadable":true}],"sortByOrderByDetails":{"sortBy":"rm.request_id","orderBy":"desc"},"mapAllTeam":true}',
                'pagination': '{"offset":0,"limit":100,"sortBy":"rm.request_id","orderBy":"desc"}'
            }) as res:
            if res.status != 200: raise Exception(f'get ticket list failed : {res.status}')
            try: return await res.json()
            except: raise Exception(f'get ticket list failed : {res.status}\n{await res.text()}')
    
    async def getTicketDetail(self, ticketId):
        async with self.session.get(f'/request/specific_request_details?requestId={ticketId}&sections=REQUEST_MASTER,SLA_EVENTASSETS,DESC_DETAIL,OTHER_INFO,SYSTEM_SPECIAL_INSTRUCTION,UNIT_SPECIAL_INSTRUCTION,ALTERNATE_CONTACT,RMA_DETAILS,RMA_LINES,REQUEST_EVENT_DETAILS,COMPONENT,REQUEST_CATEGORY_TYPE_MAPPING,EMAIL_CC,MAJOR_INCIDENT_DETAILS,REQUEST_ADDITIONAL_ATTRIBUTES,WALKUP_SCHEDULE,PRIMARY_BUNDLE,FAVORITE_CASE', headers=self.headers) as res:
            if res.status != 200: raise Exception(f'get ticket list failed : {res.status}')
            try: return await res.json()
            except: raise Exception(f'get ticket list failed : {res.status}\n{await res.text()}')
