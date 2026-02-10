import pyautogui
import time
import random

pyautogui.FAILSAFE = True  

# ================= CONFIG =================
POSITIONS = [
    (500, 300),
    (820, 420),
    (1000, 600),
]

WAIT_MINUTES = 30
WAIT_SECONDS = WAIT_MINUTES * 60

# ==========================================

def smooth_move(x, y):
    duration = random.uniform(0.8, 1.5)
    pyautogui.moveTo(
        x, y,
        duration=duration,
        tween=pyautogui.easeInOutQuad
    )

def click_with_human_delay():
    time.sleep(random.uniform(0.2, 0.6))
    pyautogui.click()

def random_offset(x, y, offset=5):
    return (
        x + random.randint(-offset, offset),
        y + random.randint(-offset, offset)
    )

print("เริ่มทำงานใน 5 วินาที...")
time.sleep(5)

while True:
    print("เริ่มรอบใหม่")

    for i, (x, y) in enumerate(POSITIONS, start=1):
        rx, ry = random_offset(x, y)
        print(f"  จุดที่ {i}: ไปที่ ({rx}, {ry})")

        smooth_move(rx, ry)
        click_with_human_delay()

    # นับถอยหลัง 30 นาที
    print(f"รอ {WAIT_MINUTES} นาที...")
    for remaining in range(WAIT_SECONDS, 0, -60):
        mins = remaining // 60
        print(f"  เหลืออีก {mins} นาที")
        time.sleep(60)