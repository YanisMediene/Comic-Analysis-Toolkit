import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QPushButton,
    QFileDialog,
    QLabel,
    QVBoxLayout,
)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from detection.panel_detector import PanelDetector


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Comic Analysis Toolkit")
        self.setGeometry(100, 100, 800, 600)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Boutons
        self.load_button = QPushButton("Charger une image")
        self.load_button.clicked.connect(self.load_image)
        layout.addWidget(self.load_button)

        # Zone d'affichage
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        # Détecteur
        self.detector = PanelDetector()

    def load_image(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Sélectionner une image", "", "Images (*.png *.jpg *.jpeg)"
        )
        if filename:
            # TODO: Implémenter le traitement de l'image
            pixmap = QPixmap(filename)
            self.image_label.setPixmap(
                pixmap.scaled(
                    self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
