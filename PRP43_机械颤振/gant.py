# 导入绘图库
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 定义任务数据
tasks = [
    {"name": "Start and Deside", "start": "2023-3-01", "end": "2023-3-28", "color": "lightcoral"},
    {"name": "Product draft design", "start": "2023-3-28", "end": "2023-4-08", "color": "plum"},
    {"name": "Competition", "start": "2023-3-28", "end": "2023-4-12", "color": "skyblue"},
    {"name": "Equipment purchase and product production", "start": "2023-4-27", "end": "2023-5-20", "color": "lightgreen"},
    {"name": "Final report", "start": "2023-5-20", "end": "2023-5-31", "color": "#C884A8"},
]

# 创建画布和坐标轴
fig, ax = plt.subplots(figsize=(10, 6))

# 设置日期格式
date_format = mdates.DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(date_format)

# 绘制每个任务的条形图
for i, task in enumerate(tasks):
    # 计算任务的持续时间
    duration = mdates.datestr2num(task["end"]) - mdates.datestr2num(task["start"])
    # 在坐标轴上添加条形图
    ax.barh(i + 1, duration, left=mdates.datestr2num(task["start"]), height=0.8, align="center", color=task["color"], edgecolor="black")
    # 在条形图上添加任务名称
    ax.text(mdates.datestr2num(task["start"]), i + 1.05, task["name"], ha="left", va="bottom", fontsize=12)

# 设置坐标轴的范围和标签
ax.set_xlim(mdates.datestr2num("2023-2-15"), mdates.datestr2num("2023-6-15"))
ax.set_ylim(0.5, len(tasks) + 0.5)
ax.set_xlabel("Date", fontsize=14)
ax.set_ylabel("Task", fontsize=14)
ax.set_title("Gantt Chart", fontsize=16)

# 设置网格线和刻度
ax.grid(True, axis="x", linestyle="--")
ax.set_axisbelow(True)
ax.xaxis_date()
fig.autofmt_xdate()

# 显示图像
plt.show()
