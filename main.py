def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 2 . . . . . . . . . . . 
                    . . . . 2 2 3 3 3 3 . . . . . . 
                    . . . . 2 2 3 3 3 3 . . . . . . 
                    . . . . 2 . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    mySprite2.destroy()
    mySprite2.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    mySprite2.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

mySprite2: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . 2 . . . . . . . . . . 
            . . . . . 8 2 . . . . . . . . . 
            . . . . 8 2 8 2 . . . . . . . . 
            . . . . . . 2 8 2 . . . . . . . 
            . . . 2 2 8 2 2 8 2 . . . . . . 
            . . . . . . 2 8 2 . . . . . . . 
            . . . . 8 2 8 2 . . . . . . . . 
            . . . . . 8 2 . . . . . . . . . 
            . . . . . 2 . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
mySprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(3)
controller.move_sprite(mySprite, 150, 150)

def on_update_interval():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . 3 . . . . . . . . . . . . 
                    . . . 3 3 3 . . . . . . . . . . 
                    . . . 3 2 9 3 . . . . . . . . . 
                    . . . 3 . 2 9 3 . . . . . . . . 
                    . . 3 3 2 9 2 9 3 . . . . . . . 
                    . 3 3 2 9 2 9 2 9 3 . . . . . . 
                    . . 3 3 2 9 2 9 3 . . . . . . . 
                    . . . 3 . 2 9 3 . . . . . . . . 
                    . . . 3 2 9 3 . . . . . . . . . 
                    . . . 3 3 3 . . . . . . . . . . 
                    . . . 3 . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    mySprite2.set_velocity(-100, 0)
    mySprite2.left = scene.screen_width()
    mySprite2.y = randint(0, scene.screen_height())
    mySprite2.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update_interval)
