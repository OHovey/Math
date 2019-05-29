import math 

from matplotlib import pyplot as plt


# 
# Bazier Curves 
# 

class QuadraticBazierCurve(object):
    def __init__(self, points, t):
        self.P0, self.P1, self.P2 = points 
        self.t = t


    def get_final_points(self):
        pfinal = {
            'x': [],
            'y': []
        } 

        Pa_points = []
        Pb_points = []

        index = 0
        t_values = [i * self.t for i in range(0, round((1 / self.t)) + 1)]
        print('t_values: {}'.format(t_values))
        for i in t_values:
            # print(index)
            pfinal['x'].append( ( (1 - i)**2 ) * self.P0['x'] + (1 - i) * 2 * i * self.P1['x'] + i * i * self.P2['x'] )

            pfinal['y'].append( ( (1 - i)**2 ) * self.P0['y'] + (1 - i) * 2 * i * self.P1['y'] + i * i * self.P2['y'] )
            index += 1 

            Pa_point = {}
            Pa_point['x'] = ( (1 - i) ) * self.P0['x'] + i * self.P1['x'] 
            Pa_point['y'] = ( (1 - i) ) * self.P0['y'] + i * self.P1['y'] 

            Pb_point = {}
            Pb_point['x'] = ( (1 - i) ) * self.P1['x'] + i * self.P2['x']
            Pb_point['y'] = ( (1 - i) ) * self.P1['y'] + i * self.P2['y']

            Pa_points.append(Pa_point)
            Pb_points.append(Pb_point)

        return (pfinal, Pa_points, Pb_points)


def make_bazier_gragh(points, t):
    
    data, Pa_points, Pb_points = QuadraticBazierCurve(points, t).get_final_points() 
    x_data = data['x']
    y_data = data['y']

    # pprint(Pa_points)
    # pprint(Pb_points)

    fig, axs = plt.subplots()
    
    # Plot Bazier Curve and Control points
    Pxs = [d['x'] for d in points]
    Pys = [d['y'] for d in points]
    axs.plot(x_data, y_data, 'o', ls='-')
    axs.plot(Pxs, Pys, 'x', color='red')
    
    # Plot lines between Pa and Pb interval points of equivilent index value 
    for p in range(0, len(Pa_points)):
        axs.plot([Pa_points[p]['x'], Pb_points[p]['x']], [Pa_points[p]['y'], Pb_points[p]['y']], color='green')

    # Set labels
    axs.set_xlabel('x')
    axs.set_ylabel('y')
    axs.grid(True) 

    plt.show()

def animate_bazier_gragh(points, t, curve_type):
    if curve_type == 3:
        return 

    data, Pa_points, Pb_points = QuadraticBazierCurve(points, t).get_final_points()
    x_data = data['x']
    y_data = data['y'] 
    Pxs = [d['x'] for d in points]
    Pys = [d['y'] for d in points]

    fig, axs = plt.subplots()

    for i in range(0, len(x_data) + 1):
        plt.clf()
        plt.plot(x_data[:i], y_data[:i], 'o', ls='-', color = 'red')
        plt.plot(Pxs, Pys, 'x', color="red")
        plt.grid(True)
        for l in  range(0, i):
            plt.plot([Pa_points[l]['x'], Pb_points[l]['x']], [Pa_points[l]['y'], Pb_points[l]['y']], color='green')
        plt.pause(0.05)
        

class CubicBazierCurve(object):
    def __init__(self, points, t):
        self.p0, self.p1, self.p2, self.p3 = points 
        self.t = t


    def get_final_points(self):
        p_final = {
            'x': [],
            'y': []
        }

        t_points = [i * self.t for i in range(0, round(1 / self.t) + 1)]

        for t in t_points:
            p_final['x'].append( (( 1 - t )**3) * self.p0['x'] + 3 * (1 - t)**2 * t * self.p1['x'] + 3 * (1 - t) * t**2 * self.p2['x'] + t**3 * self.p3['x'] )
            p_final['y'].append( (( 1 - t )**3) * self.p0['y'] + 3 * (1 - t)**2 * t * self.p1['y'] + 3 * (1 - t) * t**2 * self.p2['y'] + t**3 * self.p3['y'] )

        return p_final

    
    def plot_bazier_curve(self, animate = False):
        p_final = self.get_final_points() 

        P0_P2_Final, Pa_points, Pb_points = QuadraticBazierCurve((self.p0, self.p1, self.p2), self.t).get_final_points()
        P1_P3_Final, Pb_points, Pc_points = QuadraticBazierCurve((self.p1, self.p2, self.p3), self.t).get_final_points()  

        points = [self.p0, self.p1, self.p2, self.p3]

        Pxs = [i['x'] for i in points]
        Pys = [i['y'] for i in points]

        fig, axs = plt.subplots()

        axs.set_xlabel('x')
        axs.set_ylabel('y')

        plt.grid(True)

        if not animate:

            # plot the Quadratic curves between these points 
            # 
            plt.plot([p for p in P0_P2_Final['x']], [p for p in P0_P2_Final['y']], 'o', color = 'blue', ls = '-')
            plt.plot([p for p in P1_P3_Final['x']], [p for p in P1_P3_Final['y']], 'o', color = 'orange', ls = '-')

            # plot the conection lines between the Quadratic coordinate points
            for p in range(0, len(Pa_points)):
                plt.plot([Pa_points[p]['x'], Pb_points[p]['x']], [Pa_points[p]['y'], Pb_points[p]['y']], ls='-', color="grey")
                plt.plot([Pb_points[p]['x'], Pc_points[p]['x']], [Pb_points[p]['y'], Pc_points[p]['y']], ls='-', color="grey")

            # plot the Bazier Curve and the Coordinate Points
            plt.plot(p_final['x'], p_final['y'], 'o', ls="-", color="red")
            plt.plot(Pxs, Pys, 'x', color="green", ls='-')

            plt.show()
            return 

        for i in range(0, len(p_final['x']) + 1):
            # print(i)
            plt.clf() 

            for o in range(0, i):    
                plt.plot([Pa_points[o]['x'], Pb_points[o]['x']], [Pa_points[o]['y'], Pb_points[o]['y']], ls='-', color='grey')
                plt.plot([Pb_points[o]['x'], Pc_points[o]['x']], [Pb_points[o]['y'], Pc_points[o]['y']], ls='-', color='grey')

            plt.plot(P0_P2_Final['x'][:i], P0_P2_Final['y'][:i], 'o', ls='-', color='blue')
            plt.plot(P1_P3_Final['x'][:i], P1_P3_Final['y'][:i], 'o', ls='-', color='orange')

            plt.plot(Pxs, Pys, 'x', ls='-', color='green')

            plt.plot(p_final['x'][:i], p_final['y'][:i], 'o', ls = '-', color='red')

            plt.pause(0.05)
            
