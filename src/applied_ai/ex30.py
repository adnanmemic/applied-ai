import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

# Image Classification with Fashion-MNIST
# Based on the official PyTorch Quickstart Tutorial:
# https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html

# Load the dataset
train_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)

batch_size = 64

train_dataloader = DataLoader(
    train_data,
    batch_size=batch_size,
    shuffle=True
)

test_dataloader = DataLoader(
    test_data,
    batch_size=batch_size
)

# Define the neural network
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.flatten = nn.Flatten()

        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28 * 28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


# Select device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

model = NeuralNetwork().to(device)

# Loss function and optimizer
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=1e-3
)

# Training function
def train(dataloader, model, loss_fn, optimizer):
    model.train()
    size = len(dataloader.dataset)

    for batch, (X, y) in enumerate(dataloader):
        X = X.to(device)
        y = y.to(device)

        # Forward pass
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            current = batch * len(X)
            print(
                f"Loss: {loss.item():.4f} "
                f"[{current}/{size}]"
            )


# Evaluation function
def test(dataloader, model, loss_fn):
    model.eval()

    size = len(dataloader.dataset)
    num_batches = len(dataloader)

    test_loss = 0
    correct = 0

    with torch.no_grad():
        for X, y in dataloader:
            X = X.to(device)
            y = y.to(device)

            pred = model(X)

            test_loss += loss_fn(pred, y).item()
            correct += (
                pred.argmax(1) == y
            ).type(torch.float).sum().item()

    test_loss /= num_batches
    accuracy = correct / size

    print(
        f"Test Accuracy: {accuracy * 100:.2f}% | "
        f"Average Loss: {test_loss:.4f}"
    )


# Train and evaluate
epochs = 5

for epoch in range(epochs):
    print(f"\nEpoch {epoch + 1}/{epochs}")
    print("-------------------------------")

    train(train_dataloader, model, loss_fn, optimizer)
    test(test_dataloader, model, loss_fn)

print("\nTraining finished!")


# Make a prediction
classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot"
]

model.eval()

with torch.no_grad():
    X, y = test_data[0]
    X = X.to(device)

    pred = model(X.unsqueeze(0))
    predicted_class = pred.argmax(1).item()

    print(f"Predicted: {classes[predicted_class]}")
    print(f"Actual: {classes[y]}")
