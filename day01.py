#我的第一个python文件
name=input("请输入你的名字")
goal=input("请输入你的职业目标")
weekly_hours=int(input("你每周可以投入多少时间"))

month_hours=weekly_hours*4
yearly_hours=month_hours*12

print(f"\n你好,{name}!")
print(f"你的目标是：{goal}")
print(f"你每周的投入是{weekly_hours}")
print(f"你每个月的投入是{month_hours}")
print(f"你每年的投入是{yearly_hours}")
