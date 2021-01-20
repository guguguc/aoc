#/usr/bin/python3

def preprocess(filename):
    """
    line: light yellow bags contain 3 wavy turquoise bags.
    """
    fp = open(filename)
    tree = {}
    for line in fp.readlines():
        segments = line.rstrip(".\n").split(" contain ")
        root = segments[0][:-4].strip()
        nodes = [seg[:-4].strip() for seg in segments[1].split(",")]
        nodes = [dict(name=node[2:], num=node[0]) for node in nodes]
        for node in nodes:
            if tree.get(node['name']) is None:
                tree[node['name']] = {'root': [root], 'size': [node['num']]}
            else:
                tree[node['name']]['root'].append(root)
                tree[node['name']]['size'].append(node['num'])
    tree.pop(" other")
    return tree

def dfs1(node, tree, st):
    roots = tree.get(node)
    if roots is None: return
    for node in roots['root']:
        st.add(node)
        dfs1(node, tree, st)

def dfs2(node, tree):
    if tree.get(node) is None: return 1
    ans = 0
    childs_node = tree[node]['child']
    childs_size = tree[node]['size']
    for node, size in zip(childs_node, childs_size):
        ans += dfs2(node, tree) * size
    return ans + 1

def part1(tree: dict) -> int:
    st = set()
    target = "shiny gold"
    dfs1(target, tree, st)
    return len(st)

def convert(tree: dict):
    ntree = {}
    for node, roots in tree.items():
        roots_name = roots['root']
        roots_size = roots['size']
        for name, size in zip(roots_name, roots_size):
            child = ntree.get(name)
            size = int(size)
            if child is None:
                ntree[name] = {'child': [node], 'size': [size]}
            else:
                ntree[name]['child'].append(node)
                ntree[name]['size'].append(size)
    return ntree

def part2(tree: dict) -> int:
    ntree = convert(tree)
    target = "shiny gold"
    ans = dfs2(target, ntree) - 1
    return ans

if __name__ == "__main__":
    filename = "input.txt"
    data = preprocess(filename)
    ans1 = part1(data)
    ans2 = part2(data)
    print(ans2)
