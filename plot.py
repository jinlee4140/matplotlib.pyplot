import numpy as np
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

plt.plot([1,2,3,4], [1,4,9,16])
plt.show()



plt.plot([1,2,3,4], [1,4,9,16], 'ro')

plt.suptitle('This is a suptitle', fontsize = 14, fontweight='bold')
plt.title('This is a title')
plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.axis([0,6,0,20])
plt.text(3, 19, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
plt.text(2, 16, r'an equation: $y=x^2$', fontsize=15)
plt.annotate('annotate', xy=(2,4), xytext=(1,3), arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()


t = np.arange(0, 5, 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.show()




import matplotlib.pyplot as plt
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1,2,3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4,5,6])


plt.figure(2)                # a second figure
plt.plot([4,5,6])            # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1,2,3')   # subplot 211 title

plt.show()


print np.random.randn(10000)