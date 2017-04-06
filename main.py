# Drewdrod Created 3/31/17
# Battle Tanks
import pygame
from settings import *
from sprites import *
from os import path

class Game():
    def __init__(self):
        # Initializes Pygame
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Battle Tanks')
        self.clock = pygame.time.Clock()
        self.running = True
        self.font_name = pygame.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        # Loads data
        game_folder = path.dirname(__file__)
        image_folder = path.join(game_folder, 'image')
        sound_folder = path.join(game_folder, 'sound')

    def new(self):
        # Starts a new game
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player = Player(self)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Process input (events)
        for event in pygame.event.get():
            # checks for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                # checks for mouse motion
            if event.type == pygame.MOUSEMOTION:
                game.player.move_with_mouse()

    def update(self):
        # Update
        self.all_sprites.update()

    def draw(self):
        # Draw / Render
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        # after drawing everything, flip the display
        pygame.display.flip()

    def game_start_screen(self):
        # Game start screen
        self.intro = True
        while self.intro:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.intro = False
                    self.running = False
            self.screen.fill(WHITE)
            self.draw_text('Welcome to Battle Tanks!', 50, GREEN, WIDTH / 2, HEIGHT / 4)
            self.draw_text('Destroy the enemy tank to win!', 40, BLACK, WIDTH / 2, HEIGHT / 2)
            self.draw_text('Good luck!', 30, BLACK, WIDTH / 2, HEIGHT * 3 / 4)
            self.draw_button('play', LIGHT_GREEN, GREEN, 100, 50, WIDTH - 650, HEIGHT - 100, 'menu_play')
            self.draw_button('controls', YELLOW, LIGHT_YELLOW, 100, 50, WIDTH - 450, HEIGHT - 100, 'menu_controls')
            self.draw_button('quit', LIGHT_RED, RED, 100, 50, WIDTH - 250, HEIGHT - 100, 'menu_quit')
            pygame.display.flip()

    def game_over_screen(self):
        # Game over screen
        if not self.running:
            return

    def game_controls_screen(self):
        # Game controls screen
        self.controls = True
        while self.controls:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.controls = False
                    self.running = False
            self.screen.fill(WHITE)
            self.draw_text('Controls', 75, GREEN, WIDTH / 2, HEIGHT / 4 - 100)
            self.draw_text('A and D move your tank left or right', 50, BLACK, WIDTH / 2, HEIGHT / 4 - 25)
            self.draw_text('W and S move your turret up or down', 50, BLACK, WIDTH / 2, HEIGHT / 4 + 50)
            self.draw_text('Space to shoot', 50, BLACK, WIDTH / 2, HEIGHT / 4 + 125)
            self.draw_text('Up and Down to adjust your power', 50, BLACK, WIDTH / 2, HEIGHT / 4 + 200)
            self.draw_button('play', LIGHT_GREEN, GREEN, 100, 50, WIDTH - 650, HEIGHT - 100, 'controls_play')
            self.draw_button('back', YELLOW, LIGHT_YELLOW, 100, 50, WIDTH - 450, HEIGHT - 100, 'controls_back')
            self.draw_button('quit', LIGHT_RED, RED, 100, 50, WIDTH - 250, HEIGHT - 100, 'controls_quit')
            pygame.display.flip()

    def draw_button(self, text, on_color, off_color, width, height, x, y, action):
        mouse_location = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        button_rect = pygame.Rect(x, y, width, height)
        if x + width > mouse_location[0] > x and y + height > mouse_location[1] > y:
            pygame.draw.rect(self.screen, on_color, button_rect)
            if mouse_click[0] == 1:
                if action == 'menu_play':
                    self.intro = False
                if action == 'menu_controls':
                    self.intro = False
                    self.game_controls_screen()
                if action == 'menu_quit':
                    self.intro = False
                    self.running = False
                if action == 'controls_play':
                    self.controls = False
                if action == 'controls_back':
                    self.controls = False
                    self.game_start_screen()
                if action == 'controls_quit':
                    self.controls = False
                    self.running = False
        else:
            pygame.draw.rect(self.screen, off_color, button_rect)

        self.draw_text(text, 25, BLACK, x + 50, y + 10)

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

game = Game()
game.game_start_screen()
while game.running:
    game.new()
    game.game_over_screen()

pygame.quit()
