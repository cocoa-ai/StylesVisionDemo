import VisionLab

final class ViewController: ImageClassificationController<ClassificationService> {
  override func viewDidLoad() {
    super.viewDidLoad()
    mainView.button.setTitle("Choose a picture", for: .normal)
    classificationService.delegate = self
  }
}

// MARK: - ClassificationServiceDelegate

extension ViewController: ClassificationServiceDelegate {
  func classificationService(_ service: ClassificationService, didDetectStyles styles: String) {
    DispatchQueue.main.async { [weak mainView] in
      mainView?.label.text = styles.capitalized
    }
  }
}
