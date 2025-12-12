def distance_3d(coord1, coord2):
    return ((coord1[0] - coord2[0]) ** 2 +
            (coord1[1] - coord2[1]) ** 2 +
            (coord1[2] - coord2[2]) ** 2) ** 0.5

class equivalence_classes:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.classes = len(nodes)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        self.parent[root2] = root1
        if root1 != root2:
            self.classes -= 1

    def count_classes(self):
        return self.classes

    def class_sizes(self):
        sizes = {}
        for node in self.parent:
            root = self.find(node)
            sizes[root] = sizes.get(root, 0) + 1
        return list(sizes.values())

def easy_puzzle(coords, edges_to_add):
    pairs_with_distances = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            dist = distance_3d(coords[i], coords[j])
            pairs_with_distances.append(((coords[i], coords[j]), dist))
    pairs_with_distances.sort(key=lambda x: x[1])
    eq_classes = equivalence_classes(coords)
    for i in range(edges_to_add):
        (coord1, coord2), _ = pairs_with_distances[i]
        eq_classes.union(coord1, coord2)
    sizes = sorted(eq_classes.class_sizes(), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

def hard_puzzle(coords):
    pairs_with_distances = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            dist = distance_3d(coords[i], coords[j])
            pairs_with_distances.append(((coords[i], coords[j]), dist))
    pairs_with_distances.sort(key=lambda x: x[1])
    eq_classes = equivalence_classes(coords)
    for ((coord1, coord2), _) in pairs_with_distances:
        eq_classes.union(coord1, coord2)
        if eq_classes.count_classes() == 1:
            return coord1[0] * coord2[0]

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        coords = []
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(",")
                coords.append(tuple(int(x) for x in parts))
    print(f"Easy puzzle answer: {easy_puzzle(coords, 1000)}")
    print(f"Hard puzzle answer: {hard_puzzle(coords)}")
