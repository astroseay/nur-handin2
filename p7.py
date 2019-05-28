# problem 7
# points: 10

import sys

import numpy as np
# import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import patches
import h5py


class PointProperties():
    """define mass and x-y coordinates for a point."""

    def __init__(self,x,y,mass):
        self.x = x
        self.y = y
        self.mass = mass

class Node():
    """stores points until leaf_limit is reached, then subdivides.

    Node stores information about the points in order to know when to 
    subdivide. because it's in 2d space, it knows x-y, width, and height.

    """

    def __init__(self,x0,y0,w,h,points,moment=0,parent=None):
        self.x0 = x0
        self.y0 = y0
        self.width = w
        self.height = h
        self.points = points
        self.moment = moment
        self.children = []
        self.is_leaf = False
        self.parent = parent
    
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_points(self):
        return self.points

class QuadTree():
    """defines the quadtree. if i come back to this i'll make the documentation better."""

    def __init__(self,xlim,ylim,leaf_limit,width,height):
        self.xlim = xlim
        self.ylim = ylim
        self.leaf_limit = leaf_limit
        self.width = width
        self.height = height
        self.points = []
        self.root = Node(xlim,ylim,width,height,self.points)
    
    def add_point(self,x,y,m):
        self.points.append(PointProperties(x,y,m))

    def get_points(self):
        return self.points

    def subdivide(self):
        self.root = tree_subdivide(self.root,self.leaf_limit)

    # essentially follows the slides to define trees with nodes
    # that have a leaf limit of 12
    def graph(self,f='./plots/quadtree.png',save=False):
        fig, ax = plt.subplots(1,figsize=(7,5))
        plt.xlim(self.xlim,self.xlim + self.width)
        plt.ylim(self.ylim,self.ylim + self.height)
        children = find_children(self.root)
        x = [point.x for point in self.points]
        y = [point.y for point in self.points]
        ax.plot(x, y,marker='.',c='cyan',ls='None',alpha=0.3)
        for child in children:
            ax.add_patch(patches.Rectangle((child.x0,child.y0),child.width,
                child.height,fill=False))
        plt.xlabel('x pos ',fontsize = 20)
        plt.ylabel('y pos ',fontsize = 20)
        # plt.show()
        if save:
            plt.savefig(f)


def tree_subdivide(node,point_limit):
    """divide trees from nodes based off of point_limit."""

    if len(node.points) == 0:
        # print('zero')
        node.is_leaf = True
        return

    elif int(len(node.points)) <= point_limit:
        node.is_leaf = True
        # print('below lim')
        return

    elif len(node.points) > point_limit:\
        #  scale reduction
        w_reduced = node.width*0.5
        h_reduced = node.height*0.5

        # points in each quadrant
        # denoted as sw,nw,se,ne
        points_in_sw = check_points(node.x0,node.y0,w_reduced,h_reduced,
                node.points)

        points_in_nw = check_points(node.x0,node.y0 + h_reduced,w_reduced,
                h_reduced,node.points)

        points_in_se = check_points(node.x0 + w_reduced,node.y0,w_reduced,
                h_reduced, node.points)

        points_in_ne = check_points(node.x0 + w_reduced,node.y0 + h_reduced,
                w_reduced,h_reduced,node.points)

        sw = Node(node.x0,node.y0,w_reduced,h_reduced,
                points_in_sw,parent=node)

        nw = Node(node.x0,node.y0 + h_reduced,w_reduced,h_reduced,
                points_in_nw,parent=node)

        se = Node(node.x0 + w_reduced,node.y0,w_reduced,h_reduced,
                points_in_se,parent=node)

        ne = Node(node.x0 + w_reduced,node.y0 + h_reduced,w_reduced,h_reduced,
                points_in_ne,parent=node)

        node.children = [sw,nw,se,ne]

        for child in node.children:
            tree_subdivide(child,point_limit)

    return node


def check_points(x_node,y_node,width,height,points):
    true_points = []
    for i,point in enumerate(points):
        if x_node < point.x <= x_node + width and \
                y_node < point.y <= y_node + height:
                    
            true_points.append(point)

    return true_points


def find_children(node):
    children = []

    if node.is_leaf:
        children = [node]
    else:
        for child in node.children:
            children += (find_children(child))

    return children


def calculate_multipole(node):
    # doesn't work lol not used
    children = find_children(node)

    for child in children:
        # child.moment = 0
        for i in range(len(child.points)):
            child.moment += child.points[i].mass

def main():
    # read in data
    # coords, masses, particle ids, velocities
    particles = h5py.File('colliding.hdf5', 'r')['PartType4']
    coords = particles['Coordinates']
    masses = particles['Masses'][()]
    pids = particles['ParticleIDs'][()]
    vels = particles['Velocities'][()]

    xlim = 0
    ylim = 0
    width = 150
    height = 150
    leaf_limit = 12

    particle_qtree = QuadTree(xlim,ylim,leaf_limit,width,height)

    for i in range(len(coords[:,0])):
        particle_qtree.add_point(coords[i,0], coords[i, 1], masses[i])

    particle_qtree.subdivide()
    particle_qtree.graph(save=True)

if __name__ == '__main__':
    sys.exit(main())
