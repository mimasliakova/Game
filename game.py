import random 
import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Ladybug wants bee'

SPRITE_SCALING_BEE = .25
SPRITE_SCALING_LADYBUG = 0.5
BEE_COUNT = 35
            
            
class MyGame(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        self.ladybug_list = None
        self.bee_list = None
        self.ladybug_sprite = None
        self.score = 0
        
        self.set_mouse_visible(False)
        
        arcade.set_background_color(arcade.color.AMAZON)
        
        
    def setup(self):
        self.ladybug_list = arcade.SpriteList()
        self.bee_list = arcade.SpriteList()
        self.score = 0

 
        self.ladybug_sprite = arcade.Sprite(":resources:images/enemies/ladybug.png", 
                                       SPRITE_SCALING_LADYBUG)
        self.ladybug_sprite.center_x = 100
        self.ladybug_sprite.center_y = 100
        self.ladybug_list.append(self.ladybug_sprite)

    
        for i in range(BEE_COUNT):
            bee = arcade.Sprite(":resources:images/enemies/bee.png",
                                SPRITE_SCALING_BEE)
            bee.center_x = random.randrange(SCREEN_WIDTH)
            bee.center_y = random.randrange(SCREEN_HEIGHT)
            self.bee_list.append(bee)
        

    def on_draw(self):
        arcade.start_render()
        self.bee_list.draw()
        self.ladybug_list.draw()
    
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.ALMOND, 16)
    
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.ladybug_sprite.center_x = x
        self.ladybug_sprite.center_y = y
    
    
    def on_update(self, delta_time):
        self.bee_list.update()
        bee_hit_list = arcade.check_for_collision_with_list(self.ladybug_sprite, self.bee_list)
        for bee in bee_hit_list:
            bee.remove_from_sprite_lists()
            self.score += 1
            
        
def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()