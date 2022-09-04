from nonebot import on_notice, NoticeSession


@on_notice('essence')
async def _(session: NoticeSession):  # 群文件上传提醒
    await session.send('[CQ:at,qq=all]'+' '+'请注意留心一下精华消息')