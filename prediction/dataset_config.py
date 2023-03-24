import torch
import numpy as np
import torch.utils.data as Data
from torch.utils.data import DataLoader


def data_loading(path, batch_size=64, object_cls=None):
    # Loading and forming data
    file = np.loadtxt(path)
    print(file.shape)
    length = file.shape[0]
    train_size = int(0.8*length)
    validate_size = length - train_size
    X = torch.from_numpy(file[:, :7]).type(torch.FloatTensor)
    Y = file[:, 7] * object_cls.g_clusters + file[:, 8]  # 4-number system transform
    Y = torch.from_numpy(Y).type(torch.LongTensor)
    Y = Y.reshape(Y.shape[0])
    print(X.shape, Y.shape, length)

    Dataset = Data.TensorDataset(X, Y)
    train_set, validate_set = Data.random_split(Dataset, [train_size, validate_size])
    train_dataloader = DataLoader(train_set, batch_size=batch_size)
    test_dataloader = DataLoader(validate_set, batch_size=batch_size)
    return train_set, validate_set, train_dataloader, test_dataloader
