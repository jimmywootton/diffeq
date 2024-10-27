import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
import math  # Optional
import numpy as np  # Optional
import latexify

#latexify.__version__


def dSdx(x, S):
	y1, y2 = S
    
    
    
    
    #variable
	m = 1
	D = 0.1

	#constant
	p = 1.204
	μ=18.8








	return [(-0.5*y1**2)/(math.sqrt(y1**2+y2**2)*m),
    	(-0.5*y1**2)/(math.sqrt(y1**2+y2**2)*m)-9.8]
v_0 = 10
a = 45
y1_0 = v_0*math.cos(math.radians(a))
y2_0 = v_0*math.sin(math.radians(a))
S_0 = (y1_0, y2_0)



x = np.linspace(0,2*v_0*math.sin(math.radians(a))/9.8 , 100)
sol = odeint(dSdx, y0=S_0, t=x, tfirst=True)


y1_sol = sol.T[0]
y2_sol = sol.T[1]

y1_int = integrate.cumulative_trapezoid(y1_sol, x, initial=0)
y2_int = integrate.cumulative_trapezoid(y2_sol, x, initial=0)

x_1 = y1_0*x 
x_2 =y2_0*x - 0.5*9.8*(x**2)

y = x*math.tan(math.radians(a))-((9.8*(x**2))/(2*(v_0**2)*(math.cos(math.radians(a)))**(2)))


plt.plot(y1_int, y2_int)
plt.plot(x_1, x_2)
plt.show()


# @latexify.function
# def solve(r):
#   return []

# #print(solve(1, 4, 3))  # Invoking the function works as expected.
# print(solve)  # Printing the function shows the underlying LaTeX source.
# solve  # Displays the expression.

# # Writes the underlying LaTeX source into a file.
# with open("compiled.tex", "w") as fp:
#   print(solve, file=fp)

#[(24/r) + ((2.6/5)*r)/(1+(r/5)**1.52) + (0.411*(r/(2.63*10**5))**(-7.94)/(1+(r/(2.63*10**5))**(-8))) + ((0.25/10**6)*r)/(1+(r/10**6))]

#return [(-0.5*y1**2)/(math.sqrt(y1**2+y2**2)*m),
  #         (-0.5*y1**2)/(math.sqrt(y1**2+y2**2)*m)+g]