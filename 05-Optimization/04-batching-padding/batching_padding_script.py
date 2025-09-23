import torch
from torch.utils.data import DataLoader, Dataset

class DummyDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

def collate_fn(batch):
    """
    Custom collate function to handle variable-length sequences.

    Args:
        batch: A list of data samples.

    Returns:
        Padded batch of data.
    """
    max_length = max(len(sample) for sample in batch)
    padded_batch = [
        sample + [0] * (max_length - len(sample)) for sample in batch
    ]
    return torch.tensor(padded_batch)

if __name__ == "__main__":
    # Example usage
    data = [[1, 2, 3], [4, 5], [6]]  # Variable-length sequences
    dataset = DummyDataset(data)
    dataloader = DataLoader(dataset, batch_size=2, collate_fn=collate_fn)

    for batch in dataloader:
        print("Padded Batch:", batch)