import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2.0:
            return n
        z = z * z + c
    return max_iter

def G_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter, steps):
    mandelbrot_images = []
    step_size = max_iter // steps

    for step in range(1, steps + 1):
        current_max_iter = step * step_size
        mandelbrot_image = np.zeros((width, height))
        

        for x in range(width):
            for y in range(height):
                zx, zy = x * (x_max - x_min) / (width - 1) + x_min, y * (y_max - y_min) / (height - 1) + y_min
                c = zx + zy * 1j
                mandelbrot_image[x, y] = mandelbrot(c, current_max_iter)
  
        mandelbrot_images.append(mandelbrot_image)
    print(mandelbrot_images)
    return mandelbrot_images

# Función para actualizar la imagen en cada frame de la animación
def update(frame):
    im.set_array(mandelbrot_images[frame])
    ax.set_title(f'Iteration: {(frame + 1) * step_size}')
    return [im]

if __name__ == "__main__":
    # Parámetros para generar el fractal de Mandelbrot
    width =1000
    height = 1000
    x_min = -2.0
    x_max = 1.0
    y_min = -1.5
    y_max = 1.5
    max_iter = 500
    steps = 50 
    step_size = max_iter // steps

    mandelbrot_images = G_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter, steps)

    fig, ax = plt.subplots()
    im = ax.imshow(mandelbrot_images[0].T, extent=(x_min, x_max, y_min, y_max), cmap='jet')

    ani = animation.FuncAnimation(fig, update, frames=steps, interval=50, blit=True)
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.title('Mandelbrot Fractal Generation')
    plt.show()
