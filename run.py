import pygame
import math
from queue import PriorityQueue
from collections import deque
import sys

pygame.init()
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Algorithm Visualizer")

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 150)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Fonts
FONT = pygame.font.Font(None, 32)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def a_star(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return False

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
            if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

def dijkstra(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return False

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((g_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

def bfs(draw, grid, start, end):
    queue = deque()
    queue.append(start)
    came_from = {}
    visited = set([start])

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return False

        current = queue.popleft()

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

def dfs(draw, grid, start, end):
    stack = [start]
    came_from = {}
    visited = set([start])

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return False

        current = stack.pop()

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

class Button:
    def __init__(self, x, y, width, height, color, text, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, self.text_color)
        win.blit(text, (self.rect.x + (self.rect.width - text.get_width ()) // 2,
                        self.rect.y + (self.rect.height - text.get_height()) // 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class Dropdown:
    def __init__(self, x, y, width, height, color, options):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.options = options
        self.current_option = options[0]
        self.open = False
        self.option_rects = []

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text = font.render(self.current_option, True, BLACK)
        win.blit(text, (self.rect.x + 10, self.rect.y + (self.rect.height - text.get_height()) // 2))

        if self.open:
            self.option_rects = []  # Clear the list before adding new rectangles
            for i, option in enumerate(self.options):
                option_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                pygame.draw.rect(win, self.color, option_rect)
                text = font.render(option, True, BLACK)
                win.blit(text, (option_rect.x + 10, option_rect.y + (option_rect.height - text.get_height()) // 2))
                self.option_rects.append(option_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.open = not self.open
            elif self.open:
                for i, option_rect in enumerate(self.option_rects):
                    if option_rect.collidepoint(event.pos):
                        self.current_option = self.options[i]
                        self.open = False
                        return True
        return False



def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    
    algorithms = {
        "A*": a_star,
        "Dijkstra": dijkstra,
        "BFS": bfs,
        "DFS": dfs
    }

    run_button = Button(10, 10, 100, 40, GREEN, "Run", BLACK)
    reset_button = Button(120, 10, 100, 40, RED, "Reset", WHITE)
    algorithm_dropdown = Dropdown(230, 10, 150, 40, YELLOW, list(algorithms.keys()))

    while run:
        draw(win, grid, ROWS, width)
        
        run_button.draw(win)
        reset_button.draw(win)
        algorithm_dropdown.draw(win)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]: # LEFT
                pos = pygame.mouse.get_pos()
                
                if run_button.is_clicked(pos):
                    if start and end:
                        started = True
                        for row in grid:
                            for spot in row:
                                spot.update_neighbors(grid)
                        algorithm = algorithms[algorithm_dropdown.current_option]
                        algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                elif reset_button.is_clicked(pos):
                    # Reset everything
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
                    started = False

                    # Clear the canvas and redraw
                    win.fill(WHITE)
                    draw(win, grid, ROWS, width)

        
                else:
                    row, col = get_clicked_pos(pos, ROWS, width)
                    spot = grid[row][col]
                    if not start and spot != end:
                        start = spot
                        start.make_start()
                    elif not end and spot != start:
                        end = spot
                        end.make_end()
                    elif spot != end and spot != start:
                        spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
                    started = False
                    for row in grid:
                        for spot in row:
                            spot.reset()
                    # Clear the canvas
                    win.fill(WHITE)
                    draw(win, grid, ROWS, width)

            algorithm_dropdown.handle_event(event)

        pygame.display.update()

    pygame.quit()

main(WIN, WIDTH)
