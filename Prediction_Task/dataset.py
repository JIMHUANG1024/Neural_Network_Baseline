from torch.utils.data import Dataset


class my_dataset(Dataset):
    def __init__(self) -> None:
        super().__init__()
        pass

    def __getitem__(self, index):
        return 
    
    def __len__(self):
        return