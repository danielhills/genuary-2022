def setup():
    size(500, 500)
    background(0)
    noLoop()
    
def draw():

    for i in range(10000):
        x = 250 + randomGaussian() * 60
        y = 250 + randomGaussian() * 60
        
        r = sqrt(abs(250 - x) ** 2 + abs(250 - y) ** 2) + randomGaussian() * 50

        if r < 50:
            stroke(x, x, 0, 60)
        elif r < 100:
            stroke(x, 0, x, 80)
        else:
            stroke(0, x, x, 100)
            
        circle(x, y, 1)

    saveFrame("day1.png")
        
    
