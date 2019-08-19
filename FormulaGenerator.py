# 配方生成器_20190818
# -----------------------------------------------------------
import random
import tkinter

typeSet = (
    "Role Play",
    "Shooter",
    "Action",
    "Adventage",
    "Race",
    "Simulation",
    "Sports",
    "Music",
    "Fight",
    "Puzzle",
    "Strategy",
    "Table",
)
imagerySet = (
    "树木",
    "花草",
    "雨",
    "云",
    "月",
    "水",
    "日",
    "烟",
    "雪",
    "桥",
    "镜",
    "灯",
    "鼠",
    "牛",
    "虎",
    "兔",
    "龙",
    "蛇",
    "马",
    "羊",
    "猴",
    "鸡",
    "狗",
    "猪",
    "狮子",
    "熊",
    "象",
    "狼",
    "鹿",
    "猫",
    "鱼",
    "龟",
    "鹰",
    "鸽",
    "积木",
    "眼",
    "天秤",
    "钥匙",
    "轮",
    "锡杖",
    "首饰",
    "火",
    "风",
    "雷电",
    "载具",
    "城堡",
    "山",
    "星星",
    "颜色",
    "飞行",
)
elementSet = (
    "排行",
    "随机",
    "团队",
    "社交",
    "压力",
    "竞争",
    "探索",
    "选择",
    "收集",
    "解锁",
    "创造",
    "联机",
    "博弈",
    "回合",
    "实时",
    "永久死亡",
    "时间",
    "神话",
    "科幻",
    "奇幻",
    "中古",
    "现代",
    "战争",
    "怪物",
    "修仙",
    "武侠",
    "潜行",
    "消除",
    "组合",
    "布置",
    "平衡",
    "投掷",
    "拼图",
    "数学",
    "迷宫",
    "驾驶",
    "休闲",
    "生存",
    "指向",
    "节奏",
    "战术",
    "物理",
    "清版",
    "管理",
    "隐藏",
    "极简",
    "塔防",
    "剧情",
    "风格",
    "逻辑",
    "灵异",
    "反应",
)

# -----------------------------------------------------------
def Func():
    type1.set(random.choice(list(typeSet)))
    type2.set(random.choice(list(typeSet)))
    imagery.set(random.choice(list(imagerySet)))
    elementList = list(elementSet)
    element1.set(random.choice(elementList))
    element2.set(random.choice(elementList))
    element3.set(random.choice(elementList))


root = tkinter.Tk()
root.title("FormulaGenerator")
root.geometry("600x150")
root.resizable(False, False)

frame1 = tkinter.Frame(root)

type1Title = tkinter.Label(frame1, text="Type1", width=12, height=2)
type1Title.grid(row=0, column=0)

type2Title = tkinter.Label(frame1, text="Type2", width=12, height=2)
type2Title.grid(row=0, column=1)

imageryTitle = tkinter.Label(frame1, text="Imagery", width=12, height=2)
imageryTitle.grid(row=0, column=2)

element1Title = tkinter.Label(frame1, text="Element1", width=12, height=2)
element1Title.grid(row=0, column=3)

element2Title = tkinter.Label(frame1, text="Element2", width=12, height=2)
element2Title.grid(row=0, column=4)

element3Title = tkinter.Label(frame1, text="Element3", width=12, height=2)
element3Title.grid(row=0, column=5)

type1 = tkinter.StringVar()
type1.set("-")
type1Value = tkinter.Label(frame1, textvariable=type1, width=12, height=2)
type1Value.grid(row=1, column=0)

type2 = tkinter.StringVar()
type2.set("-")
type2Value = tkinter.Label(frame1, textvariable=type2, width=12, height=2)
type2Value.grid(row=1, column=1)

imagery = tkinter.StringVar()
imagery.set("-")
imageryValue = tkinter.Label(frame1, textvariable=imagery, width=12, height=2)
imageryValue.grid(row=1, column=2)

element1 = tkinter.StringVar()
element1.set("-")
element1Value = tkinter.Label(frame1, textvariable=element1, width=12, height=2)
element1Value.grid(row=1, column=3)

element2 = tkinter.StringVar()
element2.set("-")
element2Value = tkinter.Label(frame1, textvariable=element2, width=12, height=2)
element2Value.grid(row=1, column=4)

element3 = tkinter.StringVar()
element3.set("-")
element3Value = tkinter.Label(frame1, textvariable=element3, width=12, height=2)
element3Value.grid(row=1, column=5)

frame1.pack()
frame2 = tkinter.Frame(root)

btn = tkinter.Button(frame2, text="Generate", command=Func)
btn.pack()

frame2.pack(side=tkinter.BOTTOM, pady=10)

root.mainloop()

