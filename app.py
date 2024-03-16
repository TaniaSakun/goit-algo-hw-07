from controllers.avl_controller import Avl
from numpy import random


def avl_task():
    keys = list(set(random.randint(100, size=16)))
    tree = Avl()
    tree.insert_many(keys)
    print("AVL Tree after insertions:")
    print(tree)

    # Delete
    keys_to_delete = random.choice(keys, size=5)
    tree.delete_many(keys_to_delete)
    print("AVL Tree after deletions:")
    print(tree)

    print(f"Keys that were added to the AVL tree:  {sorted(keys)}")
    print(f"Keys that were deleted from the AVL tree: {keys_to_delete}")
    expected_keys = list(set(keys) - set(keys_to_delete))
    print(f"Keys that are in the AVL tree:            {sorted(expected_keys)}")
    print(f"Min key in the AVL tree:                  {tree.min_key()}")
    print(f"Max key in the AVL tree:                  {tree.max_key()}")
    print(f"Expected sum of keys:                     {sum(expected_keys)}")
    print(f"Sum of keys in the AVL tree:              {tree.total_sum()}")
