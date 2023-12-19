from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import DetectionPredictor


model = YOLO("yolov8n-face.pt")


def stream():
    res = model.predict(source="0", show=True)


def video():
    results = model.predict(source="../../resources/AW2_Dance.mp4", show=True)
    with open("res_yolo_vid.txt", "w") as f:
        f.write(str(results))


# stream()
video()
