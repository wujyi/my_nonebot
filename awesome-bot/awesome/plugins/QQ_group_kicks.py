from nonebot import on_command, CommandSession
import nonebot
import re


def check_onestudent(stuBackName) -> object:
    # 正则表达式判断
    pattern = re.compile(r'^[12][0-9]5\d{4}-[国测计信大建软微自通围电助A光][绘筑科观安拔数I件教电信动气01][0-9据子化]?-'
                         r'[\u4e00-\u9fa5]{2,15}$')

    # Parse判断
    # result = parse.parse("{studentNumber:d}-{classNumber}-{studentName:D}", stuBackName)

    result: object = pattern.match(stuBackName)
    return result

    # 判断验证信息是否符合要求


@on_command('QQ_group_kicks', aliases=('查看非名单成员', '踢人'))
async def qq_group_kicks(session: CommandSession):
    # 获取bot对象从而获取群列表
    bot = nonebot.get_bot()
    which_group_id = session.event.group_id
    # 这种调用全都是异步调用，因此需要适当await
    res = await bot.get_group_member_list(group_id=which_group_id, no_cache=True)
    path = '0'
    num1 = 群号1
    num2 = 群号2
    num3 = 群号3
    if session.event.group_id == num1:
        # path = 'C:\\Users\\WuCuiCui\\Desktop\\bot\\awesome-bot\\awesome\\plugins\\list1.txt'
        path = '/home/ubuntu/bot/awesome-bot/awesome/plugins/list1.txt'
    if session.event.group_id == num2:
        # path = 'C:\\Users\\WuCuiCui\\Desktop\\bot\\awesome-bot\\awesome\\plugins\\list2.txt'
        path = '/home/ubuntu/bot/awesome-bot/awesome/plugins/list2.txt'
    if session.event.group_id == num3:
        # path = 'C:\\Users\\WuCuiCui\\Desktop\\bot\\awesome-bot\\awesome\\plugins\\list3.txt'
        path = '/home/ubuntu/bot/awesome-bot/awesome/plugins/list3.txt'
    if path != '0':
        list_name = []
        with open(path, 'r', encoding='utf-8') as f:  # 打开txt文件
            for line in f:
                a = line.split()
                str1 = a[0] + ' ' + a[1]
                list_name.append(str1)
        no_in_list = ""
        list_id = []
        for stuName in res:
            result = check_onestudent(stuName["card"])
            if result is None:
                continue
            if stuName["role"] not in ["admin", "owner"]:
                str2 = stuName["card"].split('-')
                message = str2[0] + ' ' + str2[2]
                if message not in list_name and str2[1] not in ['围观', '助教']:
                    no_in_list += f'[CQ:at,qq={stuName["user_id"]}]\n'
                    list_id.append(stuName["user_id"])

        if len(no_in_list) > 0:

            await session.send(message=no_in_list)
            await session.send('上述同学不在群名单中')
            for kick_id in list_id:
                await  bot.set_group_kick(group_id=session.event.group_id,user_id=kick_id)
        else:
            await session.send('群成员均在群名单中')
