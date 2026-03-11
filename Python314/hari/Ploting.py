import matplotlib.pyplot as plt
def simple_line_plot():
    x=[1,2,3,4,5]
    y=[2,4,6,8,10]
    plt.plot(x,y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axiz')
    plt.title('Simple Line Plot')
    plt.show()

if __name__=='__main__':
    simple_line_plot()
