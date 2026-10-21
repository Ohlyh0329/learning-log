orders = [
    {"id": "O1", "city": "南京", "amount": 120},
    {"id": "O2", "city": "苏州", "amount": 300},
    {"id": "O3", "city": "南京", "amount": 80},
    {"id": "O4", "city": "上海", "amount": 500},
    {"id": "O5", "city": "苏州", "amount": 150},]

print(f"订单一共有{len(orders)}")
total_orders=0
for order in orders:
    total_orders+=order["amount"]
print(f"这份订单的总金额是:{total_orders}")

stat={}

for order in orders:
    city=order["city"]

    if city not in stat:
        stat[city]={'count':0,'amount':0}

    stat[city]['count']+=1
    stat[city]['amount']+=order['amount']

for city in stat:
    print(f"\n该城市的数据统计结果是:{city}:{stat[city]['count']},{stat[city]['amount']}")


max_amount=orders[0]

for order in orders:
    if order['amount']>max_amount['amount']:
        max_amount=order

print(f'金额最大的链条是：{max_amount}')




