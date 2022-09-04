import nonebot
from nonebot import on_command, CommandSession


@on_command('usage', aliases=['使用帮助', '帮助', '使用方法', 'help'])
async def _(session: CommandSession):
    # 获取设置了名称的插件列表
    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))

    arg = session.current_arg_text.strip().lower()
    if not arg:
        # 如果用户没有发送参数，则发送功能列表
        await session.send(
            '我现在支持的功能有：\n1.检查群名片\n' +
            '2.撤回禁言12小时\n' + '3.进群申请审批\n' + '4.获取天气\n'
            + '5.简易聊天\n' + '6.高程周四中午dll提醒\n' + '7.群文件上传时对群成员进行提醒\n'
            + '8.检查不在选课名单的成员')
        return

    # 如果发了参数则发送相应命令的使用帮助
    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)
