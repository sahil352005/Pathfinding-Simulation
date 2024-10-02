
---

# Pathfinding Algorithm Visualizer

This is a visualizer tool for various pathfinding algorithms, implemented using **Pygame**. It allows you to see how algorithms like A*, Dijkstra, Breadth-First Search (BFS), and Depth-First Search (DFS) explore the grid to find the shortest path between two points. The tool also includes interactive features to create barriers, reset the grid, and choose the algorithm.

## Features

- **Visualization of Algorithms**: Visualize A*, Dijkstra, BFS, and DFS in real-time.
- **Interactive Grid**: Click to create barriers, set start/end points, and reset the grid.
- **Algorithm Selection**: Choose the pathfinding algorithm from a dropdown menu.
- **User Controls**:
  - **Left Click**: Set the start, end, and barriers on the grid.
  - **Right Click**: Remove barriers or reset points.
  - **Run Button**: Start the selected algorithm.
  - **Reset Button**: Reset the grid and start a new simulation.

## Algorithms

- **A***: A heuristic-based algorithm that combines the cost to reach a node and the estimated cost to reach the goal.
- **Dijkstra**: A classic algorithm that guarantees the shortest path in a weighted grid (works the same as A* without a heuristic).
- **Breadth-First Search (BFS)**: Explores all possible paths one step at a time, ensuring the shortest path in unweighted grids.
- **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking. Does not guarantee the shortest path.

## Prerequisites

- Python 3.x
- Pygame

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sahil352005/Pathfinding-Simulation.git
    ```

2. Install Pygame:

    ```bash
    pip install pygame
    ```
    or

   ```bash
   python -m pip install pygame-ce
   ```

4. Run the script:

    ```bash
    python main.py
    ```

## Usage

1. **Set start and end points**: Use the left mouse button to place the start (orange) and end (turquoise) points.
2. **Create barriers**: Use the left mouse button to draw barriers (black) that the pathfinder cannot pass through.
3. **Run the algorithm**: Select an algorithm from the dropdown menu, then click the "Run" button to see the visualization.
4. **Reset the grid**: Click the "Reset" button to clear the grid and start a new simulation.

### Controls

- **Left Click**: Set the start, end, and barriers.
- **Right Click**: Reset grid cells.
- **'C' Key**: Clear the entire grid.
- **Run Button**: Execute the chosen algorithm.
- **Reset Button**: Reset the grid and simulation.

## Screenshots

![Screenshot 2024-10-02 075139](https://github.com/user-attachments/assets/7f0d834b-bf45-4412-9ffc-1b9e95c4a140)

![Screenshot 2024-10-02 075342](https://github.com/user-attachments/assets/7c5066c2-eb4e-4cbf-b852-1a1556d389d7)

![Screenshot 2024-10-02 075940](https://github.com/user-attachments/assets/017c4136-10c1-4f82-945f-1ca4792cfaf7)


## Known Issues

- The simulation may not reset entirely if run multiple times. This can be resolved by pressing the **Reset** button before starting a new algorithm run.

## Future Enhancements

- Add more pathfinding algorithms (e.g., Greedy Best-First Search).
- Allow diagonal movement between grid cells.
- Implement weighted grids with varying terrain costs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
## Contributors
- https://github.com/Lonwwolf14
