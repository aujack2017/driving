#判斷駕駛年紀程式
country = input('請問你是哪國人：')
age = int(input('請輸入年齡：'))
if country == "台灣":
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country == '美國':
	if age <= 16:
		print('你不可以考駕照喔')
	else:
		print('可以考駕照喔')
else:
	print('國家只能輸入台灣或是美國喔')
