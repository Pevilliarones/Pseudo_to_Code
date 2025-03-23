from turtle import *
from random import randrange
from freegames.utils import vector, square

# Başlangıç değişkenleri
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Oyun durumunu kontrol etmek için bir bayrak
game_running = True


# Hareket yönünü değiştirme fonksiyonu
def change(x, y):
    if game_running:  # Sadece oyun çalışıyorsa hareket etsin
        aim.x = x
        aim.y = y


# Yılanın oyun alanı içinde olup olmadığını kontrol eder
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190


# Oyunu sıfırlama fonksiyonu
def reset_game():
    global snake, food, aim, game_running
    snake = [vector(10, 0)]  # Yılanı başlangıç pozisyonuna getir
    food = vector(0, 0)  # Yemi başlangıç pozisyonuna getir
    aim = vector(0, -10)  # Hareket yönünü başlangıç değerine getir
    game_running = True  # Oyunu yeniden başlat
    move()  # Oyunu başlat


# Yılanı hareket ettirme fonksiyonu
def move():
    global game_running

    if not game_running:  # Eğer oyun bitmişse hareket etmeyi durdur
        return

    head = snake[-1].copy()  # Yılanın başını kopyala
    head.move(aim)  # Yeni yön ile yılanı hareket ettir

    if not inside(head) or head in snake:  # Yılan duvara ya da kendine çarptı mı?
        print("Game Over!")
        square(head.x, head.y, 9, 'red')  # Yılanın kafasını kırmızı yap
        update()
        game_running = False  # Oyunu durdur
        return

    snake.append(head)  # Yeni başı yılanın bir parçası yap

    if head == food:  # Yem yendi mi?
        print("Yem Yendi!")
        food.x = randrange(-15, 15) * 10  # Yeni yemi rastgele yerleştir
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)  # Yılan yemek yemezse sadece hareket eder (kuyruk kısalır)

    clear()

    # Yılanı çiz
    for segment in snake:
        square(segment.x, segment.y, 9, 'green')

    # Yemeği çiz
    square(food.x, food.y, 9, 'red')
    update()

    ontimer(move, 100)  # 100ms sonra tekrar hareket fonksiyonunu çağır


# Tuş kontrolleri
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')  # Sağ
onkey(lambda: change(-10, 0), 'Left')  # Sol
onkey(lambda: change(0, 10), 'Up')  # Yukarı
onkey(lambda: change(0, -10), 'Down')  # Aşağı
onkey(reset_game, 'space')  # Oyunu yeniden başlatmak için space tuşunu bağla

move()  # Oyunu başlat
done()
