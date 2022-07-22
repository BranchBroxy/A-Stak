import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def mea_layout():

    xy = np.zeros(shape=(64, 2))
    for counter_y, y in enumerate(range(8, 0, -1)):
        for counter_x, x in enumerate(range(8, 0, -1)):
            xy[(x - 1) + 8 * counter_y, 0] = x
            xy[(x - 1) + 8 * counter_y, 1] = y

    return xy

def plot_CM(CM, path):
    G = nx.DiGraph()
    fig = plt.figure(1, figsize=(10, 8), dpi=100)
    G.add_nodes_from(range(64))
    G = nx.restricted_view(G, [0, 7, 56, 63], [])
    #G.add_edge(1, 2)
    # G.add_edges_from(2, 3)
    # CM_ones = np.zeros(shape=(60, 60))
    arr = CM
    row = np.zeros(shape=(1, CM.shape[1]))

    arr = np.insert(arr, 0, [row], axis=0)
    arr = np.insert(arr, 7, [row], axis=0)
    arr = np.insert(arr, 56, [row], axis=0)
    arr = np.insert(arr, 63, [row], axis=0)

    cols = np.zeros(shape=(arr.shape[0]))

    arr = np.insert(arr, 0, [cols], axis=1)
    arr = np.insert(arr, 7, [cols], axis=1)
    arr = np.insert(arr, 56, [cols], axis=1)
    arr = np.insert(arr, 63, [cols], axis=1)
    CM = arr

    CM_neg = np.where(CM < 0, CM, 0)
    CM_pos = np.where(CM > 0, CM, 0)
    CM_pos_masked = np.ma.masked_equal(CM_pos, 0)
    CM_pos_compressed = np.ma.compressed(CM_pos_masked)

    CM_neg_masked = np.ma.masked_equal(CM_neg, 0)
    CM_neg_compressed = np.ma.compressed(CM_neg_masked)

    CM_neg_weights = np.reshape(CM_neg, newshape=(1, -1))
    CM_pos_weights = np.reshape(CM_pos, newshape=(1, -1))
    #CM_neg_weights = np.where(CM_neg_weights == 0, newshape=(1, -1))

    CM_ones = np.where(CM < 0, -1, CM)
    CM_ones = np.where(CM > 0, 1, CM_ones)
    # CM_ones = np.where(CM == 0, CM, 0)
    CM_ones_pos = np.where(CM > 0, 1, 0)

    CM_ones_neg = np.where(CM < 0, 1, 0)

    rows, cols = np.where(CM_ones == 1)

    pos_rows, pos_cols = np.where(CM_ones_pos == 1)
    neg_rows, neg_cols = np.where(CM_ones_neg == 1)

    edges = zip(rows.tolist(), cols.tolist())
    pos_edges = zip(pos_rows.tolist(), pos_cols.tolist())
    neg_edges = zip(neg_rows.tolist(), neg_cols.tolist())

    #G.add_edges_from(list(edges))



    # val_map = {'A': 1.0, 'D': 0.5714285714285714, 'H': 0.0}
    #values = [val_map.get(node, 0.25) for node in G.nodes()]

    # Specify the edges you want here
    green_edges = list(pos_edges)
    red_edges = list(neg_edges)
    #edge_colours = ['black' if not edge in red_edges else 'red' for edge in G.edges()]


    #mapping =
    #G = nx.relabel_nodes(G, mapping)

    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    # mea_layout()
    pos = mea_layout()
    #print(pos)

    d = nx.degree(G)


    nx.draw_networkx_nodes(G, pos, node_size= 850, node_color="grey")
    #plt.show()
                            #node_size = [v * 100 for v in d.values()])
    #nx.draw_networkx_labels(G, pos)

    if CM_pos_compressed.size > CM_neg_compressed.size:
        nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=False, width=CM_neg_compressed, alpha=0.2)
        nx.draw_networkx_edges(G, pos, edgelist=green_edges, edge_color='g', arrows=False, width=CM_pos_compressed, alpha=0.1)
    if CM_neg_compressed.size > CM_pos_compressed.size:
        nx.draw_networkx_edges(G, pos, edgelist=green_edges, edge_color='g', arrows=False, width=CM_pos_compressed, alpha=0.2)
        nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=False, width=CM_neg_compressed, alpha=0.1)





    old_labels = {  56: "", 57: 21, 58: 31, 59: 41, 60: 51, 61: 61, 62: 71, 63: "",
                48: 12, 49: 22, 50: 32, 51: 42, 52: 52, 53: 62, 54: 72, 55: 82,
                40: 13, 41: 23, 42: 33, 43: 43, 44: 53, 45: 63, 46: 73, 47: 83,
                32: 14, 33: 24, 34: 34, 35: 44, 36: 54, 37: 64, 38: 74, 39: 84,
                24: 15, 25: 25, 26: 35, 27: 45, 28: 55, 29: 65, 30: 75, 31: 85,
                16: 16, 17: 26, 18: 36, 19: 46, 20: 56, 21: 66, 22: 76, 23: 86,
                 8: 17,  9: 27, 10: 37, 11: 47, 12: 57, 13: 67, 14: 77, 15: 87,
                 0: "",  1: 28,  2: 38,  3: 48,  4: 58,  5: 68,  6: 78,  7: ""}

    labels = { 0: "",  1: 21, 2: 31,  3: 41,  4: 51,  5: 61,  6: 71,  7: "",
               8: 12,  9: 22, 10: 32, 11: 42, 12: 52, 13: 62, 14: 72, 15: 82,
              16: 13, 17: 23, 18: 33, 19: 43, 20: 53, 21: 63, 22: 73, 23: 83,
              24: 14, 25: 24, 26: 34, 27: 44, 28: 54, 29: 64, 30: 74, 31: 84,
              32: 15, 33: 25, 34: 35, 35: 45, 36: 55, 37: 65, 38: 75, 39: 85,
              40: 16, 41: 26, 42: 36, 43: 46, 44: 56, 45: 66, 46: 76, 47: 86,
              48: 17, 49: 27, 50: 37, 51: 47, 52: 53, 53: 67, 54: 77, 55: 87,
              56: "", 57: 28, 58: 38, 59: 48, 60: 58, 61: 68, 62: 78, 63: ""}
    nx.draw_networkx_labels(G, pos, labels, font_size=18, font_color="whitesmoke")
    #plt.set_size_inches(18.5, 10.5)
    from matplotlib.pyplot import figure

    #figure(figsize=(8, 6), dpi=80)
    plt.savefig(path, edgecolor=None, bbox_inches = "")


    #plt.show()

