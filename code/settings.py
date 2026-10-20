"""게임 설정값."""
CELL = 24
COLS = 25
ROWS = 20
WIDTH = CELL * COLS
HEIGHT = CELL * ROWS + 40  # 아래 40px은 점수판
FPS_START = 8
FPS_MAX = 20
OBSTACLE_EVERY = 30  # 이 점수마다 장애물 하나 추가 (먹이 3개당 1개)
OBSTACLE_SAFE_DIST = 4  # 머리에서 이 맨해튼 거리 안에는 장애물을 만들지 않음

BG = (20, 24, 30)
GRID = (28, 33, 41)
SNAKE_HEAD = (120, 220, 120)
SNAKE_BODY = (70, 170, 90)
FOOD = (230, 80, 80)
OBSTACLE = (130, 135, 150)
TEXT = (230, 230, 230)
PANEL = (12, 14, 18)
