import matplotlib.pyplot as plt

def plotPlan(path, points, num_iters=1):

    clr=['r','g','b','y','v','i']
    """
    path: List of lists with the different orders in which the nodes are visited
    points: coordinates for the different nodes
    num_iters: number of paths that are in the path list
    
    """
    plt.plot(points[:,0], points[:,1], 'co')
    
    # Set a scale for the arrow heads here should be a reasonable default for this, WTF?)
    a_scale = float(max(points[:,0]))/float(100)

    for i in range(num_iters):
        xi = []; yi = [];
        for j in path[i]:
            xi.append(points[j][0])
            yi.append(points[j][1])
        plt.arrow(xi[-2], yi[-2], (xi[0] - xi[-2]), (yi[0] - yi[-2]),head_width = 3*a_scale, 
        color =clr[i], length_includes_head=True)
        for j in range(0, len(xi) - 2):
            plt.arrow(xi[j], yi[j], (xi[j+1] - xi[j]), (yi[j+1] - yi[j]),head_width = a_scale, 
            color =clr[i], length_includes_head=True)



    #Set axis too slitghtly larger than the set of x and y
    plt.xlim(min(points[:,0])*1.1, max(points[:,0])*1.1)
    plt.ylim(min(points[:,1])*1.1, max(points[:,1])*1.1)
    plt.show()
