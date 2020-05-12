from fractal.rules import settings
from fractal import processor
import painter

if __name__ == '__main__':
    for fractal in settings:
        string = processor.process_fractal(fractal)
        print("Fractal '{}' after {} iterations is: {}".format(fractal['name'], fractal['n'], string))
        if fractal['name'] == 'Plant':
            painter.draw_fractal(string, fractal, 4)
