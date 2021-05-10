drive = input('請問你有沒有開過車?')
if drive != '有' and drive != '沒有':
    print('不要亂回答!!!')
    raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if drive == '有':
    if age >= 18:
        print('你合格了!')
    else:
        print('你違法了!!')
elif drive == '沒有':
    if age >= 18:
        print('你幹嘛不去考駕照!!')
    else:
        print('跟你沒甚麼好說的!!')