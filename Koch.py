from turtle import *

def koch(num, step):
    """Argumenty(2): num - rząd krzywej, step - długość jednego kroku
    Funkcja rysuje krzywą Kocha rekurencyjnie. Zwraca błąd jeśli num nie jest liczbą całkowitą lub jest mniejsze od zera.
     """

    angles = [60, -120, 60, 0]

    if num<0 or not (float(num)).is_integer():  ## is_integer() działa dla float, zadziała np. dla 5.0
        raise IndexError("Variable n should be an integer higher than 0.")

    if num == 0:
        forward(step)
    else:
        for i in angles:
            koch(num-1, step // 3)
            left(i)
        
def draw(num):
    """Argumenty(1): num - rząd krzywej
    Funkcja rysuje krzywą Kocha rekurencyjnie z wykorzystaniem powyższej funkcji koch. 
    Przekazuje do niej rozmiar, pozycję początkową żółwia oraz ustawia długość kroku równą 1/3 rozmiaru."""
    size = 1000
    penup()
    goto(-150,0)
    pendown()
    koch(num, size//3)
    done()



if __name__ == "__main__":
    draw(4)
