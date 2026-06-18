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

# 2. ENCAPSULATION & INHERITANCE
class HandTracker(ComputerVisionApp):  # INHERITANCE: Mana ang cam setup ng parent class
    def __init__(self, confidence=0.7):
        super().__init__()  # Tinatawag ang constructor ng parent para magbukas ang cam

        # ENCAPSULATION: Private variable para sa threshold ng detection
        self.__confidence = confidence

    # Getter and Setter para sa encapsulation
    def get_confidence(self):
        return self.__confidence

    def run_app(self):
        print(f"Running tracker at {self.__confidence * 100}% confidence. Press 'q' to exit.")
        while self.cap.isOpened():
            success, frame = self.cap.read()
            if not success:
                continue

            # Ina-activate ang Polymorphism dito depende kung anong subclass ang gamit
            self.process_frame(frame)

            cv2.imshow('Final Project OOP Demo', frame)

            # Pindutin ang 'q' sa keyboard para mag-close ang camera window
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()