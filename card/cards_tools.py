card_list = []
def show_menu():
	print("*" * 50)
	print("欢迎使用名片功能")
	print("1.新增名片")
	print("2.显示所有名片")
	print("3.查询名片")
	print("*" * 50)

def new_card():
	print("-" * 50)
	print("新增名片")

	name = input("输入姓名：")
	phone= input("输入电话：")
	email = input("输入邮箱：")

	card_dict = {
				'name': name,
				'phone': phone,
				'email': email
				}

	card_list.append(card_dict)

	print(card_list)
	print("添加 %s 完成!" % name)

def show_all():
	print("-" * 50)
	print("显示所有名片")

	if len(card_list) ==0:
		print("现无名片")
		return

	for name in ["姓名","电话","邮箱"]:
		print(name, end='\t\t')
	print(' ')
	print('-' * 50)
	for card in card_list:
		# print(card['name'],end='\t\t')
		# print(card['phone'],end='\t\t')
		# print(card['email'],end='\t\t')

		print('%s\t\t%s\t\t%s' % (card['name'],card['phone'],card['email']))

def search_card():
	print("-" * 50)
	print("查询名片")
	find_name = input("输入搜索的姓名：")
	for card_dict in card_list:
		if card_dict['name'] == find_name:
			print("姓名\t\t电话\t\t邮箱")
			print('-' * 50)
			print('%s\t\t%s\t\t%s' % (card_dict['name'],card_dict['phone'],card_dict['email']))
			deal_card(card_dict)
			break
	else:
		print("未找到")

def deal_card(find_dict):
	print(find_dict)

	action_str = int(input("输入要执行的操作：【1】修改 【2】删除 【3】返回主菜单"))

	if action_str == 1:
		find_dict['name'] = input_card_info(find_dict['name'], "输入姓名(回车不修改)：")
		find_dict['phone'] = input_card_info(find_dict['phone'], "输入电话(回车不修改)：")
		find_dict['email'] = input_card_info(find_dict['email'], "输入邮箱(回车不修改)：")

		print("修改完成")
	elif action_str == 2:
		card_list.remove(find_dict)
		print("删除完成")

#重定义input
def input_card_info(dict_value, tip):
	result_str = input(tip)
	if len(result_str) > 0:
		return result_str
	else:
		return dict_value
