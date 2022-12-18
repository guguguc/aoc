#/usr/bin/python3
from collections import defaultdict

def preprocess(filename):
    """
    line: light yellow bags contain 3 wavy turquoise bags.
    """
    fp = open(filename)
    tree = defaultdict(list)
    for line in fp.readlines():
        segments = line.rstrip(".\n").split(" contain ")
        root = segments[0][:-4].strip()
        nodes = [seg[:-4].strip() for seg in segments[1].split(",")]
        nodes = [dict(name=node[2:], size=node[0]) for node in nodes]
        for node in nodes:
            tree[node['name']].append((root, node['size']))
    tree.pop(" other")
    return tree

def dfs1(node, tree, st):
    roots = tree.get(node)
    if roots is None: return
    for nd, _ in roots:
        st.add(nd)
        dfs1(nd, tree, st)

def dfs2(root, tree):
    if tree.get(root) is None: return 1
    ans = 0
    for node, size in tree[root]:
        ans += dfs2(node, tree) * size
    return ans + 1

def convert(tree: dict):
    ntree = defaultdict(list)
    for node_name, roots in tree.items():
        for name, size in roots:
            ntree[name].append((node_name, int(size)))
    return ntree

def part1(tree: dict, target) -> int:
    st = set()
    dfs1(target, tree, st)
    return len(st)


def part2(tree: dict, target) -> int:
    ntree = convert(tree)
    ans = dfs2(target, ntree) - 1
    return ans

if __name__ == "__main__":
    filename = "input.txt"
    data = preprocess(filename)
    target = "shiny gold"
    ans1 = part1(data, target)
    ans2 = part2(data, target)
    print(f"ans 1 is {ans1}")
    print(f"ans 2 is {ans2}")
