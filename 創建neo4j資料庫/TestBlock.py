cards = [
    "中信兄弟聯名卡_鼎極卡",
    "中信兄弟聯名卡_鼎極卡",
    "中信兄弟聯名卡_御璽卡",
    "中信兄弟聯名卡_鈦金卡",
    "中信兄弟聯名卡_白金卡",
    "中信兄弟聯名卡_白金卡"
]

result = list({card.split("_")[0] for card in cards})

print(result)

