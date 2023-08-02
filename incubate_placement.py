#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.position = (x, y, z)
        self.direction = direction

    def move(self, distance):
        x, y, z = self.position
        if self.direction == 'N':
            self.position = (x, y + distance, z)
        elif self.direction == 'S':
            self.position = (x, y - distance, z)
        elif self.direction == 'E':
            self.position = (x + distance, y, z)
        elif self.direction == 'W':
            self.position = (x - distance, y, z)
        elif self.direction == 'Up':
            self.position = (x, y, z + distance)
        elif self.direction == 'Down':
            self.position = (x, y, z - distance)

    def turn(self, direction):
        directions = ['N', 'E', 'S', 'W', 'Up', 'Down']
        current_index = directions.index(self.direction)
        if direction == 'l':
            new_index = (current_index - 1) % len(directions)
        elif direction == 'r':
            new_index = (current_index + 1) % len(directions)
        self.direction = directions[new_index]

    def turn_up_down(self, direction):
        if direction == 'u':
            self.direction = 'Up'
        elif direction == 'd':
            self.direction = 'Down'

    def execute_commands(self, commands):
        for command in commands:
            if command in ['f', 'b']:
                distance = 1 if command == 'f' else -1
                self.move(distance)
            elif command in ['l', 'r']:
                self.turn(command)
            elif command in ['u', 'd']:
                self.turn_up_down(command)


# Test the spacecraft movement
if __name__ == "__main__":
    chandrayaan_3 = Spacecraft(0, 0, 0, 'N')
    commands = ["f", "r", "u", "b", "l"]
    chandrayaan_3.execute_commands(commands)
    print("Final Position:", chandrayaan_3.position)
    print("Final Direction:", chandrayaan_3.direction)


# In[7]:


def run_tests():
    # Test case 
    chandrayaan_3 = Spacecraft(0, 0, 0, 'N')
    commands = ["f", "r", "u", "b", "l"]
    chandrayaan_3.execute_commands(commands)
    assert chandrayaan_3.position == (0, 1, -1)
    assert chandrayaan_3.direction == 'W'
    print("Test case 1 passed.")



if __name__ == "__main__":
    run_tests()


# In[ ]:




