import joblib
import numpy as np
from sklearn.svm import LinearSVC
from grid_solver import parse_grid, show_digits


GRID_PATH = 'tests/grid.png'
digits = parse_grid(GRID_PATH)
clf = joblib.load('classifier.pkl')
grid = []
for d in digits:
    num = clf.predict(np.reshape(d, (1,-1)))    
    grid.append(num)
grid = np.reshape(grid, (9,9))
print(grid)