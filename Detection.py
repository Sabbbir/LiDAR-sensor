import time
import us

class Detection:
    def __init__(self):
        pass

    def run_detection(self):
        while True:
            result = us.detection()
            print(result)
            time.sleep(0.1)
    # def distance_data(self):
    #     rr = us.data()
    #     print(rr)

# Example usage:
if __name__ == "__main__":
    detector = Detection()
    detector.run_detection()
