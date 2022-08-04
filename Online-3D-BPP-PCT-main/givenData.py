# container_size: A vector of length 3 describing the size of the container in the x, y, z dimension.
# item_size_set:  A list records the size of each item. The size of each item is also described by a vector of length 3.

container_size = [9,9,9]

lower = 3
higher = 3 ## Change to have uniform boxes was 1-5, now 2-2
resolution = 1
item_size_set = []
for i in range(lower, higher + 1):
    for j in range(lower, higher + 1):
        for k in range(lower, higher + 1):
                item_size_set.append((i * resolution, j * resolution , k *  resolution))

# If you want to sample item sizes from a uniform distribution in continuous domain,
# type --sample-from-distribution in your command line.