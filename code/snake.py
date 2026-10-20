"""뱀 게임 로직 (화면 출력과 분리)."""
import random

from settings import COLS, ROWS, OBSTACLE_EVERY, OBSTACLE_SAFE_DIST

UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)


class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        cx, cy = COLS // 2, ROWS // 2
        self.body = [(cx, cy), (cx - 1, cy), (cx - 2, cy)]
        self.direction = RIGHT
        self.next_dir = RIGHT
        self.score = 0
        self.alive = True
        self.obstacles = set()
        self.food = self._spawn_food()

    def _free_cells(self):
        return [(x, y) for x in range(COLS) for y in range(ROWS)
                if (x, y) not in self.body and (x, y) not in self.obstacles]

    def _spawn_food(self):
        free = self._free_cells()
        return random.choice(free) if free else None

    def _spawn_obstacle(self):
        hx, hy = self.body[0]
        free = [(x, y) for x, y in self._free_cells() if (x, y) != self.food
                and abs(x - hx) + abs(y - hy) >= OBSTACLE_SAFE_DIST]
        if free:
            self.obstacles.add(random.choice(free))

    def turn(self, new_dir):
        # 정반대 방향으로는 바로 돌 수 없다
        if (new_dir[0] + self.direction[0], new_dir[1] + self.direction[1]) != (0, 0):
            self.next_dir = new_dir

    def step(self):
        if not self.alive:
            return
        self.direction = self.next_dir
        hx, hy = self.body[0]
        head = (hx + self.direction[0], hy + self.direction[1])

        ate = head == self.food
        # 꼬리는 이번 턴에 빠지므로 먹지 않았다면 꼬리 칸은 충돌 대상이 아니다
        hits_body = head in (self.body if ate else self.body[:-1])
        if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS) or hits_body or head in self.obstacles:
            self.alive = False
            return

        self.body.insert(0, head)
        if ate:
            self.score += 10
            if self.score % OBSTACLE_EVERY == 0:
                self._spawn_obstacle()  # 먹이보다 먼저 만들어야 새 먹이가 장애물에 겹치지 않음
            self.food = self._spawn_food()
            if self.food is None:  # 판을 가득 채우면 종료
                self.alive = False
        else:
            self.body.pop()
