import cv2
from abc import ABC, abstractmethod

# 1. ABSTRACTION (Abstract Base Class)
class ComputerVisionApp(ABC):
    def __init__(self):
        # Buksan ang Webcam (0 = default internal camera)
        self.cap = cv2.VideoCapture(0)
        print("Camera Hardware Initialized...")

    @abstractmethod
    def process_frame(self, frame):
        """Abstract method para sa processing ng frame"""
        pass