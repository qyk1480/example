import cards_tools

while True: 

    cards_tools.show_menu()
    action_str = int(input('选择执行操作：'))
    print("选择的操作是 [%d] " % action_str)

    if action_str in [1, 2, 3]:
        if action_str == 1:
            cards_tools.new_card()
        elif action_str == 2:
            cards_tools.show_all()
        elif action_str == 3:
            cards_tools.search_card()
    elif action_str == 0:
        break
    else:
        print("输入错误，请重新输入")
