import numpy as np
import torch
from PIL import Image

from owr.open_world import utils
from owr.open_world import params


class Subset(torch.utils.data.Dataset):
    def __init__(self, dataset, indexes, transform):
        """
        :param dataset: the whole dataset
        :param indexes: indexes to take and put in the subset
        """
        self.dataset = dataset
        self.indexes = indexes
        self.transform = transform

    def __getitem__(self, idx):
        image, labels = self.dataset[self.indexes[idx]]
        return image, labels, idx

    def __len__(self):
        return len(self.indexes)
