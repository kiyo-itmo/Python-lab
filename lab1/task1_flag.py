
CSI = '\x1b['
RED= CSI +"41m"  # красный фон
WHITE= CSI +"107m" # белый фон
RESET= CSI +"0m"   # сброс цвета

def draw_flag(stripe_height=6, width=30):
    # Верхняя полоса — белая
    for _ in range(stripe_height):              
         print(WHITE + " " * width + RESET)

     # Нижняя полоса — красная
    for _ in range(stripe_height):
        print(RED + " "*width + RESET)   

if __name__== "__main__":
    draw_flag()