import matplotlib
matplotlib.use("Qt5Agg")  # Or 'TkAgg', 'GTK3Agg', etc.

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Valentine:
    def __init__(self):
        self.seed = 69
        self.message_hash = 0x53454E44204E55444553
        self.fig, self.ax = plt.subplots()
        self.ani = None  # To keep animation alive

    def generate_pattern(self):
        num_dots = 143
        x = np.zeros(num_dots)
        y = np.zeros(num_dots)
        colors = []

        for j in range(num_dots):
            self.seed = (1103515245 * self.seed + 12345) % 2**31
            x[j] = (self.seed / 2**31) * 10
            self.seed = (1103515245 * self.seed + 12345) % 2**31
            y[j] = (self.seed / 2**31) * 10
            colors.append(f"#{random.randint(0, 0xFFFFFF):06x}")

        return x, y, colors

    def display_message(self):
        message = ""
        message_hash = self.message_hash

        for _ in range(10):
            char_code = message_hash & 0xFF
            message = chr(char_code) + message
            message_hash >>= 8

        return message

    def animate(self, i):
        self.ax.clear()
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)

        if i < 100:
            x, y, colors = self.generate_pattern()
            self.ax.scatter(x, y, s=20, c=colors)
        else:
            self.ax.text(5, 5, self.display_message(), fontsize=32, ha='center', va='center')

    def run(self):
        self.ani = animation.FuncAnimation(self.fig, self.animate, frames=200, interval=50)
        plt.show()

if __name__ == "__main__":
    val = Valentine()
    val.run()
