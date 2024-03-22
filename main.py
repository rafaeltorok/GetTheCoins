# Complete your game here
import pygame
from random import randint


class Robot:
    def __init__(self, location: str):
        self.__new = pygame.image.load(location)
        self.__width = self.__new.get_width()
        self.__height = self.__new.get_height()

    @property
    def new(self):
        return self.__new

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


class Coin:
    def __init__(self, location: str):
        self.__new = pygame.image.load(location)
        self.__width = self.__new.get_width()
        self.__height = self.__new.get_height()

    @property
    def new(self):
        return self.__new

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


class Monster:
    def __init__(self, location: str):
        self.__new = pygame.image.load(location)
        self.__width = self.__new.get_width()
        self.__height = self.__new.get_height()

    @property
    def new(self):
        return self.__new

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


class GameWindow:
    def __init__(self, width: int, height: int):
        self.__window_width = width
        self.__window_height = height
        self.__screen = pygame.display.set_mode((self.window_width, self.window_height))

    @property
    def screen(self):
        return self.__screen

    @property
    def window_width(self):
        return self.__window_width

    @property
    def window_height(self):
        return self.__window_height


class GameManager:
    def __init__(self):
        self.__game_window = GameWindow(640, 480)
        self.__robot = Robot("img/robot.png")
        self.__coin = Coin("img/coin.png")
        self.__monster = Monster("img/monster.png")
        self.__positions_coins = []
        self.__positions_monsters = []
        self.__xaxis = self.__game_window.window_width//2 - self.__robot.width//2
        self.__yaxis = self.__game_window.window_height - self.__robot.height
        self.__points = 0

    @property
    def game_window(self):
        return self.__game_window

    def welcome_screen(self):
        # Shows the Welcome screen containing the instructions
        self.game_window.screen.fill((220, 220, 220))
        font = pygame.font.SysFont("Arial", 36)
        title = font.render("WELCOME TO GET THE COINS!", True, (255, 0, 0))
        font = pygame.font.SysFont("Arial", 24)
        first_line = font.render("INSTRUCTIONS:", True, (255, 0, 0))
        second_line = font.render("Dodge the monsters and get the coins,", True, (255, 0, 0))
        third_line = font.render("if you touch a monster, it's game over!", True, (255, 0, 0))
        fourth_line = font.render("If a coin reaches the bottom, you'll lose one point,", True, (255, 0, 0))
        fifth_line = font.render("If your score drops below zero, it's also game over!", True, (255, 0, 0))
        sixth_line = font.render("If you get 50 coins, you win the game!", True, (255, 0, 0))
        seventh_line = font.render("Press any key to start", True, (255, 0, 0))
        self.game_window.screen.blit(title, (50, 50))
        self.game_window.screen.blit(first_line, (220, 140))
        self.game_window.screen.blit(second_line, (120, 170))
        self.game_window.screen.blit(third_line, (120, 200))
        self.game_window.screen.blit(fourth_line, (60, 230))
        self.game_window.screen.blit(fifth_line, (60, 260))
        self.game_window.screen.blit(sixth_line, (110, 290))
        self.game_window.screen.blit(seventh_line, (200, 425))
        pygame.display.flip()

    def game_over(self):
        # Shows the game over screen with the final score
        self.game_window.screen.fill((220, 220, 220))
        font = pygame.font.SysFont("Arial", 56)
        first_line = font.render("GAME OVER!", True, (255, 0, 0))
        font = pygame.font.SysFont("Arial", 32)
        second_line = font.render("Final score: " + str(self.points), True, (255, 0, 0))
        font = pygame.font.SysFont("Arial", 24)
        third_line = font.render("Press ESC to exit, or ENTER to play again", True, (255, 0, 0))
        self.game_window.screen.blit(first_line, (150, 100))
        self.game_window.screen.blit(second_line, (225, 200))
        self.game_window.screen.blit(third_line, (100, 420))
        pygame.display.flip()

    def congratulations(self):
        # Shows the congratulations screen after reaching 50 points
        self.game_window.screen.fill((220, 220, 220))
        font = pygame.font.SysFont("Arial", 44)
        first_line = font.render("CONGRATULATIONS!!!", True, (255, 0, 0))
        second_line = font.render("YOU WON!", True, (255, 0, 0))
        font = pygame.font.SysFont("Arial", 32)
        third_line = font.render("Final score: " + str(self.points), True, (255, 0, 0))
        font = pygame.font.SysFont("Arial", 24)
        fourth_line = font.render("Press ESC to exit, or ENTER to play again", True, (255, 0, 0))
        self.game_window.screen.blit(first_line, (90, 60))
        self.game_window.screen.blit(second_line, (200, 110))
        self.game_window.screen.blit(third_line, (220, 250))
        self.game_window.screen.blit(fourth_line, (100, 420))
        pygame.display.flip()

    @property
    def robot(self):
        return self.__robot

    @property
    def coin(self):
        return self.__coin

    @property
    def monster(self):
        return self.__monster

    @property
    def positions_coins(self):
        return self.__positions_coins

    @property
    def positions_monsters(self):
        return self.__positions_monsters

    def add_positions_coins(self):
        self.__positions_coins.append([randint(0,self.game_window.window_width-self.coin.width),-randint(100,1000)])

    # Spawns new coins when starting a new game
    def reset_positions_coins(self):
        self.__positions_coins.clear()

    def add_positions_monsters(self):
        self.__positions_monsters.append([randint(0,self.game_window.window_width-self.monster.width),-randint(100,1000)])

    # Spawns new monsters when starting a new game
    def reset_positions_monsters(self):
        self.__positions_monsters.clear()

    @property
    def xaxis(self):
        return self.__xaxis

    def xaxis_increase(self):
        self.__xaxis+=3

    def xaxis_decrease(self):
        self.__xaxis-=3

    # Resets the robot position to the center, when starting a new game
    def reset_xaxis(self):
        self.__xaxis = self.__game_window.window_width//2 - self.__robot.width//2

    @property
    def yaxis(self):
        return self.__yaxis

    @property
    def points(self):
        return self.__points

    def reset_points(self):
        self.__points = 0

    def increase_points(self):
        self.__points+=1

    def decrease_points(self):
        self.__points-=1


