controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, mySprite, 200, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    mySprite2.destroy()
    mySprite2.destroy(effects.fire, 100)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    mySprite2.destroy()
    info.changeLifeBy(-1)
})
let mySprite2: Sprite = null
let projectile: Sprite = null
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite.setFlag(SpriteFlag.StayInScreen, true)
info.setLife(3)
controller.moveSprite(mySprite, 150, 150)
game.onUpdateInterval(500, function () {
    mySprite2 = sprites.create(img`
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
        `, SpriteKind.Enemy)
    mySprite2.setVelocity(-100, 0)
    mySprite2.left = scene.screenWidth()
    mySprite2.y = randint(0, scene.screenHeight())
    mySprite2.setFlag(SpriteFlag.AutoDestroy, true)
})
