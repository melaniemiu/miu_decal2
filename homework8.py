
# # Question 1.1
# import numpy as np
# import matplotlib.pyplot as plt

# def make_sin_wave(x, A, w):
#     return A * np.sin(w * x)

# # Question 1.2
# x = np.linspace(0, 2* np.pi, 1000)

# # Question 1.3
# amplitudes = np.array([0.5, 1, 1.5, 2, 2.5])
# frequencies = np.array([1,2,3,4,5])
# line_styles = ['-', '--', '-.', ':', (0, (3,1,1,1))] #this creates 5 different types of line styles

# # Question 1.4
# fig = plt.figure(figsize=(10,6))

# # Question 1.5
# for A,w, style in zip(amplitudes, frequencies, line_styles):
#     y = make_sin_wave(x,A,w)
#     plt.plot(x,y, linestyle=style, label= f"A={A}, w={w}") #tells matplotlib HOW to draw your lines
    
# # Question 1.6
# plt.title("Sine Wave")
# plt.xlabel("Sine Values")
# plt.ylabel("y = A * np.sin(w * x)")
# plt.grid(True) # adds the gridlines
# plt.legend() # this shows a box explaining each line
# plt.show() # displays the actual curve

# Question 2.1
import pandas as pd
stars = pd.read_csv('stars.csv')

# Question 2.2
for row in stars:
    df = pd.DataFrame(stars)
    print(df.head(5))

