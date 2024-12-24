import torch
from torch.utils.data import DataLoader
from model import YOLOModel
from dataset import ComicDataset


# Define training loop
def train_model():
    model = YOLOModel()
    dataset = ComicDataset("data/annotated")
    loader = DataLoader(dataset, batch_size=16, shuffle=True)

    optimizer = torch.optim.Adam(model.parameters())
    for epoch in range(10):
        for images, labels in loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = compute_loss(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch}, Loss: {loss.item()}")


if __name__ == "__main__":
    train_model()
