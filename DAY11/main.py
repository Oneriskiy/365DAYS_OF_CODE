from tqdm import tqdm
import time
from typing import Iterable

dict_of_fruits = {
    "Apple": "10kg",
    "Orange": "6kg",
    "Pineapple": "15kg",
}


def tqdm_basic(iterable: Iterable) -> tqdm:
    return tqdm(iterable,
                total=len(iterable),
                desc="dict_of_fruits",
                leave=True,
                unit="items",
                unit_scale=True)


def check_fruits() -> None:
    for item, item_kg in tqdm_basic(dict_of_fruits.items()):
        print(f"\nFruit: {item} | Kg: {item_kg}")
        time.sleep(0.5)


if __name__ == "__main__":
    check_fruits()