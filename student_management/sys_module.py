# coding: utf8
import random
import json
import os


card_list = []

room_map = {
    'm': ['100', '101', '102'],
    'f': ['200', '201', '202']
}


def read():
    """读取文件"""
    global card_list
    if os.path.exists('./students.json'):
        with open("./students.json", 'r', encoding="utf8") as f:
            card_list = json.load(f)


def show_menu():
    print('*' * 50)
    print('欢迎使用【宿舍管理系统】')

    print('')
    print('1.新增学生')
    print('2.显示全部')
    print('3.搜索学生')
    print('4.修改信息')
    print('0.退出系统')
    print('*' * 50)


def input_room_info(sex='m'):
    """
    学生信息输入
    """
    choose = input("宿舍号:手动输入按'1'，自动分配按回车:")
    if choose in ['1']:
        d = input('请选择（100-102）:')
        room = d if d in room_map[sex] else None
    else:
        room = random.choice(room_map[sex])
        print("自动选择的房间号为：", room)
    room_str = input('请确认宿舍号：')
    if room_str == room:
        if room_status(room):
            print("房间{}已满".format(room))
            return
    else:
        print("抱歉，两次输入房间号不一致，请重新确认！")
        return
    print("欢迎入住{}宿舍!宿舍号:".format("男生" if sex == 'm' else '女生'), room)
    return room


def room_status(room_num):
    """
    房间是否已满监测
    """
    if len([peo for peo in filter(lambda item: item["room_str"] == room_num, card_list)]) == 4:
        return True


def new_card():
    print('-' * 50)
    print('新增学生')
    name_str = input('请输入姓名：')
    for s in card_list:
        if s["name_str"] == name_str:
            print("已存在!")
            return
    ID_str = input("学号:")
    for s in card_list:
        if s["ID_str"] == ID_str:
            print("已存在!")
            return

    while True:
        sex_str = input("请输入性别(m/f)：")
        room_info = input_room_info(sex_str)
        if room_info:
            # 使用用户输入建字典
            card_dict = {
                'name_str': name_str,
                'sex_str': sex_str,
                'ID_str': ID_str,
                'room_str': room_info
            }
            break
        else:
            print("房间号输入有误")
    # 将名片字典添加到列表中
    card_list.append(card_dict)  # 把一个字典追加到一个列表中

    # 提示用户添加成功
    print('添加 %s 的信息成功' % name_str)


def show_all():
    """显示所有学生信息"""
    print('-' * 50)
    print('显示所有学生信息')

    if len(card_list) == 0:
        print('没有当前学生信息，请确认输入或者进行添加')
        return
    for name in ["姓名", "性别", "学号", "房间号"]:
        print(name, end="\t")
    print('')
    print('=' * 50)

    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:
        # print card_dict
        print(
            '%s\t\t%s\t\t%s\t\t%s' % (card_dict['name_str'],
                                      card_dict['sex_str'],
                                      card_dict['ID_str'],
                                      card_dict['room_str']))


def search_card():
    print('-' * 50)

    print('【搜索学生信息】')

    print('1.按姓名搜索')

    print('2.按性别搜索')

    print('3.按学号搜索')

    print('4.按宿舍搜索')

    print('0.返回主菜单')

    action_str = input("请选择希望执行的操作: ")
    print("你选择的操作是 %s" % action_str)
    if action_str in ["1", "2", "3", "4", "0"]:
        if action_str == "1":
            find_name = input('请输入要搜索的姓名：')
            for card_dict in card_list:
                if card_dict['name_str'] == find_name:
                    print('姓名 性别 学号 宿舍号')

                    print('=' * 50)

                    print(
                        '%s %s %s %s' % (card_dict['name_str'],
                                         card_dict['sex_str'],
                                         card_dict['ID_str'],
                                         card_dict['room_str']))

                    break

                else:
                    print('抱歉，没有找到学生：%s' % find_name)

        elif action_str == "2":
            find_sex = input('请输入要搜索的性别(m/f)：')
            for card_dict in card_list:
                if card_dict['sex_str'] == find_sex:
                    print('姓名 性别 学号 宿舍号')

                    print('=' * 50)

                    print(
                        '%s %s %s %s' % (card_dict['name_str'],
                                         card_dict['sex_str'],
                                         card_dict['ID_str'],
                                         card_dict['room_str']))
                else:
                    show_menu()
                    print("性别格式不正确！")
        elif action_str == "3":
            find_ID = input('请输入要搜索的学号：')
            for card_dict in card_list:
                if card_dict['ID_str'] == find_ID:
                    print('姓名 性别 学号 宿舍号')

                    print('=' * 50)

                    print(
                        '%s %s %s %s' % (card_dict['name_str'],
                                         card_dict['sex_str'],
                                         card_dict['ID_str'],
                                         card_dict['room_str']))
                    break
                else:
                    print('抱歉，没有找到学号：%s' % find_ID)

        elif action_str == "4":
            find_room = input('请输入要搜索的宿舍：')
            for card_dict in card_list:
                if card_dict['room_str'] == find_room:
                    print('姓名 性别 学号 宿舍号')

                    print('=' * 50)

                    print(
                        '%s %s %s %s' % (card_dict['name_str'],
                                         card_dict['sex_str'],
                                         card_dict['ID_str'],
                                         card_dict['room_str']))
                else:
                    print('抱歉，没有找到宿舍：%s' % find_room)

        elif action_str == "0":
            pass


def search_name():
    print('-' * 50)
    print('进行学生信息的修改')
    find_name = input('请输入要修改的姓名：')
    for card_dict in card_list:
        if card_dict['name_str'] == find_name:
            print('姓名 性别 学号 宿舍号')

            print('=' * 50)

            print(
                '%s %s %s %s' % (card_dict['name_str'],
                                 card_dict['sex_str'],
                                 card_dict['ID_str'],
                                 card_dict['room_str']))
            deal_card(card_dict)
            break


def deal_card(find_dict):
    print("=" * 50)
    action_str = input('请选择要执行的操作 '
                       '[1] 修改 [2] 删除 [0] 返回主菜单:')
    if action_str == '1':
        find_dict['name_str'] = input_card_info(find_dict['name_str'], '姓名：')
        find_dict['sex_str'] = input_card_info(find_dict['sex_str'], '性别：')
        find_dict['ID_str'] = input_card_info(find_dict['ID_str'], '学号：')
        find_dict['room_str'] = input_card_info(find_dict['room_str'], '宿舍号：')

        print('修改学生信息成功！！！')

    elif action_str == '2':

        card_list.remove(find_dict)

        print('删除学生信息成功！！！')

    elif action_str == "0":
        pass


def input_card_info(dict_value, tip_message):
    """如果用户输入了内容，就返回内容，负责返回字典中原有的值"""
    # 1.提示用户输入内容
    # tip_message:输入的提示文字
    result_str = input(tip_message)
    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没有输入内容，返回‘字典中原有的值’
    else:
        # dict_value:字典中原有的值
        return dict_value


def save():
    """保存数据"""
    with open("./students.json", 'w', encoding="utf8") as f:
        json.dump(card_list, f)