from settings import *

class SnakeGameAI:
    """
    A class to represent the Snake Game with AI.

    ...

    Methods
    -------
    __init__():
        Initializes the game by setting up the display, font, and initial state.

    reset():
        Resets the game to its initial state.

    _place_food():
        Places the food in a random position on the grid.

    play_step(action):
        Executes one step of the game based on the provided action.

    is_collision(pt=None):
        Checks if the given point (or the head) collides with the boundaries or itself.

    _update_ui():
        Updates the game display and UI elements.

    _move(action):
        Moves the snake in the specified direction based on the action taken.
    """

    def __init__(self):
        """
        Initializes the SnakeGameAI class, setting up the display, font, and initial game state.
        """
        pg.init()
        self.font = pg.font.SysFont("Arial", 24, bold=True)
        self.display = pg.display.set_mode(RES)
        pg.display.set_caption('Snake')
        self.clock = pg.time.Clock()
        self.reset()

    def reset(self):
        """
        Resets the game to its initial state, including the snake's position, direction, score, and food placement.
        """
        self.direction = Direction.RIGHT
        self.head = Point(WIDTH / 2, HEIGHT / 2)
        self.snake = [
            self.head,
            Point(self.head.x - BLOCK_SIZE, self.head.y),
            Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)
        ]
        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0

    def _place_food(self):
        """
        Places the food in a random position on the grid, ensuring it does not overlap with the snake.
        """
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self, action):
        """
        Executes one step of the game based on the provided action.

        Parameters:
        action (list): A list representing the action [straight, right, left].

        Returns:
        tuple: reward, game_over, score
        """
        self.frame_iteration += 1

        # 1. Collect user input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # 2. Move
        self._move(action)
        self.snake.insert(0, self.head)

        # 3. Check if game over
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score

        # 4. Place new food or just move
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()

        # 5. Update UI and clock
        self._update_ui()
        self.clock.tick(FPS)

        # 6. Return reward, game over and score
        return reward, game_over, self.score

    def is_collision(self, pt=None):
        """
        Checks if the given point (or the head) collides with the boundaries or itself.

        Parameters:
        pt (Point): The point to check for collision. Defaults to the snake's head.

        Returns:
        bool: True if a collision is detected, False otherwise.
        """
        if pt is None:
            pt = self.head
        # Hits boundary
        if pt.x > WIDTH - BLOCK_SIZE or pt.x < 0 or pt.y > HEIGHT - BLOCK_SIZE or pt.y < 0:
            return True
        # Hits itself
        if pt in self.snake[1:]:
            return True
        return False

    def _update_ui(self):
        """
        Updates the game display and UI elements, such as the snake, food, and score.
        """
        self.display.fill(BLACK)
        for pt in self.snake:
            pg.draw.rect(self.display, BLUE1, pg.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pg.draw.rect(self.display, BLUE2, pg.Rect(pt.x + 4, pt.y + 4, 12, 12))
        pg.draw.rect(self.display, RED, pg.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = self.font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pg.display.flip()

    def _move(self, action):
        """
        Moves the snake in the specified direction based on the action taken.

        Parameters:
        action (list): A list representing the action [straight, right, left].
        """
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx]  # No change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx]  # Right turn
        else:  # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx]  # Left turn

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)

if __name__ == "__main__":
    game = SnakeGameAI()
    while True:
        action = [1, 0, 0]  # Example action, should be provided by AI in actual use
        reward, game_over, score = game.play_step(action)
        if game_over:
            game.reset()


    def __init__(self):
        pg.init()
        self.font = pg.font.Font("Ariel", 25)        
        self.display = pg.display.set_mode(RES)
        pg.display.set_caption('Snake')
        self.clock = pg.time.Clock()
        self.reset()


    def reset(self):
        # init game state
        self.direction = Direction.RIGHT

        self.head = Point(WIDTH/2, HEIGHT/2)
        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0


    def _place_food(self):
        x = random.randint(0, (WIDTH-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        y = random.randint(0, (HEIGHT-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()


    def play_step(self, action):
        self.frame_iteration += 1
        # 1. collect user input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        
        # 2. move
        self._move(action) # update the head
        self.snake.insert(0, self.head)
        
        # 3. check if game over
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score

        # 4. place new food or just move
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()
        
        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(FPS)
        # 6. return game over and score
        return reward, game_over, self.score


    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # hits boundary
        if pt.x > WIDTH - BLOCK_SIZE or pt.x < 0 or pt.y > HEIGHT - BLOCK_SIZE or pt.y < 0:
            return True
        # hits itself
        if pt in self.snake[1:]:
            return True

        return False


    def _update_ui(self):
        self.display.fill(BLACK)

        for pt in self.snake:
            pg.draw.rect(self.display, BLUE1, pg.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pg.draw.rect(self.display, BLUE2, pg.Rect(pt.x+4, pt.y+4, 12, 12))

        pg.draw.rect(self.display, RED, pg.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = self.font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pg.display.flip()


    def _move(self, action):
        # [straight, right, left]

        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx] # no change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx] # right turn r -> d -> l -> u
        else: # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx] # left turn r -> u -> l -> d

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)