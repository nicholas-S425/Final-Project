from p5 import *
import random

# select the interpereter as like 3.11.15 or somethig the homebrew one
player_img = None
map_img = None
player_jump = None
player_walk_left = []
player_walk_right = []
coin = []
font_04b = None
projectile = None
jump = False
walk = False
opacity = 100
flash = False
score = 0
ItemCounter = 0
items = []
parallax1 = None
projectiles = []
wormguy_img= None
class MovingMap:
    def __init__(self):
        self.w = 1300
        self.h = 1300
        self.x = -500
        self.y = -400
        self.vel = {"x": 0, "y": 0}

class Player:
    def __init__(self):
        self.w = 200  
        self.h = 200  
        self.x = 350
        self.y = 283 
        self.strength = 8
        self.gravity = 0.5
        self.direction = "right" 

class Worm:
    def __init__(self):
        self.w = 200  
        self.h = 200  
        self.x = 500
        self.y = 610
        self.health =100

player = Player()
game_map = MovingMap()
wormguy=Worm()
walk_speed = 0
image_speed = 0

def setup():
    global player_img, map_img, player_jump, player_walk_left, player_walk_right, coin, font_04b, projectile, parallax1, wormguy_img
    size(700, 500)
    wormguy_img=load_image('/Users/nicschl29/Downloads/pixil-frame-0 (29).png')
    player_img = load_image('/Users/nicschl29/Downloads/characteranims/standing_scaled_13x_pngcrushed.png')
    player_jump = load_image('/Users/nicschl29/Downloads/characteranims/jumping_scaled_13x_pngcrushed.png')
    projectile = load_image('/Users/nicschl29/Downloads/pixil-frame-0 (27)_scaled_96x_pngcrushed.png')
    player_walk_left = [
        load_image('/Users/nicschl29/Downloads/characteranims/walkleft1_scaled_13x_pngcrushed.png'),
        load_image('/Users/nicschl29/Downloads/characteranims/walkleft2_scaled_13x_pngcrushed.png')
    ]
    
    player_walk_right = [
        load_image('/Users/nicschl29/Downloads/characteranims/walkright1_scaled_13x_pngcrushed.png'),
        load_image('/Users/nicschl29/Downloads/characteranims/walkright2_scaled_13x_pngcrushed.png')
    ]
    parallax1 = load_image('/Users/nicschl29/Downloads/pixil-frame-0 (26)_scaled_10x_pngcrushed.png')
    map_img = load_image('/Users/nicschl29/Downloads/pixil-frame-0 (30).png')
    coin = [
        load_image('/Users/nicschl29/Downloads/pixilart-frames (4) 2/pixil-frame-0_scaled_96x_pngcrushed.png'),
        load_image('/Users/nicschl29/Downloads/pixilart-frames (4) 2/pixil-frame-1_scaled_96x_pngcrushed.png'),
        load_image('/Users/nicschl29/Downloads/pixilart-frames (4) 2/pixil-frame-2_scaled_96x_pngcrushed.png'),
        load_image('/Users/nicschl29/Downloads/pixilart-frames (4) 2/pixil-frame-3_scaled_96x_pngcrushed.png')
    ]
    font_04b = load_font('/Users/nicschl29/Downloads/bytebounce.medium.ttf')
    image(map_img, -9999, -9999)
    image(player_img, -9999, -9999)
    image(player_jump, -9999, -9999)
    image(player_walk_left[0], -9999, -9999)
    image(player_walk_left[1], -9999, -9999)
    image(player_walk_right[0], -9999, -9999)
    image(player_walk_right[1], -9999, -9999)
    image(coin[0], -9999, -9999)
    image(coin[1], -9999, -9999)
    image(coin[2], -9999, -9999)
    image(coin[3], -9999, -9999)
    image(parallax1, -9999, -9999)
    image(projectile, -9999, -9999)
    image(wormguy_img,-99999,-99999)
