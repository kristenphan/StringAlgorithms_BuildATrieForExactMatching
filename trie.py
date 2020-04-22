#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    tree[0] = {} # initialize the root node as empty (ie. having no branches yet)
    node_id = 1 # id of the next node to be added to the trie
    for pattern in patterns:
        # when adding a new pattern to the trie, start from the root ie node 0
        curr_node = 0
        for let in pattern:
            # if there are outgoing edges from the current node,
            # check if one of the outgoing edge has same letter as the letter in pattern
            if bool(tree[curr_node]):
                # if yes, there is no need to add this letter to the trie
                # update curr_node and proceed to the next letter
                if let in tree[curr_node]:
                    curr_node = tree[curr_node][let]
                # otherwise, add a new node to the trie,
                # branching from the current node to represent the letter
                else:
                    new_node = node_id
                    node_id += 1
                    tree[curr_node][let] = new_node
                    tree[new_node] = {}
                    curr_node = new_node
            # if there is no outgoing edge from this node,
            # create a new node with a new node id and letter
            # attach the new node underneath the current node
            # update the current node as the new node and proceed to the next letter in the pattern
            else:
                new_node = node_id
                node_id += 1
                tree[curr_node][let] = new_node
                tree[new_node] = {}
                curr_node = new_node

    return tree


# this program reads the input that contains the patterns to be searched for
# and build a trie representing the pattern
# example:
# input:
# 3
# ATAGA
# ATC
# GAT
# output:
# 0->1:A
# 1->2:T
# 2->3:A
# 3->4:G
# 4->5:A
# 2->6:C
# 0->7:G
# 7->8:A
# 8->9:T
# the trie is visualized as below:
#                           (0) root
#                        /      \
#                   A (1)        (7) G
#                      |          |
#                   T (2)        (8) A
#                      |  \       |  <------- edge connecting 2 nodes
#                   A (3) (6) C  (9) T
#                      |
#                   G (4)
#                      |
#  letter ------->  A (5) <------- node id
#  in a pattern
if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
