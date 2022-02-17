import math
import random
import winsound
import arcade
import arcade.gui
import os
USER_SPRITE_SCALING = 0.1
SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "Arctic Rush"

MOVEMENT_SPEED = 10
BULLET_SPEED = 3

INSTRUCTIONS_PAGE = 0
GAME_RUNNING = 1
GAME_OVER = 2
WIN_GAME = 3

winsound.PlaySound("sounds/cool.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        self.wall_list = None
        self.background = None


def setup_room_1():
    room = Room()


    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/glacier.png", SPRITE_SCALING)
    wall.left = 4 * SPRITE_SIZE
    wall.bottom = 3 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("images/icecrack.png", 0.12)
    wall.left = 5 * SPRITE_SIZE
    wall.bottom = 6 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("images/spiky.png", 0.2)
    wall.left = 8 * SPRITE_SIZE
    wall.bottom = 2.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    room.background = arcade.load_texture("images/ice.jpg")

    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    USER_SPRITE_SCALING = 0.2


    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    USER_SPRITE_SCALING = 0.2
    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5):
                wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/glacier.png", SPRITE_SCALING)
    wall.left = 3 * SPRITE_SIZE
    wall.bottom = 6 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceberg.png", 0.2)
    wall.left = 120
    wall.bottom = 150
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceberg.png", 0.3)
    wall.left = 350
    wall.bottom = 150
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceberg.png", 0.1)
    wall.left = 550
    wall.bottom = 150
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/icecrack.png", 0.1)
    wall.left = 9 * SPRITE_SIZE
    wall.bottom = 6 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("images/iceberg.png", 0.12)
    wall.left = 750
    wall.bottom = 100
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")




    return room

def setup_room_3():
    """
    Create and return room 2.
    """
    room = Room()

    USER_SPRITE_SCALING = 0.2


    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    USER_SPRITE_SCALING = 0.2
    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            if (x != SPRITE_SIZE * 9 and x != SPRITE_SIZE * 10 ):    
                wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5):
                wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/glacier.png", SPRITE_SCALING)
    wall.left = 3 * SPRITE_SIZE
    wall.bottom = 4.5 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/icecrack.png", 0.12)
    wall.left = 150
    wall.bottom = 100
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/icecrack.png", 0.15)
    wall.left = 480
    wall.bottom = 255
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/icecrack.png", 0.05)
    wall.left = 730
    wall.bottom = 470
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")



    return room

def setup_room_4():
    """
    Create and return room 2.
    """
    room = Room()

    USER_SPRITE_SCALING = 0.01


    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    USER_SPRITE_SCALING = 0.2
    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x != 0:
                wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 11 * SPRITE_SIZE
    wall.bottom = 1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 11 * SPRITE_SIZE
    wall.bottom = 1.5 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 11 * SPRITE_SIZE
    wall.bottom = 2 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 11 * SPRITE_SIZE
    wall.bottom = 4 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 11 * SPRITE_SIZE
    wall.bottom = 4.5 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 11 * SPRITE_SIZE
    wall.bottom = 5 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 11 * SPRITE_SIZE
    wall.bottom = 5.5 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 11 * SPRITE_SIZE
    wall.bottom = 6 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 11 * SPRITE_SIZE
    wall.bottom = 6.5 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 11 * SPRITE_SIZE
    wall.bottom = 7 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 11 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 10.5 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 10 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 9.5 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 9 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 8.5 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 8 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 7.5 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 7 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 6.5 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 6 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 5.5 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 5 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 4.5 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 4 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 3.5 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 3 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 2.5 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 2 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 1.5 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")

    wall = arcade.Sprite("images/iceblock.png", SPRITE_SCALING * 0.5)
    wall.left = 1 * SPRITE_SIZE
    wall.bottom = 7.1 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/ice.jpg")








    return room



