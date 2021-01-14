from student_management import sys_module  # 调用工具函数
# 无限循环，由用户主动决定什么时候退出
while True:

    sys_module.show_menu()

    action_str = input("请选择希望执行的操作: ")
    print("你选择的操作是 %s" % action_str)
    if action_str in ["1", "2", "3", "4"]:
        if action_str == "1":
            sys_module.new_card()  # 调用功能为增添的函数
        elif action_str == "2":
            sys_module.show_all()  # 调用功能为显示全部的函数
        elif action_str == "3":
            sys_module.search_card()  # 调用功能为指定信息查找的函数
        elif action_str == "4":
            sys_module.search_name()  # 调用功能为修改的函数
    # 0退出系统
    elif action_str == "0":
        print("欢迎再次使用【宿舍管理系统】")

        break

    else:
        print("输入错误，请重新输入:")
