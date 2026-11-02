import torch
import torchvision.models as models

# Load your PyTorch model
model = torch.load('your_model.pt', map_location=torch.device('cpu'))
model.eval()

# Dummy input with correct shape
dummy_input = torch.randn(1, 3, 224, 224)  # Adjust to your model input size

# Export
torch.onnx.export(model, dummy_input, "model.onnx", opset_version=11)
