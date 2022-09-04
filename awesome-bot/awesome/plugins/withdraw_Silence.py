from nonebot import on_notice, NoticeSession
import nonebot


# on_notice 装饰器将函数包装成一个通知处理器，这里的 group_recall 表示群成员撤回消息
# 各请求对应的参数值可以参考 go-cqhttp 帮助中心的 事件 (opens new window)（或 Onebot 标准 (opens new window)）的 notice_type 字段


@on_notice('group_recall')
async def _(session: NoticeSession):
    # 获取撤回消息操作的人的qq号和该消息发送者的QQ号
    ban_id = session.event.operator_id
    send_id = session.event.user_id
    if ban_id == send_id:
        which_group_id = session.event.group_id
        bot = nonebot.get_bot()
        # 主要是获取该成员在群里面的权限及id
        res = await bot.get_group_member_info(group_id=which_group_id, user_id=ban_id)
        if res["role"] not in ["admin", "owner"]:
            await bot.set_group_ban(group_id=which_group_id, user_id=ban_id, duration=3 * 60)
            await session.send('请勿撤回消息')
        # 判断是不是管理员或者群主
        else:
            user_id = f'[CQ:at,qq={res["user_id"]}]'
            await session.send(user_id + ' 管理撤回鲨不掉，坏管理，哼哼！')
