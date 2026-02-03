from __future__ import annotations

"""RO: Animatie interactiva pentru bubble sort.
EN: Interactive animation for bubble sort.
"""

import random

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider

from ..algorithms.metrics import Metrics
from ..algorithms.sorting import bubble_sort


class SortingAnimator:
    """RO: UI Matplotlib cu slider de viteza si buton randomize.
    EN: Matplotlib UI with speed slider and randomize button.
    """
    def __init__(self, size: int = 30):
        """RO: Pregateste datele, animatia si controalele.
        EN: Prepare data, animation, and controls.
        """
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
        """RO: Ajusteaza intervalul de animatie.
        EN: Adjust animation interval.
        """
        self.interval = int(value)
        self.anim.event_source.interval = self.interval

    def _randomize(self, _event) -> None:
        """RO: Reface datele si metricle pentru o noua rulare.
        EN: Rebuild data and metrics for a new run.
        """
        self.data = [random.randint(1, 100) for _ in range(self.size)]
        self.metrics = Metrics()
        self.frames = list(bubble_sort(self.data, self.metrics))
        self.index = 0

    def _update(self, _frame) -> None:
        """RO: Deseneaza frame-ul curent si actualizeaza metricle.
        EN: Draw current frame and update metrics.
        """
        if self.index >= len(self.frames):
            return
        arr = self.frames[self.index]
        for rect, h in zip(self.bar, arr):
            rect.set_height(h)
        self.ax.set_xlabel(f"Comparisons: {self.metrics.comparisons} Swaps: {self.metrics.swaps}")
        self.index += 1

    def show(self) -> None:
        """RO: Afiseaza fereastra Matplotlib.
        EN: Show the Matplotlib window.
        """
        plt.show()
