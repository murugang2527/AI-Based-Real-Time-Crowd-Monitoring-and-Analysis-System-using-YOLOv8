from ultralytics import YOLO
import cv2
import winsound  # for alert sound (Windows)

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print(" Camera not opening")
    exit()

# Set crowd limit
CROWD_LIMIT = 2

print(" Crowd Monitoring Started (Press Q to exit)")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # YOLO detection
    results = model(frame)

    boxes = results[0].boxes
    human_count = 0

    # Count humans
    for box in boxes:
        cls_id = int(box.cls[0])
        if cls_id == 0:  # person class
            human_count += 1

    # Draw bounding boxes
    frame = results[0].plot()

    # Display count
    cv2.putText(frame, f"Human Count: {human_count}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    # ALERT CONDITION
    if human_count > CROWD_LIMIT:
        cv2.putText(frame, "CROWD LIMIT EXCEEDED!",
                    (20, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)

        # Beep sound alert
        winsound.Beep(1000, 500)  # frequency, duration

    # Show output
    cv2.imshow("Crowd Monitoring System", frame)

    # Exit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()