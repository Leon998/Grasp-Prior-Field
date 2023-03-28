import torch
import numpy as np
import torch.utils.data as Data
from torch.utils.data import DataLoader
import os


def data_loading(path, batch_size=64):
    # Loading and forming data
    file = np.loadtxt(path)
    print(file.shape)
    length = file.shape[0]
    train_size = int(0.8*length)
    validate_size = length - train_size
    X = torch.from_numpy(file[:, :7]).type(torch.FloatTensor)
    Y = file[:, 7]
    Y = torch.from_numpy(Y).type(torch.LongTensor)
    Y = Y.reshape(Y.shape[0])
    print(X.shape, Y.shape, length)

    Dataset = Data.TensorDataset(X, Y)
    train_set, validate_set = Data.random_split(Dataset, [train_size, validate_size])
    train_dataloader = DataLoader(train_set, batch_size=batch_size)
    test_dataloader = DataLoader(validate_set, batch_size=batch_size)
    return train_set, validate_set, train_dataloader, test_dataloader


def data_extract_diverse(path, batch_size=64):
    # path = '../obj_coordinate/mug/'
    files = os.listdir(path)
    files.sort()
    X = np.zeros((1, 7))
    G = np.zeros((1, 7))
    Y = []
    for i, file in enumerate(files):
        TF_oh = np.loadtxt(path + file)
        x = TF_oh[:-1]
        gpose = TF_oh[-1].reshape(1, 7)
        length = len(x)
        g = g_stack(gpose, length)
        for j in range(length):
            Y.append(i)
        X = np.concatenate((X, x), axis=0)
        G = np.concatenate((G, g), axis=0)
    X = torch.from_numpy(X[1:]).type(torch.FloatTensor)
    G = torch.from_numpy(G[1:]).type(torch.FloatTensor)
    Y = np.array(Y).reshape(len(Y), -1)
    Y = torch.from_numpy(Y).type(torch.LongTensor).reshape(Y.shape[0])
    length = X.shape[0]
    train_size = int(0.8 * length)
    validate_size = length - train_size
    print(X.shape, Y.shape, length)

    Dataset = Data.TensorDataset(X, Y)
    train_set, validate_set = Data.random_split(Dataset, [train_size, validate_size])
    train_dataloader = DataLoader(train_set, batch_size=batch_size)
    test_dataloader = DataLoader(validate_set, batch_size=batch_size)
    return train_set, validate_set, train_dataloader, test_dataloader


def g_stack(gpose, length):
    g = np.zeros((1, 7))
    for i in range(length):
        g = np.concatenate((g, gpose), axis=0)
    g = g[1:, :]
    return g


if __name__ == "__main__":
    path = '../obj_coordinate/mug/'
    files = os.listdir(path)
    files.sort()
    X = np.zeros((1, 7))
    G = np.zeros((1, 7))
    Y = []
    for i, file in enumerate(files):
        TF_oh = np.loadtxt(path + file)
        x = TF_oh[:-1]
        gpose = TF_oh[-1].reshape(1, 7)
        length = len(x)
        g = g_stack(gpose, length)
        for j in range(length):
            Y.append(i)
        # print(x.shape, g.shape)
        X = np.concatenate((X, x), axis=0)
        G = np.concatenate((G, g), axis=0)
    X = X[1:]
    G = G[1:]
    Y = np.array(Y).reshape(len(Y), -1)
    print(X.shape, Y.shape)