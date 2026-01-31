from src.data.transaction import Transaction


t = Transaction(1000, 2, 'RU')
t2 = Transaction(500, 14, 'US')
print(t.to_dict())
print('Night:', t.is_night())


print(t2.to_dict())
print('Night:', t2.is_night())
