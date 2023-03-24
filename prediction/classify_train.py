import torch
import torch.utils.data as Data
from torch import nn
from torch.utils.data import DataLoader
import numpy as np
from dataset_config import *
from object_config import objects

object_cls = objects['cracker_box']
output_dim = object_cls.g_clusters * len(object_cls.grasp_types)

MLP = torch.nn.Sequential(
    torch.nn.Linear(7, 32),
    torch.nn.ReLU(),
    torch.nn.Linear(32, 64),
    torch.nn.ReLU(),
    torch.nn.Linear(64, output_dim)
)


def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # Compute prediction error
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def t_test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100 * correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")


if __name__ == "__main__":
    torch.manual_seed(1)  # reproducible

    path = 'classify/training_data/' + object_cls.name + '_field.txt'
    batch_size = 64
    epochs = 50
    # Get cpu or gpu device for training.
    device = "cuda"
    print(f"Using {device} device")

    _, _, train_dataloader, test_dataloader = data_loading(path, batch_size, object_cls)

    for X, y in train_dataloader:
        print(f"Shape of X [N, C, H, W]: {X.shape}")
        print(f"Shape of y: {y.shape} {y.dtype}")
        break

    model = MLP.to(device)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.03)

    for t in range(epochs):
        print(f"Epoch {t + 1}\n-------------------------------")
        train(train_dataloader, model, loss_fn, optimizer)
        t_test(test_dataloader, model, loss_fn)
    print("Done!")
    # Save model
    # torch.save(model.state_dict(), "model.pth")
    torch.save(model, 'classify/trained_models/' + object_cls.name + '.pkl')
