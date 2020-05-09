from rules import settings
import processor
import drawer

if __name__ == '__main__':
    for fractal in settings:
        string = processor.process_fractal(fractal)
        print("Fractal '{}' after {} iterations is: {}".format(fractal['name'], fractal['n'], string))
        if fractal['name'] == 'Koch Curve':
            drawer.draw_fractal(string, fractal, 5)
