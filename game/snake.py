
# Import settings
from settings import *



# Snake Game class
class Snake:
    def __init__(self) -> None:
        self.initialize_game()

    def initialize_game(self):
        """Initialize the game settings and variables."""
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Snake-Intelligence')
        pg.font.init()
        self.timer_event = pg.USEREVENT + 1
        pg.time.set_timer(self.timer_event, 1000)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("Arial", 24, bold=True)
        self.direction = Direction.RIGHT
        self.head = Point(WIDTH // 2, HEIGHT // 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self.game_over = False
        self.place_food()


    def place_food(self):
        """Place the food at a random location."""
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self.place_food()

    def is_collision(self):
        """Check if the snake has collided with itself or the boundaries."""
        # Hits boundary
        if self.head.x >= WIDTH or self.head.x < 0 or self.head.y >= HEIGHT or self.head.y < 0:
            return True
        # Hits itself
        if self.head in self.snake[1:]:
            return True
        return False

    def check_events(self):
        """Handle the user inputs and events."""
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                elif event.key == pg.K_RIGHT and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                elif event.key == pg.K_UP and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                elif event.key == pg.K_DOWN and self.direction != Direction.UP:
                    self.direction = Direction.DOWN

    def update_display(self):
        """Update the game display."""
        pg.display.flip()
        self.clock.tick(FPS)

    def move_snake(self):
        """Move the snake in the current direction."""
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
        self.snake.insert(0, self.head)

    def draw_elements(self):
        """Draw the snake, food, and score on the screen."""
        self.screen.fill(BLACK)
        for pt in self.snake:
            pg.draw.rect(self.screen, BLUE1, pg.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pg.draw.rect(self.screen, BLUE2, pg.Rect(pt.x + 4, pt.y + 4, 12, 12))
        pg.draw.rect(self.screen, RED, pg.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        text = self.font.render("Score: " + str(self.score), True, WHITE)
        self.screen.blit(text, [0, 0])

    def handle_timer(self):
        """Handle the timer event."""
        pass

    def check_game_status(self):
        """Check the game status and handle collisions and food collection."""
        if self.is_collision():
            self.game_over = True
            return self.game_over, self.score

        if self.head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()

    def __call__(self):
        """Run the game loop."""
        while not self.game_over:
            self.check_events()
            self.move_snake()
            self.check_game_status()
            self.draw_elements()
            self.update_display()
        self.__del__()

    def __del__(self):
        """Clean up resources and end the game."""
        print('Final Score', self.score)
        pg.quit()
        print("Game is destroyed")

if __name__ == "__main__":
    game = Snake()
    game()
