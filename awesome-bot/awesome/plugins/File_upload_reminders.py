from nonebot import on_notice, NoticeSession


@on_notice('group_upload')
async def _(session: NoticeSession):  # 群文件上传提醒
    await session.send('[CQ:at,qq=all]'+' '+'请注意留心一下群文件哦')
