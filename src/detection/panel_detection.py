import cv2
import torch


def detect_panels(image_path, model_path):
    # Load the model
    model = torch.load(model_path)
    model.eval()

    # Load and preprocess the image
    image = cv2.imread(image_path)
    # (Additional preprocessing here)

    # Perform detection
    detections = model(image)
    return detections


if __name__ == "__main__":
    results = detect_panels("data/raw/example_comic.jpg", "data/models/yolo_model.pth")
    print(results)
