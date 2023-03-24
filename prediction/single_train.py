import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np


device = "cuda"
file = np.loadtxt('../obj_coordinate/pcd_field/mustard_bottle/field_position.txt')
print(file.shape)
X = torch.from_numpy(file[:, :3]).type(torch.FloatTensor)
Y = file[:, 3:4] * 4 + file[:, 4:5]  # quaternary system transform
Y = torch.from_numpy(Y).type(torch.LongTensor)
Y = Y.reshape(Y.shape[0])
print(Y.shape)

net = torch.nn.Sequential(
    torch.nn.Linear(3, 10),
    torch.nn.ReLU(),
    torch.nn.Linear(10, 32),
    torch.nn.ReLU(),
    torch.nn.Linear(32, 12)
)  # define the network
print(net)  # net architecture
net = net.to(device)

optimizer = torch.optim.SGD(net.parameters(), lr=0.03)
loss_func = torch.nn.CrossEntropyLoss()  # the target label is NOT an one-hotted

for t in range(8000):
    X, Y = X.to(device), Y.to(device)
    out = net(X)  # input x and predict based on x
    loss = loss_func(out, Y)  # must be (1. nn output, 2. target), the target label is NOT one-hotted

    optimizer.zero_grad()  # clear gradients for next train
    loss.backward()  # backpropagation, compute gradients
    optimizer.step()  # apply gradients

    if t % 50 == 0:
        loss, current = loss.item(), (t + 1) * len(X)
        print(f"loss: {loss:>7f}")
        prediction = torch.max(out, 1)[1]
        pred_Y = prediction.data.cpu().numpy()
        target_Y = Y.data.cpu().numpy()
        accuracy = float((pred_Y == target_Y).astype(int).sum()) / float(target_Y.size)
        print(f"accuracy: {accuracy:>7f}")
