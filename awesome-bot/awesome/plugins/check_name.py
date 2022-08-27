import json
import re
from tokenize import Name

import nonebot
import requests
from requests import Response
from nonebot import on_command, CommandSession
from aiocqhttp.message import Message
import parse


def check_onestudent(stuBackName) -> object:
    # 正则表达式判断
    pattern = re.compile(r'^[12][0-9]5\d{4}-[国测计信大软微自通电助人光][豪绘科安拔数件教电信动工气012][0-9智据子化]?[能]?-'
                         r'[\u4e00-\u9fa5]{2,15}$')

    # Parse判断
    # result = parse.parse("{studentNumber:d}-{classNumber}-{studentName:D}", stuBackName)

    result: object = pattern.match(stuBackName)
    return result


@on_command('check_name', aliases='检查群名片')
async def check_name(session: CommandSession):
    # 获取bot对象从而获取群列表
    bot = nonebot.get_bot()
    which_group_id = session.event.group_id
    # 这种调用全都是异步调用，因此需要适当await
    res = await bot.get_group_member_list(group_id=which_group_id)
    list_error = ""
    for stuName in res:
        if stuName["role"] not in ["admin", "owner"]:
            result = check_onestudent(stuName["card"])
            if result is None:
                list_error += f'[CQ:at,qq={stuName["user_id"]}] '
                # list_error.append(f'[CQ:at,qq={stuName["user_id"]}]')
    if len(list_error) > 0:
        # for list_stu in list_error:
        #     await session.send(list_stu)
        # print(list_error)
        await session.send(message=list_error)
        await session.send('请上述同学按要求更改群备注')
    else:
        await session.send('所有成员的群备注没问题')
