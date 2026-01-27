from __future__ import annotations

import random

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider

from ..algorithms.metrics import Metrics
from ..algorithms.sorting import bubble_sort


class SortingAnimator:
    def __init__(self, size: int = 30):
        self.size = size
        self.data = [random.randint(1, 100) for _ in range(size)]
        self.metrics = Metrics()
        self.frames = list(bubble_sort(self.data, self.metrics))
        self.index = 0
        self.interval = 200

        self.fig, self.ax = plt.subplots()
        self.bar = self.ax.bar(range(len(self.data)), self.data)
        self.ax.set_title("Bubble Sort Visualizer")

        axcolor = "lightgoldenrodyellow"
        self.ax_slider = plt.axes([0.15, 0.02, 0.65, 0.03], facecolor=axcolor)
        self.slider = Slider(self.ax_slider, "Speed", 50, 1000, valinit=self.interval)
        self.slider.on_changed(self._set_speed)

        self.ax_button = plt.axes([0.82, 0.9, 0.12, 0.06])
        self.button = Button(self.ax_button, "Randomize")
        self.button.on_clicked(self._randomize)

        self.anim = FuncAnimation(self.fig, self._update, interval=self.interval, repeat=False)

    def _set_speed(self, value: float) -> None:
        self.interval = int(value)
        self.anim.event_source.interval = self.interval

    def _randomize(self, _event) -> None:
        self.data = [random.randint(1, 100) for _ in range(self.size)]
        self.metrics = Metrics()
        self.frames = list(bubble_sort(self.data, self.metrics))
        self.index = 0

    def _update(self, _frame) -> None:
        if self.index >= len(self.frames):
            return
        arr = self.frames[self.index]
        for rect, h in zip(self.bar, arr):
            rect.set_height(h)
        self.ax.set_xlabel(f"Comparisons: {self.metrics.comparisons} Swaps: {self.metrics.swaps}")
        self.index += 1

    def show(self) -> None:
        plt.show()
