from sprite_object import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = "resources/sprites/static_sprites/"
        self.anim_sprite_path = "resources/sprites/animated_sprites/"
        add_sprite = self.add_sprite

        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game, pos=(1.1, 1.1)))
        add_sprite(AnimatedSprite(game, pos=(15.9, 1.1)))
        add_sprite(AnimatedSprite(game, pos=(15.9, 8.9)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + "red_light/0.png", pos=(10.1, 4.1)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + "red_light/0.png", pos=(3.8, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + "red_light/0.png", pos=(11.8, 2.8)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + "red_light/0.png", pos=(7.5, 4.1)))



    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)