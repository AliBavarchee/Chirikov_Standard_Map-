# -*- coding: utf-8 -*-
'''

# Poincaré map of Chirikov–Taylor map Visualizations
---
'''

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.models import ColorBar, LinearColorMapper
from bokeh.palettes import Viridis256
from bokeh.transform import linear_cmap
from bokeh.palettes import Viridis256
from bokeh.io import export_png
from bokeh.io import output_notebook
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
from bokeh.plotting import figure, output_file, save
from bokeh.models import LinearColorMapper, ColorBar
from bokeh.palettes import Viridis256
from bokeh.io import export_png
import kaleido

# Load data from the Fortran output file
data = np.loadtxt('chirikov_map_data.txt')
p = data[:, 0]
x = data[:, 1]

assert x.shape == p.shape, "x and p must be of the same shape."
colmaps = ['red', 'green', 'blue', 'gold', 'purple', 'orange', 'cyan']*1000
# Poincaré map
plt.figure(figsize=(8, 8))
plt.scatter(x, p, s=0.5, color=colmaps, alpha=1)
plt.title('Poincaré Map of the Chirikov Standard Map')
plt.xlabel('Displacement (x)')
plt.ylabel('Momentum (p)')
plt.xlim(0, 2 * np.pi)
plt.ylim(-np.pi, np.pi)
plt.grid(True)
plt.show()

# Create a scatter plot for the Poincaré map by plotly
fig = go.Figure(data=go.Scattergl(x=x, y=p, mode='markers', marker=dict(size=2, color='blue', opacity=0.6)))

fig.update_layout(
    title='Poincaré Map of the Chirikov Standard Map',
    xaxis=dict(title='Displacement (x)', range=[0, 2 * np.pi]),
    yaxis=dict(title='Momentum (p)', range=[-np.pi, np.pi]),
    width=800,
    height=800)
fig.show()

num_bins = 100

# 2D hist
hist, xedges, yedges = np.histogram2d(x, p, bins=num_bins, density=True)

# Get meshgrid
X, Y = np.meshgrid(xedges[:-1], yedges[:-1])

# Plotting the Poincaré surface of section as a contour plot
plt.figure(figsize=(8, 8))
plt.contourf(X, Y, hist.T, levels=20, cmap='plasma')
plt.colorbar(label='Density')
plt.title("Poincaré Surface of Section")
plt.xlabel("Displacement (x)")
plt.ylabel("Momentum (p)")
plt.xlim(0, 2 * np.pi)
plt.ylim(-np.pi, np.pi)
plt.grid(True)
plt.show()

# Create a grid of points for contour plotting
p_min, p_max = min(p), max(p)
x_min, x_max = min(x), max(x)

# Adjust grid density based on array length
grid_density = 100

p_grid, x_grid = np.meshgrid(np.linspace(p_min, p_max, grid_density),
                             np.linspace(x_min, x_max, grid_density))

# Calculate the corresponding Hamiltonian values
H = p_grid**2 / 2 + np.cos(x_grid)

# Plot the contour lines
plt.contour(x_grid, p_grid, H, levels=21)
plt.xlabel("Displacement (x)")
plt.ylabel("Momentum (p)")
plt.title("Poincaré Map of Chirikov Standard Map")
plt.show()

# Create a grid of points for wind barbs plotting
p_min, p_max = min(p), max(p)
x_min, x_max = min(x), max(x)

# Adjust grid density
grid_density = 70

p_grid, x_grid = np.meshgrid(np.linspace(p_min, p_max, grid_density), np.linspace(x_min, x_max, grid_density))

u = np.sin(x_grid)
v = np.cos(p_grid)

# Create a plt
plt.figure(figsize=(10, 8))
plt.title("Poincaré Map with Wind Barbs")
plt.xlabel("Displacement (x)")
plt.ylabel("Momentum (p)")

# Add wind barbs!!! to the plot
plt.barbs(x_grid, p_grid, u, v, length=5)

plt.show()

# Create a grid of points for contour plotting
p_min, p_max = min(p), max(p)
x_min, x_max = min(x), max(x)

# Adjust grid density based on array length
grid_density = 7000

p_grid, x_grid = np.meshgrid(np.linspace(p_min, p_max, grid_density),
                             np.linspace(x_min, x_max, grid_density))

# Calculate the corresponding Hamiltonian values
H = p_grid**2 / 2 + np.cos(x_grid)

# Contour plot using Seaborn
plt.figure(figsize=(8, 8))
contour_plot = sns.heatmap(H, cmap='plasma', cbar=True, xticklabels=False, yticklabels=False)
contour_plot.set_xlabel('Displacement (x)')
contour_plot.set_ylabel('Momentum (p)')
contour_plot.set_title('Poincaré Map of Chirikov Standard Map')
plt.show()

# Create a grid of points
p_min, p_max = min(p), max(p)
x_min, x_max = min(x), max(x)

# Adjust grid density based on array length
grid_density = 7000 # len(x) = len(p) = 7000

p_grid, x_grid = np.meshgrid(np.linspace(p_min, p_max, grid_density),
                             np.linspace(x_min, x_max, grid_density))

# Hamiltonian values
H = p_grid**2 / 2 + np.cos(x_grid)

# Plot
plt.contour(x_grid, p_grid, H, levels=29, cmap='plasma')
plt.colorbar()
plt.xlabel("Displacement (x)")
plt.ylabel("Momentum (p)")
plt.title("Poincaré Map of Chirikov Standard Map")
plt.show()

p_min, p_max = min(p), max(p)
x_min, x_max = min(x), max(x)

# grid density
grid_density = 700

p_grid, x_grid = np.meshgrid(np.linspace(p_min, p_max, grid_density),
                             np.linspace(x_min, x_max, grid_density))

H = p_grid**2 / 2 + np.cos(x_grid)

# Bokeh figure
p = figure(title="Poincaré Map of Chirikov Standard Map",
           x_axis_label='Displacement (x)',
           y_axis_label='Momentum (p)',
           x_range=(x_min, x_max),
           y_range=(p_min, p_max),
           tools="pan,wheel_zoom,box_zoom,reset",
           width=800, height=800)

# Convert H to a format Bokeh can use for plotting
H_flat = H.flatten()
x_flat = x_grid.flatten()
p_flat = p_grid.flatten()

mapper = LinearColorMapper(palette=Viridis256, low=H.min(), high=H.max())

p.image(image=[H], x=x_min, y=p_min, dw=x_max-x_min, dh=p_max-p_min, color_mapper=mapper)

color_bar = ColorBar(color_mapper=mapper, width=8, location=(0,0))
p.add_layout(color_bar, 'right')

output_notebook()
show(p)

p_min, p_max = min(p), max(p)
x_min, x_max = min(x), max(x)

grid_density = 100

p_grid, x_grid = np.meshgrid(np.linspace(p_min, p_max, grid_density), np.linspace(x_min, x_max, grid_density))

H = p_grid**2 / 2 + np.cos(x_grid)

fig = go.Figure(data=go.Contour(z=H, x=np.linspace(x_min, x_max, grid_density), y=np.linspace(p_min, p_max, grid_density),
    colorscale='Viridis',
    contours=dict(
        showlines=True,
        coloring='lines',
        showlabels=True
    )
))

fig.update_layout(
    title='Contour Plot of the Hamiltonian',
    xaxis=dict(title='Displacement (x)'),
    yaxis=dict(title='Momentum (p)'),
    width=800,
    height=800
)
fig.show()