def render(player, game_map, parallax1):
    global walk_speed, ItemCounter, image_speed, score, opacity, flash, wormguy
    image(parallax1, game_map.x/2, (game_map.y/2)+90, game_map.w-200, game_map.h-200)
    image(wormguy_img, (game_map.x/1.1) + wormguy.x, game_map.y + (wormguy.y/1.1), wormguy.w, wormguy.h)
    if wormguy.health<=0:
        wormguy.y=-100000
    for p in projectiles[:]: #yeath this part was half vibe coded shut up
        p['x'] += p['vx']
        p['y'] += p['vy']
        p['vy'] += 0.3
        
        worm_screen_x = (game_map.x / 1.1) + wormguy.x
        worm_screen_y = game_map.y + (wormguy.y / 1.1)
        rel_x = p['x'] - worm_screen_x
        rel_y = p['y'] - worm_screen_y
            

        if 0 < rel_x < wormguy.w and 0 < rel_y < wormguy.h:
            p['vx'] *= -1
            p['vy'] *= -1
            tint(255, 0, 0)
            wormguy.health=wormguy.health-1
            image(wormguy_img, worm_screen_x, worm_screen_y, wormguy.w, wormguy.h)
            no_tint()
            continue
        
        if p['y'] > 600 or p['x'] < -100 or p['x'] > 800:
            projectiles.remove(p)
        else:
            px = p['x'] - p['s'] / 2
            py = p['y'] - p['s'] / 2
            image(projectile, px, py, p['s'], p['s'])
    for i in items:
        i['x'] += game_map.vel['x']
        i['y'] += game_map.vel['y']
        i['y'] += 1
        
        if abs(i['x'] - player.x) < 20 and abs(i['y'] - player.y) < 40:
            items.remove(i)
            score = score + 1
            opacity = 100
            flash = True
        elif i['y'] > 500:
            items.remove(i)
        else:
            coin_draw_x = i['x'] - (i['s'] / 2)
            coin_draw_y = i['y'] - (i['s'] / 2)
            image(coin[int(image_speed)%4], coin_draw_x, coin_draw_y, i['s'], i['s'])
    if image_speed >= 4:
        image_speed = 0
    image_speed += 0.21
    if game_map.x > 312:
        game_map.x = 312
        game_map.vel['x'] = 0
    if game_map.x < -940:
        game_map.x = -940
        game_map.vel['x'] = 0
    p_draw_x = player.x - (player.w / 2)
    p_draw_y = player.y - (player.h / 2)
    
    if jump:
        image(player_jump, p_draw_x, p_draw_y, player.w, player.h)
    elif walk:
        if player.direction == "left":
            image(player_walk_left[int(walk_speed)], p_draw_x, p_draw_y, player.w, player.h)
        else:
            image(player_walk_right[int(walk_speed)], p_draw_x, p_draw_y, player.w, player.h)
            
        walk_speed += 0.12
        if walk_speed >= 2:
            walk_speed = 0
    else:
        image(player_img, p_draw_x, p_draw_y, player.w, player.h)
        
    if ItemCounter >= 1:
        ItemCounter = 0
        items.append({'x': random.randint(300+game_map.x, 1000+game_map.x), 'y': 0, 's': 70})
    ItemCounter += 0.01
    
    if flash == True:
        no_stroke()
        fill(255, 255, 255, opacity)
        rect(0, 0, 10000, 10000)
        opacity -= 10
    if opacity < 0:
        flash = False  
    image(map_img, game_map.x, game_map.y, game_map.w, game_map.h)

def move(game_map):
    global jump
    game_map.x += game_map.vel['x']
    game_map.y += game_map.vel['y']
    if jump:
        game_map.vel["y"] -= player.gravity
    if game_map.y <= -400:
        game_map.y = -400
        game_map.vel["y"] = 0
        jump = False
    fill(255)
    text_font(font_04b)
    text_size(50)
    text(f"Waffles (toast): {score}", 50, 10)
    text(f"Health: {wormguy.health}", 400, 10)
def key_pressed(evt):
    global walk, jump, score
    if evt.key == "RIGHT" or evt.key == "D":
        game_map.vel["x"] -= 3
        walk = True
        player.direction = "right"
    elif evt.key == "LEFT" or evt.key == "A":
        game_map.vel["x"] += 3
        walk = True
        player.direction = "left"
        
    if evt.key == "UP" or evt.key == "W":
        if not jump:
            jump = True
            game_map.vel["y"] = player.strength

    if evt.key == "C":
        score = 999999

def key_released(evt):
    global walk
    if evt.key == "LEFT" or evt.key == "RIGHT" or evt.key == "A" or evt.key == "D":
        walk = False
        game_map.vel["x"] = 0
def mouse_pressed(evt):
    global score
    if game_map.x>-378 and game_map.x<-165:
        print("no")
        return
    elif score > 0:
        score -= 1
        dx = mouse_x - player.x
        dy = mouse_y - player.y
        dist = (dx**2 + dy**2) ** 0.5
        if dist == 0:
            dist = 1
        speed = 10
        projectiles.append({
            'x': player.x,
            'y': player.y,
            's': 70,
            'vx': (dx / dist) * speed,
            'vy': (dy / dist) * speed
        })
def draw():
    clear()
    background(242, 218, 150)
    render(player, game_map, parallax1)
    move(game_map)
    text(f"gamemap: {game_map.x}, {game_map.y}", 50, 70)
run()