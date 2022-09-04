from nonebot import on_request, RequestSession
from nonebot import on_notice, NoticeSession
import re


def check_message1(message) -> object:
    # 正则
    pattern = re.compile(r'^[12][0-9]5\d{4} [\u4e00-\u9fa5]{2,15} [\u4e00-\u9fa50-9()]{2,15}$')
    result: object = pattern.match(message)
    return result


def check_message2(message) -> object:
    # 正则
    pattern = re.compile(r'^[12][0-9]5\d{4}-[\u4e00-\u9fa5]{2,15}-[\u4e00-\u9fa50-9()（），,]{2,15}$')
    result: object = pattern.match(message)
    return result


# 将函数注册为群成员增加通知处理器

@on_notice('group_increase')
async def _(session: NoticeSession):  # 发送欢迎消息
    await session.send('欢迎新朋友～，请按群公告的要求更改群备注')


# 将函数注册为群请求处理器
@on_request('group')
async def _(session: RequestSession):
    num1 = 819139648
    num2 = 753920893
    num3 = 753944686
    # 判断验证信息是否符合要求
    path = '0'
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
                list_name.append(str1)  # 这是选取需要读取的位数
        # with open('file.json', 'a', encoding='utf-8') as file:  # 创建一个json文件，mode设置为'a'
        #     json.dump(d, file, ensure_ascii=False)
        #     # 将字典d写入json文件中，并设置ensure_ascii = False,主要是因为汉字是ascii字符码,若不指定该参数，那么文字格式就会是ascii码
        #     file.write('\n')
        list1 = session.event.comment[15:]
        list2 = list1[0:7]
        if int(list2) % 2 == 1:
            result1 = check_message1(list1)
            result2 = check_message2(list1)
            # # if '暗号' in session.event.comment:
            if result1 is not None or result2 is not None:
                if result1 is not None:
                    str2 = str.split(list1)
                else:
                    str2 = list1.split('-')
                message = str2[0] + ' ' + str2[1]
                if message in list_name:
                    # 验证信息正确，同意入群
                    await session.approve()
                return
            if result1 is None and result2 is None:
                # 验证信息错误，拒绝入群
                await session.reject('请按要求发送验证信息,中间的间隔是单个空格哦,还有别忘记填专业')
                # 更正为留给人工处理
