import math


class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.edges = []
        self.x = x
        self.y = y
        self.g_distance = 0

    def add_child(self, node, distance):
        for edge in self.edges:
            if edge.node == node:
                return -1
        self.edges.append(Edge(node, distance))


class Edge(boject):
    def __init__(self, node, distance):
        self.node = node    # why not nodes
        self.distance = distance
