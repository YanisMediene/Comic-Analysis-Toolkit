import torch
import torch.nn as nn
import torchvision.transforms as transforms


class PanelDetector(nn.Module):
    def __init__(self):
        super(PanelDetector, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.classifier = nn.Sequential(
            nn.Linear(128 * 56 * 56, 1024),
            nn.ReLU(True),
            nn.Linear(1024, 4),  # [x, y, width, height]
        )

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

    def detect(self, image):
        """Détecte les cases dans une image"""
        transform = transforms.Compose(
            [
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
            ]
        )
        # TODO: Implémenter la détection
        return []
