# -- coding: utf-8 --**
import json
import requests
from requests import Response
from nonebot import on_command, CommandSession


@on_command("news", aliases='日报')
async def news(session: CommandSession):
    res: Response = requests.get('https://api.qqsuu.cn/api/60s')

    obj = json.loads(res.text)

    img_url = obj["img_url"]

    cq = "[CQ:image,file=" + img_url + ",id=40000]"
    await session.send(cq)
