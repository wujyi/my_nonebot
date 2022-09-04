from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', day_of_week=3, hour='12')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=753944686,
                                 message=f'高程作业快到ddl了，请各位同学抓紧完成')
        await bot.send_group_msg(group_id=753944686,
                                 message=f'[CQ:image,file=https://i.postimg.cc/cH8T2Z7W/QQ-20220828150419.jpg]')
        await bot.set_group_whole_ban(group_id=753944686)
    except CQHttpError:
        pass


@nonebot.scheduler.scheduled_job('cron', day_of_week=4, hour='0')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.set_group_whole_ban(group_id=753944686, enable=False)
    except CQHttpError:
        pass