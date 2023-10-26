import keyboard
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.preprocessing.sequence import pad_sequences

# 创建一个字典来保存按键及其对应的次数
key_counts = {}

# 按键事件处理函数
def key_event_handler(event):
    key = event.name
    print(key)

    # 忽略非字母和数字按键
    # if not key.isalnum():
    #     return

    # 更新按键计数
    if key in key_counts:
        key_counts[key] += 1
    else:
        key_counts[key] = 1

# 注册按键事件处理函数
keyboard.on_press(key_event_handler)
print('Start tapping now')
# 监听键盘事件，直到按下F11退出
keyboard.wait('f11')
keyboard.unhook_all()

# Weird, if u delete the print, you shall get a runtime error?
print(key_counts)
for key, count in key_counts.items():
    print(f"按键 {key}: {count} 次")
    pass

# 创建一个2D列表来表示键盘布局
keyboard_layout = [
    ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace', ], 
    ['tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', ],
    ['caps lock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', 'enter', ],
    ['shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'right shift', ],
    ['ctrl', 'fn', 'left windows', 'alt', 'space', 'right alt', 'right ctrl', ],
]
# 2 problems:1. */8 two values should added together 2. what the heck is left ctrl?

# 提取按键使用频率列表
key_freq = []
for row in keyboard_layout:
    row_freq = []
    for key in row:
        if key in key_counts:
            row_freq.append(key_counts[key])
        else:
            row_freq.append(0)
    key_freq.append(row_freq)

# 对子列表进行填充，使其具有相同的长度
key_freq = pad_sequences(key_freq, padding='post')
# 调整图形大小和间距
plt.figure(figsize=(8, 4))
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.9)

# 绘制热图
sns.heatmap(key_freq, annot=True, cmap="jet", fmt="d", linewidths=0.5,
            xticklabels=False, yticklabels=False, cbar=False)
plt.title("Keyboard Heatmap: Key Usage Frequency")
plt.xlabel("Keys")
plt.ylabel("Rows")
plt.show()
