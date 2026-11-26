import pickle
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "data" / "cifar-10-batches-py"


def _load_batch(name):
    with open(DIR / name, "rb") as f:
        batch = pickle.load(f, encoding="bytes")
    X = np.asarray(batch[b"data"], dtype=np.uint8)  # (N, 3072)
    y = np.asarray(batch[b"labels"], dtype=np.int64)
    return X, y


def load_cifar10():
    """Return Xtr, ytr, Xte, yte with flat 3072-length rows."""
    parts = [_load_batch(f"data_batch_{i}") for i in range(1, 6)]
    Xtr = np.concatenate([p[0] for p in parts])
    ytr = np.concatenate([p[1] for p in parts])
    Xte, yte = _load_batch("test_batch")
    return Xtr, ytr, Xte, yte