class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.frame_count = 0

        self.current_state = INSTRUCTIONS_PAGE

        self.player_list = arcade.SpriteList()

        self.total_time = 0.0
        


        # Sprite lists
        self.current_room = 0

        self.coin_list = None
        self.coin_list2 = None
        self.coin_list3 = None
        self.coin_list4 = None

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.score = 0
        self.score_text = None

        self.instructions = []
        texture = arcade.load_texture("images/intro.jpg")
        self.instructions.append(texture)
    

    def level_1(self):
        for i in range(10):
            
            # Create the coin instance
            coin = arcade.Sprite("images/diamonddd.png", SPRITE_SCALING / 4)

            # Position the coin
            coin.center_x = random.randrange(100, SCREEN_WIDTH - 100)
            coin.center_y = random.randrange(100, SCREEN_HEIGHT - 100)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Add top-left enemy ship
        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 0
        self.enemy_list.append(enemy)

        # Add top-right enemy ship
        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = SCREEN_WIDTH - 120
        enemy.center_y = 3
        enemy.angle = 0
        self.enemy_list.append(enemy)



    def level_2(self):
        for i in range(20):

            # Create the coin instance
            coin = arcade.Sprite("images/diamonddd.png", SPRITE_SCALING / 4)

            # Position the coin
            coin.center_x = random.randrange(100, SCREEN_WIDTH - 100)
            coin.center_y = random.randrange(100, SCREEN_HEIGHT - 100)
            # Add the coin to the 2nd coin list
            self.coin_list2.append(coin)

        # Add top-left enemy ship
        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 0
        self.enemy_list2.append(enemy)

        # Add top-right enemy ship
        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = SCREEN_WIDTH - 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 0
        self.enemy_list2.append(enemy)

        # Add top-right enemy ship
        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 450
        enemy.center_y = 13
        enemy.angle = 0
        self.enemy_list2.append(enemy)


        # Loop through each enemy that we have

            
    def level_3(self):
        for i in range(30):

            # Create the coin instance
            coin = arcade.Sprite("images/diamonddd.png", SPRITE_SCALING / 4)

            # Position the coin
            coin.center_x = random.randrange(100, SCREEN_WIDTH - 100)
            coin.center_y = random.randrange(100, SCREEN_HEIGHT - 100)

            # Add the coin to the lists
            self.coin_list3.append(coin)

        # Add top-left enemy ship
        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 0
        self.enemy_list3.append(enemy)

        # Add top-right enemy ship
        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = SCREEN_WIDTH - 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 0
        self.enemy_list3.append(enemy)


        # Add top-right enemy ship
        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = SCREEN_WIDTH - 120
        enemy.center_y = 13
        enemy.angle = 0
        self.enemy_list3.append(enemy)

        # Add top-right enemy ship
        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 120
        enemy.center_y = 13
        enemy.angle = 0
        self.enemy_list3.append(enemy)
        
        # Loop through each enemy that we have


    def level_4(self):
        for i in range(100):

            # Create the coin instance
            coin = arcade.Sprite("images/goldfish.png", SPRITE_SCALING / 6)

            # Position the coin
            coin.center_x = 2 * SPRITE_SIZE
            coin.center_y = 8.5 * SPRITE_SIZE

            # Add the coin to the 2nd coin list
            self.coin_list4.append(coin)

        for i in range(30):

            # Create the coin instance
            coin = arcade.Sprite("images/diamonddd.png", SPRITE_SCALING / 4)

            # Position the coin
            coin.center_x = random.randrange(100, SCREEN_WIDTH - 100)
            coin.center_y = random.randrange(100, SCREEN_HEIGHT - 100)

            # Add the coin to the 2nd coin list
            self.coin_list4.append(coin)

        # Add top-left enemy ship
        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 110
        enemy.center_y = 3
        enemy.angle = 0
        self.enemy_list4.append(enemy)

        # Add top-right enemy ship
        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = SCREEN_WIDTH - 30
        enemy.center_y = 3
        enemy.angle = 0
        self.enemy_list4.append(enemy)

        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 300
        enemy.center_y = 400
        enemy.angle = 0
        self.enemy_list4.append(enemy)

        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 300
        enemy.center_y = 100
        enemy.angle = 0
        self.enemy_list4.append(enemy)

        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 200
        enemy.center_y = 400
        enemy.angle = 0
        self.enemy_list4.append(enemy)

        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 100
        enemy.center_y = 400
        enemy.angle = 0
        self.enemy_list4.append(enemy)

        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 100
        enemy.center_y = 100
        enemy.angle = 0
        self.enemy_list4.append(enemy)

        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 200
        enemy.center_y = 100
        enemy.angle = 0
        self.enemy_list4.append(enemy)

        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 400
        enemy.center_y = 100
        enemy.angle = 0
        self.enemy_list4.append(enemy)

        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 500
        enemy.center_y = 100
        enemy.angle = 0
        self.enemy_list4.append(enemy)

        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 400
        enemy.center_y = 400
        enemy.angle = 0
        self.enemy_list4.append(enemy)

        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 500
        enemy.center_y = 400
        enemy.angle = 0
        self.enemy_list4.append(enemy)

        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 600
        enemy.center_y = 400
        enemy.angle = 0
        self.enemy_list4.append(enemy)

        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 600
        enemy.center_y = 100
        enemy.angle = 0
        self.enemy_list4.append(enemy)




    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("images/penguin.png", USER_SPRITE_SCALING)
        self.player_sprite.center_x = 150
        self.player_sprite.center_y = 350
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        self.total_time = 0.0
        
        self.coin_list = arcade.SpriteList()
        self.coin_list2 = arcade.SpriteList()
        self.coin_list3 = arcade.SpriteList()
        self.coin_list4 = arcade.SpriteList()

        self.enemy_list = arcade.SpriteList()
        self.enemy_list2 = arcade.SpriteList()
        self.enemy_list3 = arcade.SpriteList()
        self.enemy_list4 = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.bullet_list2 = arcade.SpriteList()
        self.bullet_list3 = arcade.SpriteList()
        self.bullet_list4 = arcade.SpriteList()

        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 0
        self.enemy_list.append(enemy)

        # Add top-right enemy ship
        enemy = arcade.Sprite("images/walrus.png", 0.2)
        enemy.center_x = SCREEN_WIDTH - 120
        enemy.center_y = 3
        enemy.angle = 0
        self.enemy_list.append(enemy)

        for i in range(50):

            # Create the coin instance
            coin = arcade.Sprite("images/diamonddd.png", SPRITE_SCALING / 4)

            # Position the coin
            coin.center_x = random.randrange(100, SCREEN_WIDTH - 100)
            coin.center_y = random.randrange(100, SCREEN_HEIGHT - 100)
            # Add the coin to the lists
            self.coin_list.append(coin)

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        room = setup_room_3()
        self.rooms.append(room)

        room = setup_room_4()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
    

    def draw_instructions_page(self, page_number):
        """
        Draw an instruction page. Load the page as an image.
        """
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)
        
        output ="Arctic Rush"
        arcade.draw_text(output, 225, 350, [134, 235, 228], 54, font_name="Kenney Pixel Square")
        output ="Click anywhere to start"
        arcade.draw_text(output, 450, 325, arcade.color.WHITE_SMOKE, 15, font_name="Kenney Pixel Square")


    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """

        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, [0, 0, 0, 150])
        
        output = "Game Over"
        arcade.draw_text(output, 225, 350, arcade.color.RED, 54, font_name="Kenney Pixel Square")

        output = "Press 'r' to Restart"

        arcade.draw_text(output, 265, 275, arcade.color.WHITE_SMOKE, 24, font_name="Kenney Pixel Square")

    def draw_win_game(self):

        minutes = int(self.total_time) // 60

        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60

        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, [0, 0, 0, 150])
        
        output = "Congratulations! You found the Golden Fish!"
        arcade.draw_text(output, 5, 450, arcade.color.RED, 24, font_name="Kenney Pixel Square")
        
        output = f"You finished in: {minutes:02d}:{seconds:02d}"
        arcade.draw_text(output, 250, 300, arcade.color.GOLDEN_YELLOW, 24, font_name="Kenney Pixel Square")

        output = f"Score: {self.score}"
        arcade.draw_text(output, 350, 250, arcade.color.GOLDEN_YELLOW, 24, font_name="Kenney Pixel Square")

        output = "Press 'r' to play again!"
        arcade.draw_text(output, 235, 100, arcade.color.WHITE_SMOKE, 24, font_name="Kenney Pixel Square")


        

    def draw_game(self):


        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.rooms[self.current_room].background)

        # Draw all the walls in this room
        self.rooms[self.current_room].wall_list.draw()

        self.player_list.draw()
        if self.current_room == 0:
            self.coin_list.draw()
        elif self.current_room == 1:
            self.coin_list2.draw()
        elif self.current_room == 2:
            self.coin_list3.draw()
        elif self.current_room == 3:
            self.coin_list4.draw()

        if self.current_room == 0:
            self.enemy_list.draw()
        elif self.current_room == 1:
            self.enemy_list2.draw()
        elif self.current_room == 2:
            self.enemy_list3.draw()
        elif self.current_room == 3:
            self.enemy_list4.draw()

        if self.current_room == 0:
            self.bullet_list.draw()
        elif self.current_room == 1:
            self.bullet_list2.draw()
        elif self.current_room == 2:
            self.bullet_list3.draw()
        elif self.current_room == 3:
            self.bullet_list4.draw()

        # Calculate minutes
        minutes = int(self.total_time) // 60

        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60

        # Figure out our output
        output = f"Time: {minutes:02d}:{seconds:02d}"

        # Output the timer text.
        arcade.draw_text(output, 625, 15, arcade.color.RED, 30, font_name="Kenney Pixel Square")
            
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.RED, 30, font_name="Kenney Pixel Square")
        


    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        if self.current_state == INSTRUCTIONS_PAGE:
            self.draw_instructions_page(0)

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        elif self.current_state == WIN_GAME:
            self.draw_game()
            self.draw_win_game()

        else:
            self.draw_game()
            self.draw_game_over()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change states as needed.
        if self.current_state == INSTRUCTIONS_PAGE:
            # Start the game
            self.setup()
            self.current_state = GAME_RUNNING

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if self.current_state == GAME_OVER and key == arcade.key.R:
            self.clearall()
            self.current_state = GAME_RUNNING
            self.setup()
        if self.current_state == WIN_GAME and key == arcade.key.R:
            self.clearall()
            self.score = 0
            self.current_state = GAME_RUNNING
            self.setup()
        elif self.current_state == GAME_RUNNING:
            if key == arcade.key.UP:
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.player_sprite.change_y = -MOVEMENT_SPEED
            elif key == arcade.key.LEFT:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def clearall(self):
        self.bullet_list.clear()
        self.bullet_list2.clear()
        self.bullet_list3.clear()
        self.bullet_list4.clear()
        self.enemy_list.clear()
        self.enemy_list2.clear()
        self.enemy_list3.clear()
        self.enemy_list4.clear()
        self.coin_list.clear()
        self.coin_list2.clear()
        self.coin_list3.clear()
        self.coin_list4.clear()

    def update(self, delta_time):
        """ Movement and game logic """
        if self.current_state == GAME_RUNNING:

            self.frame_count += 1

            self.total_time += delta_time

            for enemy in self.enemy_list:

                # First, calculate the angle to the player. We could do this
                # only when the bullet fires, but in this case we will rotate
                # the enemy to face the player each frame, so we'll do this
                # each frame.

                # Position the start at the enemy's current location
                start_x = enemy.center_x
                start_y = enemy.center_y

                # Get the destination location for the bullet
                dest_x = self.player_sprite.center_x
                dest_y = self.player_sprite.center_y

                # Do math to calculate how to get the bullet to the destination.
                # Calculation the angle in radians between the start points
                # and end points. This is the angle the bullet will travel.
                x_diff = dest_x - start_x
                y_diff = dest_y - start_y
                angle = math.atan2(y_diff, x_diff)

                # Set the enemy to face the player.
                enemy.angle = math.degrees(angle)-90

                # Shoot every 60 frames change of shooting each frame
                if self.frame_count % 120 == 0:
                    bullet = arcade.Sprite("images/fireball.png", 0.1)
                    bullet.center_x = start_x
                    bullet.center_y = start_y

                    # Angle the bullet sprite
                    bullet.angle = math.degrees(angle)

                    # Taking into account the angle, calculate our change_x
                    # and change_y. Velocity is how fast the bullet travels.
                    bullet.change_x = math.cos(angle) * BULLET_SPEED
                    bullet.change_y = math.sin(angle) * BULLET_SPEED

                    self.bullet_list.append(bullet)


            # Get rid of the bullet when it flies off-screen
            for bullet in self.bullet_list:
                if self.player_sprite.center_x == 0:
                    bullet.kill()

            for enemy in self.enemy_list2:

                # First, calculate the angle to the player. We could do this
                # only when the bullet fires, but in this case we will rotate
                # the enemy to face the player each frame, so we'll do this
                # each frame.

                # Position the start at the enemy's current location
                start_x = enemy.center_x
                start_y = enemy.center_y

                # Get the destination location for the bullet
                dest_x = self.player_sprite.center_x
                dest_y = self.player_sprite.center_y

                # Do math to calculate how to get the bullet to the destination.
                # Calculation the angle in radians between the start points
                # and end points. This is the angle the bullet will travel.
                x_diff = dest_x - start_x
                y_diff = dest_y - start_y
                angle = math.atan2(y_diff, x_diff)

                # Set the enemy to face the player.
                enemy.angle = math.degrees(angle)-90

                # Shoot every 60 frames change of shooting each frame
                if self.frame_count % 120 == 0:
                    bullet = arcade.Sprite("images/fireball.png", 0.1)
                    bullet.center_x = start_x
                    bullet.center_y = start_y

                    # Angle the bullet sprite
                    bullet.angle = math.degrees(angle)

                    # Taking into account the angle, calculate our change_x
                    # and change_y. Velocity is how fast the bullet travels.
                    bullet.change_x = math.cos(angle) * BULLET_SPEED
                    bullet.change_y = math.sin(angle) * BULLET_SPEED

                    self.bullet_list2.append(bullet)


            # Get rid of the bullet when it flies off-screen
            for bullet in self.bullet_list2:
                if self.player_sprite.center_x == 0:
                    bullet.kill()

            for enemy in self.enemy_list3:

                # First, calculate the angle to the player. We could do this
                # only when the bullet fires, but in this case we will rotate
                # the enemy to face the player each frame, so we'll do this
                # each frame.

                # Position the start at the enemy's current location
                start_x = enemy.center_x
                start_y = enemy.center_y

                # Get the destination location for the bullet
                dest_x = self.player_sprite.center_x
                dest_y = self.player_sprite.center_y

                # Do math to calculate how to get the bullet to the destination.
                # Calculation the angle in radians between the start points
                # and end points. This is the angle the bullet will travel.
                x_diff = dest_x - start_x
                y_diff = dest_y - start_y
                angle = math.atan2(y_diff, x_diff)

                # Set the enemy to face the player.
                enemy.angle = math.degrees(angle)-90

                # Shoot every 60 frames change of shooting each frame
                if self.frame_count % 120 == 0:
                    bullet = arcade.Sprite("images/fireball.png", 0.1)
                    bullet.center_x = start_x
                    bullet.center_y = start_y

                    # Angle the bullet sprite
                    bullet.angle = math.degrees(angle)

                    # Taking into account the angle, calculate our change_x
                    # and change_y. Velocity is how fast the bullet travels.
                    bullet.change_x = math.cos(angle) * BULLET_SPEED
                    bullet.change_y = math.sin(angle) * BULLET_SPEED

                    self.bullet_list3.append(bullet)



            # Get rid of the bullet when it flies off-screen
            for bullet in self.bullet_list3:
                if self.player_sprite.center_x == 0:
                    bullet.kill()

            for enemy in self.enemy_list4:

                # First, calculate the angle to the player. We could do this
                # only when the bullet fires, but in this case we will rotate
                # the enemy to face the player each frame, so we'll do this
                # each frame.

                # Position the start at the enemy's current location
                start_x = enemy.center_x
                start_y = enemy.center_y

                # Get the destination location for the bullet
                dest_x = self.player_sprite.center_x
                dest_y = self.player_sprite.center_y

                # Do math to calculate how to get the bullet to the destination.
                # Calculation the angle in radians between the start points
                # and end points. This is the angle the bullet will travel.
                x_diff = dest_x - start_x
                y_diff = dest_y - start_y
                angle = math.atan2(y_diff, x_diff)

                # Set the enemy to face the player.
                enemy.angle = math.degrees(angle)-90

                # Shoot every 60 frames change of shooting each frame
                if self.frame_count % 60 == 0:
                    bullet = arcade.Sprite("images/fireball.png", 0.1)
                    bullet.center_x = start_x
                    bullet.center_y = start_y

                    # Angle the bullet sprite
                    bullet.angle = math.degrees(angle)


                    # Taking into account the angle, calculate our change_x
                    # and change_y. Velocity is how fast the bullet travels.
                    bullet.change_x = math.cos(angle) * BULLET_SPEED
                    bullet.change_y = math.sin(angle) * BULLET_SPEED

                    self.bullet_list4.append(bullet)



            # Get rid of the bullet when it flies off-screen
            for bullet in self.bullet_list4:
                if self.player_sprite.center_x == 0:
                    bullet.kill()


            # Call update on all sprites (The sprites don't do much in this
            # example though.)
            self.physics_engine.update()

            # Do some logic here to figure out what room we are in, and if we need to go
            # to a different room.
            if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
                self.current_room = 1
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.player_sprite.center_x = 0
                self.clearall()
                self.level_2()
                
            elif self.player_sprite.center_x < 0 and self.current_room == 1:
                self.current_room = 0
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.player_sprite.center_x = SCREEN_WIDTH
                self.clearall()
                self.level_1()

            elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 1:
                self.current_room = 2
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.player_sprite.center_x = 0
                self.clearall()
                self.level_3()
               
            elif self.player_sprite.center_x < 0 and self.current_room == 2:
                self.current_room = 1
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.player_sprite.center_x = SCREEN_WIDTH
                self.clearall()
                self.level_2()

            elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 2:
                self.current_room = 3
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.player_sprite.center_x = 0
                self.clearall()
                self.level_4()

            elif self.player_sprite.center_x < 0 and self.current_room == 3:
                self.current_room = 2
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.player_sprite.center_x = SCREEN_WIDTH
                self.clearall()
                self.level_3()

            elif self.player_sprite.center_y > SCREEN_HEIGHT and self.current_room == 2:
                self.player_sprite.center_y = 0

            elif self.player_sprite.center_y < 0 and self.current_room == 2:
                self.player_sprite.center_y = SCREEN_HEIGHT

            self.coin_list.update()
            self.coin_list2.update()
            self.coin_list3.update()
            self.coin_list4.update()

            self.enemy_list.update()
            self.enemy_list2.update()
            self.enemy_list3.update()
            self.enemy_list4.update()

            self.bullet_list.update()
            self.bullet_list2.update()
            self.bullet_list3.update()
            self.bullet_list4.update()
            
            # Generate a list of all sprites that collided with the player.
            hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
            hit_list2 = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list2)
            hit_list3 = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list3)
            hit_list4 = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list4)

            hit_list5 = arcade.check_for_collision_with_list(self.player_sprite, self.bullet_list)
            hit_list6 = arcade.check_for_collision_with_list(self.player_sprite, self.bullet_list2)
            hit_list7 = arcade.check_for_collision_with_list(self.player_sprite, self.bullet_list3)
            hit_list8 = arcade.check_for_collision_with_list(self.player_sprite, self.bullet_list4)
            # Loop through each colliding sprite, remove it, and add to the score.
            for coin in hit_list:
                coin.kill()
                self.score += 1
            for coin in hit_list2:
                coin.kill()
                self.score += 1
            for coin in hit_list3:
                coin.kill()
                self.score += 1
            for coin in hit_list4:
                coin.kill()
                self.score += 1

            for bullet in hit_list5:
                bullet.kill()
                self.score -= 5
            for bullet in hit_list6:
                bullet.kill()
                self.score -= 5
            for bullet in hit_list7:
                bullet.kill()
                self.score -= 5
            for bullet in hit_list8:
                bullet.kill()
                self.score -= 5

            if self.score < 0:
                self.current_state = GAME_OVER
                self.score = 0

            if self.score > 90:
                self.current_state = WIN_GAME




def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
