""" A simple Tetris clone for µGame 10 """
import ugame
import stage

bank = stage.Bank.from_bmp16("ball.bmp")
background = stage.Grid(bank)
ball = stage.Sprite(bank, 1, 8, 8)
game = stage.Stage(ugame.display, 12)
game.layers = [ball, background]
game.render_block()

while True:
    ball.set_frame(ball.frame % 15 + 1)
    game.render_sprites([ball])
    game.tick()
