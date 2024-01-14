import random

class Environment:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [[random.choice([0, 1]) for _ in range(grid_size)] for _ in range(grid_size)]

class VacuumCleaner:
    def __init__(self, grid_size):
        self.position = (0, 0)
        self.battery = 100
        self.clean_count = 0
        self.environment = Environment(grid_size)
        self.dirt_positions = [(i, j) for i in range(grid_size) for j in range(grid_size) if self.environment.grid[i][j] == 1]
        self.output_positions = []

    def move(self, direction):
        if direction == 'up' and self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])
        elif direction == 'down' and self.position[0] < self.environment.grid_size - 1:
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == 'left' and self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == 'right' and self.position[1] < self.environment.grid_size - 1:
            self.position = (self.position[0], self.position[1] + 1)

        self.battery -= 1

    def clean(self):
        if self.environment.grid[self.position[0]][self.position[1]] == 1:
            self.environment.grid[self.position[0]][self.position[1]] = 0
            self.clean_count += 1
            self.dirt_positions.remove(self.position)
            self.battery -= 1

    def print_dirt_positions(self):
        print("Dirt positions:", self.dirt_positions)

    def print_output_positions(self):
        print("Output positions:", self.output_positions)

def main():
    grid_size = 5
    vacuum = VacuumCleaner(grid_size)
    steps = 20

    vacuum.print_dirt_positions()
    vacuum.print_output_positions()

    print("\nCleaning Process:")

    while vacuum.dirt_positions:
        if vacuum.battery <= 0:
            print("Battery depleted. Exiting.")
            break

        if vacuum.position in vacuum.dirt_positions:
            print("Cleaning dirt")
            vacuum.clean()
        else:
            possible_moves = ['up', 'down', 'left', 'right']
            direction = random.choice(possible_moves)
            vacuum.move(direction)

        vacuum.print_output_positions()

    print("\nFinished cleaning")
    print(f"Total Cells Cleaned: {vacuum.clean_count}")
    print(f"Remaining Battery: {vacuum.battery}")

if __name__ == "__main__":
    main()
