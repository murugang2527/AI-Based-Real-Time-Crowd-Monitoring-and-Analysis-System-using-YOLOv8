from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ Camera not opening")
    exit()

print("✅ Human Counting Started (Press Q to exit)")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # YOLO prediction
    results = model(frame)

    # Get detection boxes
    boxes = results[0].boxes

    human_count = 0

    # Loop through detections
    for box in boxes:
        cls_id = int(box.cls[0])  # class id

        # COCO class 0 = person
        if cls_id == 0:
            human_count += 1

    # Draw results
    annotated_frame = results[0].plot()

    # Show human count on screen
    cv2.putText(
        annotated_frame,
        f"Human Count: {human_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Display
    cv2.imshow("YOLO Human Counting", annotated_frame)

    # Exit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()