class PlayGame:
    def __init__(self, manager: GameManager, number: int):
        self.__manager = manager
        self.__number = number

    @property
    def manager(self):
        return self.__manager

    @property
    def number(self):
        return self.__number

    # Waits for the player to choose between exiting the game(ESC key) or playing again(ENTER key)
    def game_over(self):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_RETURN:
                    self.play()

    # Waits for the player to press a key before starting the game after the "Welcome" screen
    def start_game(self):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                self.play()

    def play(self):
        to_right = False
        to_left = False
        clock = pygame.time.Clock()
        font = pygame.font.SysFont("Arial", 24)
        # The reset methods are usefull when the player chooses the "play again" option
        self.manager.reset_points()
        self.manager.reset_positions_coins()
        self.manager.reset_positions_monsters()
        self.manager.reset_xaxis()

        # Generates the random positions where both the coins and monsters are going to spawn on the top
        for i in range(self.number):
            self.manager.add_positions_coins()
        for i in range(self.number):
            self.manager.add_positions_monsters()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        to_left = True
                    if event.key == pygame.K_RIGHT:
                        to_right = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        to_left = False
                    if event.key == pygame.K_RIGHT:
                        to_right = False

                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                if self.manager.points < 0:
                    self.manager.game_over()
                    self.game_over()
                elif self.manager.points == 50:
                    self.manager.congratulations()
                    self.game_over()

            # Increases or decreases the value on the X axis, to move the robot either left or right
            if to_right:
                if self.manager.xaxis + self.manager.robot.width < self.manager.game_window.window_width:
                    self.manager.xaxis_increase()
            if to_left:
                if self.manager.xaxis > 0:
                    self.manager.xaxis_decrease()

            for i in range(len(self.manager.positions_monsters)):
                # Increases the Y axis values, so both the coins and monsters can move down the screen
                self.manager.positions_coins[i][1] += 1
                self.manager.positions_monsters[i][1] += 1
                robot_middle = self.manager.xaxis + self.manager.robot.width/2
                if self.manager.positions_monsters[i][1] + self.manager.monster.height <= self.manager.game_window.window_height and self.manager.positions_monsters[i][1] + self.manager.monster.height > 0:
                    monster_middle = self.manager.positions_monsters[i][0] + self.manager.monster.width/2
                    if abs(robot_middle-monster_middle) <= 40 and abs(self.manager.yaxis - self.manager.positions_monsters[i][1]) <= 50:
                        # Game ends if the player touches a monster
                        self.manager.game_over()
                        self.game_over()
                elif self.manager.positions_monsters[i][1] >= self.manager.game_window.window_height:
                    # When a monster reaches the bottom of the screen, a new one is generated on the top
                    self.manager.positions_monsters[i][0] = randint(0, self.manager.game_window.window_width - self.manager.monster.width)
                    self.manager.positions_monsters[i][1] = -randint(100,1000)

                if self.manager.positions_coins[i][1] + self.manager.coin.height >= self.manager.yaxis:
                    coin_middle = self.manager.positions_coins[i][0] + self.manager.coin.width/2
                    if abs(robot_middle-coin_middle) <= (self.manager.robot.width + self.manager.coin.width)/2:
                        # If the robot catches a coin, the player gets 1 point
                        self.manager.positions_coins[i][0] = randint(0, self.manager.game_window.window_width - self.manager.coin.width)
                        self.manager.positions_coins[i][1] = -randint(100,1000)
                        self.manager.increase_points()
                    elif abs(self.manager.positions_coins[i][1] >= self.manager.game_window.window_height):
                        # If a coin touches the bottom, the player loses 1 point
                        self.manager.positions_coins[i][0] = randint(0, self.manager.game_window.window_width - self.manager.coin.width)
                        self.manager.positions_coins[i][1] = -randint(100,1000)
                        self.manager.decrease_points()

            # Displays the character you control on the screen
            self.manager.game_window.screen.fill((220, 220, 220))
            self.manager.game_window.screen.blit(self.manager.robot.new, (self.manager.xaxis, self.manager.yaxis))

            # Creates both a new coin object and a monster object to display on the screen
            for i in range(self.number):
                self.manager.game_window.screen.blit(self.manager.coin.new, (self.manager.positions_coins[i][0], self.manager.positions_coins[i][1]))
                self.manager.game_window.screen.blit(self.manager.monster.new, (self.manager.positions_monsters[i][0], self.manager.positions_monsters[i][1]))

            # Shows the score on the top right edge of the window
            text = font.render("Score: " + str(self.manager.points), True, (255, 0, 0))
            self.manager.game_window.screen.blit(text, (self.manager.game_window.window_width-150, 10))
            pygame.display.flip()
            clock.tick(120)


def main():
    pygame.init()
    pygame.display.set_caption("GET THE COINS!")
    manager = GameManager()
    number = 10  # Defines how many monsters and coins are going to appear on screen simultaneously

    play_game = PlayGame(manager, number)
    play_game.manager.welcome_screen()
    play_game.start_game()


main()