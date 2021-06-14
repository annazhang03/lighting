import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represented by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    normalize(normal)
    normalize(light[LOCATION])
    normalize(view)
    I_a = calculate_ambient(ambient, areflect)
    I_d = calculate_diffuse(light, dreflect, normal)
    I_s = calculate_specular(light, sreflect, view, normal)
    return limit_color([I_a[i] + I_d[i] + I_s[i] for i in [0,1,2]])

def calculate_ambient(alight, areflect):
    return [alight[i] * areflect[i] for i in [0,1,2]]

def calculate_diffuse(light, dreflect, normal):
    NL = dot_product(normal, light[LOCATION])
    return [dreflect[i] * NL * light[COLOR][i] for i in [0,1,2]]

def calculate_specular(light, sreflect, view, normal):
    NL = dot_product(normal, light[LOCATION])
    R = [2 * NL * normal[i] - light[LOCATION][i] for i in [0,1,2]]
    RV = dot_product(R, view)
    return [sreflect[i] * light[COLOR][i] * RV ** SPECULAR_EXP for i in [0,1,2]]

def limit_color(color):
    return [int(255 if c > 255 else 0 if c < 0 else c) for c in color]

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]
    '''print(i)
    print(A)
    print(polygons)'''
    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]
    #print(i)
    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