def plot_CM_test(CM, path):
    G = nx.DiGraph()
    fig = plt.figure(1, figsize=(10, 8), dpi=100)
    G.add_nodes_from(range(64))
    G = nx.restricted_view(G, [0, 7, 56, 63], [])
    #G.add_edge(1, 2)
    # G.add_edges_from(2, 3)
    # CM_ones = np.zeros(shape=(60, 60))
    arr = CM
    row = np.zeros(shape=(1, CM.shape[1]))

    arr = np.insert(arr, 0, [row], axis=0)
    arr = np.insert(arr, 7, [row], axis=0)
    arr = np.insert(arr, 56, [row], axis=0)
    arr = np.insert(arr, 63, [row], axis=0)

    cols = np.zeros(shape=(arr.shape[0]))

    arr = np.insert(arr, 0, [cols], axis=1)
    arr = np.insert(arr, 7, [cols], axis=1)
    arr = np.insert(arr, 56, [cols], axis=1)
    arr = np.insert(arr, 63, [cols], axis=1)
    CM = arr

    CM_pos = np.where(CM < 0, CM, 0)
    CM_neg = np.where(CM > 0, CM, 0)
    # CM_ones = np.where(CM == 0, CM, 0)


    rows, cols = np.where(CM != 0)

    pos_rows, pos_cols = np.where(CM == 1)
    neg_rows, neg_cols = np.where(CM == 1)

    edges = zip(rows.tolist(), cols.tolist())
    pos_edges = zip(pos_rows.tolist(), pos_cols.tolist())
    neg_edges = zip(neg_rows.tolist(), neg_cols.tolist())

    #G.add_edges_from(list(edges))

    green_edges = list(pos_edges)
    red_edges = list(neg_edges)
    #edge_colours = ['black' if not edge in red_edges else 'red' for edge in G.edges()]


    pos = mea_layout()
    nx.draw_networkx_nodes(G, pos, node_size= 850, node_color="grey")


    nx.draw_networkx_edges(G, pos, edgelist=green_edges, edge_color='g', arrows=False)
    edges = nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=False)
    labels = { 0: "",  1: 21, 2: 31,  3: 41,  4: 51,  5: 61,  6: 71,  7: "",
               8: 12,  9: 22, 10: 32, 11: 42, 12: 52, 13: 62, 14: 72, 15: 82,
              16: 13, 17: 23, 18: 33, 19: 43, 20: 53, 21: 63, 22: 73, 23: 83,
              24: 14, 25: 24, 26: 34, 27: 44, 28: 54, 29: 64, 30: 74, 31: 84,
              32: 15, 33: 25, 34: 35, 35: 45, 36: 55, 37: 65, 38: 75, 39: 85,
              40: 16, 41: 26, 42: 36, 43: 46, 44: 56, 45: 66, 46: 76, 47: 86,
              48: 17, 49: 27, 50: 37, 51: 47, 52: 53, 53: 67, 54: 77, 55: 87,
              56: "", 57: 28, 58: 38, 59: 48, 60: 58, 61: 68, 62: 78, 63: ""}
    nx.draw_networkx_labels(G, pos, labels, font_size=18, font_color="whitesmoke")
    # plt.savefig(path, edgecolor=None, bbox_inches = "")
    plt.show()
