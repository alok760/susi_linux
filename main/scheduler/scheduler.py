from abc import ABC, abstractclassmethod
from threading import Thread

from rx.subjects import Subject


class Schedule(ABC, Thread):
    def __init__(self):
        super().__init__()
        self.subject = Subject()


    @abstractclassmethod
    def run(self):
        pass

    def on_detected(self):
        self.subject.on_next("Event")
