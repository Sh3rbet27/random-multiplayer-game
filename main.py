def on_a_pressed():
    scene.set_background_color(0)
    game.splash("W,A,S,D to move player 1", "I,J,K,L to move player 2")
    game.splash("Press \"A\" to begin")
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    info.player2.change_score_by(1)
    tacos_from_Mexico.set_position(randint(10, 120), randint(10, 120))
sprites.on_overlap(SpriteKind.enemy, SpriteKind.food, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.player1.change_score_by(1)
    tacos_from_Mexico.set_position(randint(10, 120), randint(10, 120))
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

tacos_from_Mexico: Sprite = None
scene.set_background_color(9)
player1 = sprites.create(assets.image("""
    woodguy
"""), SpriteKind.player)
controller.move_sprite(player1, 100, 100)
player1.set_scale(1.5, ScaleAnchor.MIDDLE)
player1.set_position(29, 85)
player2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . 5 . . . . . 
            . . . . . . b b b 5 5 5 . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . b b b b b 5 5 5 5 5 5 5 b . . 
            . b c 5 5 5 5 5 5 5 5 5 5 b . . 
            . . c 5 5 5 5 5 5 f 5 5 4 f . . 
            . . b c 5 5 5 5 f f 5 4 4 f . . 
            c c d c 5 5 5 5 f 5 4 4 4 4 4 b 
            c d d c 5 5 5 5 5 4 4 4 4 4 b . 
            c d d d c 5 5 5 5 5 5 5 5 5 b . 
            c c d d d d d 5 5 5 5 5 5 5 b . 
            . c d d d d d d 5 5 5 5 5 5 b . 
            . . c c d d d d c 5 5 5 b b . . 
            . . . c c c c c c c c b b . . .
    """),
    SpriteKind.enemy)
player2.set_scale(1.5, ScaleAnchor.MIDDLE)
player2.set_position(125, 80)
controller.player2.move_sprite(player2)
player1.set_bounce_on_wall(True)
player2.set_bounce_on_wall(True)
tacos_from_Mexico = sprites.create(img("""
        ..............eeeeeee...........
            ............ee455662e2e.........
            ..........ee45556723e2688.......
            .........e46776677232e777778....
            ........e46745554772227777778...
            .......4448744444777777777778...
            ......4722e7777777777777777778..
            .....4773277777722e777eeeee888..
            ....457722777772322e4555dddd48..
            ...44577777554723e455ddddddddd4.
            ...e66774554477e4555ddd55554dd44
            ..e46777444777e555555555555dddd4
            ..e5677777777e555555555555555dde
            .e4557777777e55555555555555555de
            .e554e77777e555555555555555d54de
            .e55eee77775d5555555555555ddddde
            e454eeeee745d555555555555d4ddde.
            e5e4eeeeee5d5555555555555dddde..
            e5ee4eeee45d555555555555dddde...
            e5eeeeeee5d55555555555d5ddde....
            e5ffefeee5d55555555555ddd4e.....
            e5ffffffe5d555555555d4ddee......
            e54efeff45d55555555dddde........
            e5eeeffe5dd5555555dddee.........
            e4eeefff5d5555555ddde...........
            e4efefff5d5d55555d4e............
            .e4efffe5d555555dee.............
            .e54eeee5d545dd4e...............
            ..e554ee5dddddee................
            ...ee5544dddee..................
            .....eeeeeee....................
            ................................
    """),
    SpriteKind.food)
tacos_from_Mexico.set_scale(0.6, ScaleAnchor.MIDDLE)
tacos_from_Mexico.set_position(randint(10, 120), randint(10, 120))
info.player1.set_score(0)
info.player2.set_score(0)