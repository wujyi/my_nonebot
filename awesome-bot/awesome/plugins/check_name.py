import re

import nonebot
from nonebot import on_command, CommandSession
import parse


def check_onestudent(stuBackName) -> object:
    # 正则表达式判断
    pattern = re.compile(r'^[12][0-9]5\d{4}-[国测计信大建软微新自通围电A助光][绘筑科观能安拔数I件教电信动气01][0-9源据子化]?-'
                         r'[\u4e00-\u9fa5]{2,15}$')

    # Parse判断
    # result = parse.parse("{studentNumber:d}-{classNumber}-{studentName:D}", stuBackName)

    result: object = pattern.match(stuBackName)
    return result


def check_onestudent_bot(stuBackName) -> object:
    # 正则表达式判断
    pattern = re.compile(r'^Bot-[\u4e00-\u9fa5a-z]?[\u4e00-\u9fa5a-z]?[\u4e00-\u9fa5a-z]?[\u4e00-\u9fa5a-z]?$')

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
    res = await bot.get_group_member_list(group_id=which_group_id, no_cache=True)
    list_error = ""
    for stuName in res:
        if stuName["role"] not in ["admin", "owner"]:
            result1 = check_onestudent(stuName["card"])
            result2 = check_onestudent_bot(stuName["card"])
            if result1 is None and result2 is None:
                list_error += f'[CQ:at,qq={stuName["user_id"]}]\n'
                # list_error.append(f'[CQ:at,qq={stuName["user_id"]}]')
    if len(list_error) > 0:
        # for list_stu in list_error:
        #     await session.send(list_stu)
        # print(list_error)
        await session.send(message=list_error)
        await session.send('请上述同学按要求更改群备注')
    else:
        await session.send('所有成员的群备注没问题')
