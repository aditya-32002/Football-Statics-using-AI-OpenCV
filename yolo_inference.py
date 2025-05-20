from ultralytics import YOLO

model = YOLO('Models/best.pt')

result = model.predict('video/test.mp4', save=True)

print(result[0])

for box in result[0].boxes:
    print(box) 