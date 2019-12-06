from collections import namedtuple
from typing import Dict, List, Callable

Node = namedtuple('Node', 'name parent children data')


def make_tree_from_adj_list(adj_list):
    root = 'COM'
    nodes: Dict['str', Node] = {root: Node(root, None, [], {})}

    for parent, child in adj_list:
        node = Node(child, parent, [], {})
        nodes[child] = node

    # N.B. I modify node_lookup under iteration, so I cast to list and slice, to get a fixed iterator
    for node in list(nodes.values())[:]:
        if not (node.parent in nodes.keys()) and node.name != root:
            parent_node = Node(node.parent, root, [], {})
            nodes[node.parent] = parent_node

    for node in nodes.values():
        if node.name != root:
            nodes[node.parent].children.append(node)

    return nodes[root]


def compute_descendants(tree_root, f_descendants='n_descendants'):
    topo_sorted_nodes = all_descendants_BFS(tree_root)
    reverse_topo_sort = reversed(topo_sorted_nodes)
    for n in reverse_topo_sort:
        if len(n.children) == 0:
            n.data[f_descendants] = 0
        else:
            n.data[f_descendants] = len(n.children) + sum(nn.data[f_descendants] for nn in n.children)


def all_descendants_BFS(tree_root: Node) -> List[Node]:
    """All descendents of a node, in Breadth First Search order"""
    topo_sorted_nodes = [tree_root]
    for n in topo_sorted_nodes:
        topo_sorted_nodes += n.children

    return topo_sorted_nodes


def find_DFS(predicate: Callable[[Node], bool], node: Node) -> List[Node]:
    """Returns the path in the tree from the root node to the first element that fulfils the predicate"""
    def find_DFS_(predicate,node) -> List[Node]:
        if predicate(node):
            return [node]
        elif len(node.children) == 0:
            return []
        else:
            for c in node.children:
                dfs1 = find_DFS_(predicate,c)
                if len(dfs1) > 0:
                    return [node] + dfs1
        return []

    path_found = find_DFS_(predicate,node)
    if len(path_found) > 0:
        return path_found
    else:
        raise ValueError("There is no element in the tree that fulfils the predicate.")


def calculate_hops(root: Node) -> int:
    nodes = all_descendants_BFS(root)
    bottom_up = reversed(nodes)
    for node in bottom_up:
        try:
            p1 = find_DFS(lambda n: n.name == 'YOU', node)
            p2 = find_DFS(lambda n: n.name == 'SAN', node)
            hops_to_santa = len(p1) + len(p2) - 4 #remove both endpoints of both paths
            return hops_to_santa
        except ValueError:
            pass
    raise ValueError("There is no common object that one can orbit hop through to get to Santa!")