from fast_bitrix24 import BitrixAsync
import asyncio


async def push_bx(data):
    webhook = "https://bitrix24.snt.kg/rest/41089/ifzljsu0o21qrhgc/"
    b = BitrixAsync(webhook)
    method = 'crm.deal.add'
    
    GET_PROBLEM = {
        'Не работает домофон': 14308,
        'Не работает камера': 14309,
        'Проблемы с магнитом': 16993,
        'Проблема с доводчиком': 16994,
        'Проблема с кнопкой выхода': 16995,
        'Закончились чип ключи': 17005
    }
    
    problem = GET_PROBLEM.get(data[5])

    params = {'fields': {
        'UF_CRM_1708493866814': data[2],
        'UF_CRM_1722838742068': data[0],
        'UF_CRM_1722838763973': f'+996{data[1]}',
        'UF_CRM_1714472575287': data[3],
        'UF_CRM_1721033133176': problem,
        'UF_CRM_1723981877150': data[6],
        'UF_CRM_1673258743852': data[7],
        'CATEGORY_ID': 66,
        'ASSIGNED_BY_ID': '87'
    }}

    test = await b.call(method, params)
    return test


test_data = {
    'address': 'Bishkek 12mkr 37d',
    'name': 'Tom',
    'num': '+996700466661',
    'ent': '3',
    'problem': 'Закончились чип ключи',
    'option_problem': '30 чипов ',
    'description': 'On tomorrow',
}

# asyncio.run(push_bx(test_data))
