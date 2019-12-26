from day06.day6_lib import make_tree_from_adj_list, compute_descendants, all_descendants_BFS, calculate_hops

if __name__ == "__main__":
    with open('../inputs/day6.txt') as f:
        input_ = f.read()
    orbits_ = [p.split(")") for p in input_.splitlines()]
    com_object = make_tree_from_adj_list(orbits_)
    desc = 'desc'
    compute_descendants(com_object,'desc')
    print(f"Ans A:{sum(nn.data[desc] for nn in all_descendants_BFS(com_object))}") # 160040

    hops_to_santa = calculate_hops(com_object)
    print(f"ans B: You need {hops_to_santa} orbital hops to get to share orbital center with santa") #  373
