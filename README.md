# Starmie
A\* algorithm implementation

　　　　　　　　　　　　　　　　　　　　　　▅██▅  
　　　　　　　▅▅▅　　　　　　　　　　　█▓█　　█　　　　　　▅▅▅  
　　　　　　　█　　▀▀▅▅　　　　　　█▓█　　　　█　　　▅▀▅▀　█  
　　　　　　　█▓▓　　　　▀▀▅▅　█▓█　　　　　　█▅▀▅▀　　▓█  
　　　　　　　██▓▓　　　　　　▓█▓█　　　▅▀▀▅　█▀　　　▓▓█  
　　　　　　　█▓█▓▓　　　　▓█▓█　　　　█▓　█　　█　　▓▓▓█  
　　　　　　　　█▓█▓▓　▅▅█▓█　　▅▅█▓▓　　█▅　▀▅▅▅▅█▅▅▅  
　　　　　　▅▅██▓███▓　　▀▅▅▀　　　▅▅▅▅▅▅▀▅▀　　▓█　　　▀▀▀▀▅  
　▅▅▀▀▀▀　　　　　▀██▓　　　　　　▅▀▅▅　▅▅▅▀▅　　▓█▓　　　　　　　█  
▀█▅　　　　　　　　　　　▀█▓　　　▅▀　▅▀▅▀　　　▀　▀▅▀█▓▓　　　　▅▀  
　　▀█▓▅　　　　　　　　▅▀　　▅▀　▅██▀▅████▅▀▅　▓　█▓▓　　▅▀  
　　　　█▓▓▅　　　▅▅█　　　　▓　█▅▅　████▀▀██▅　█▓▀█▓▓▀  
　　　　　█▓▓█▀▀　　　　　　　█　███▓██▓▓　　█▀█　█▓　　▀▀▅  
　　　　　▅▀██▓▓▓▓▓▓▓▓▓█　███▓██▓▓▓████▓█▓▓▓▓█　　　▀▀▅  
　　　▅▀　　　▀██▀▀█▓▓▓▓▓　▅▅▅█▅▀█████▀▅██　█▀　　　　　█  
　▅▀　　　　▅█▓▀　　　█▓▓　　█　▀███▀▅▅▅▅▅█▀█　▅▀▓▓▓▓▓▅▀  
█　　　　▓▓█▓█　　　　▓█　　　▀▓▅　▀▅████▓▀▅▀▅▀　　█▓▓▓▀  
　▀▓▓▓▓█▓█　　　　　▓▀　　　▓▓　▀▓▅▅▅▅▅▅▀▓▓　▀▅　　█▀  
　　　▀▀▓█▓█　　　　█　　　▅██▅▅▓▓▓　　　▅▅██▓▓　█　　█  
　　　　　█▓█　　　　▓█▅▅▀　　　▀▓█▓▓　　█▓▓▓　　▀▀▀　　　█  
　　　　　█▓▀　　　▓▓▓　　　　▅▅████▓　███▓▓▓▅▅　　　　　█  
　　　　　　█　　　▓▓▓▅▅▅▀▀████▓██▓█▀　　　　　　▀▀▀▀▀  
　　　　　　　▀▀▀▀▀　　　　　　　▀█▓█▓▓▀  
　　　　　　　　　　　　　　　　　　　▀▀▀  

## Install
``` console
$ pip install starmie
```

## Usage
0. Define class and extends [AStarProblem](/starmie.py)
0. Define some methods
    - Required: `get_start` `is_goal` `get_neighbors`
    - Recommended: `get_path_cost` `estimate_heuristic_cost`
0. Create object and call `solve()`

For details, see test scripts.

- [Maze](/tests/test_maze.py)
- [Graph](/tests/test_graph.py)

## Test
``` console
$ python -m unittest discover tests
```
