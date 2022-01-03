def setup():
    size(500, 500)
    background(0)
    
def draw():
    
    for i in range(0, 10, 1):
        # draw stars
        
        b = random(0, 255)
        stroke(255, 255, b)
        fill(255, 255, b)
        
        circle(random(0, 500), random(0, 500), randomGaussian() + 1)
        
        # remove stars
        
        stroke(0)
        fill(0)
        for j in range(1, 1000):
            circle(random(0, 500), random(0, 500), .1)
        
        
    
