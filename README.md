# Fractal-Terrain-Generator-Python

![Example](https://i.imgur.com/IrAuogB.png)

This generator works on the princiles described here:
https://en.wikipedia.org/wiki/Fractal_landscape

The generator creates a two dimensional array of points representing a plane.
It then draws a series of lines intersecting the plane which then raise one half of the terrain by +1 and the other half by -1.

Prforming the line making operation many times and applying a "Terrain" color filter to the resulting height values will give an interesting looking terrain.

# Requierments

Matplotlib and Numpy
