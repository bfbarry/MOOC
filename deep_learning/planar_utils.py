bplist00�XUTI-Data�_$com.apple.traditional-mac-plain-text_public.utf8-plain-text_public.utf16-plain-textO�import matplotlib.pyplot as pltimport numpy as npimport sklearnimport sklearn.datasetsimport sklearn.linear_modeldef plot_decision_boundary(model, X, y):    # Set min and max values and give it some padding    x_min, x_max = X[0, :].min() - 1, X[0, :].max() + 1    y_min, y_max = X[1, :].min() - 1, X[1, :].max() + 1    h = 0.01    # Generate a grid of points with distance h between them    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))    # Predict the function value for the whole grid    Z = model(np.c_[xx.ravel(), yy.ravel()])    Z = Z.reshape(xx.shape)    # Plot the contour and training examples    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)    plt.ylabel('x2')    plt.xlabel('x1')    plt.scatter(X[0, :], X[1, :], c=y, cmap=plt.cm.Spectral)    def sigmoid(x):    """    Compute the sigmoid of x    Arguments:    x -- A scalar or numpy array of any size.    Return:    s -- sigmoid(x)    """    s = 1/(1+np.exp(-x))    return sdef load_planar_dataset():    np.random.seed(1)    m = 400 # number of examples    N = int(m/2) # number of points per class    D = 2 # dimensionality    X = np.zeros((m,D)) # data matrix where each row is a single example    Y = np.zeros((m,1), dtype='uint8') # labels vector (0 for red, 1 for blue)    a = 4 # maximum ray of the flower    for j in range(2):        ix = range(N*j,N*(j+1))        t = np.linspace(j*3.12,(j+1)*3.12,N) + np.random.randn(N)*0.2 # theta        r = a*np.sin(4*t) + np.random.randn(N)*0.2 # radius        X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]        Y[ix] = j            X = X.T    Y = Y.T    return X, Ydef load_extra_datasets():      N = 200    noisy_circles = sklearn.datasets.make_circles(n_samples=N, factor=.5, noise=.3)    noisy_moons = sklearn.datasets.make_moons(n_samples=N, noise=.2)    blobs = sklearn.datasets.make_blobs(n_samples=N, random_state=5, n_features=2, centers=6)    gaussian_quantiles = sklearn.datasets.make_gaussian_quantiles(mean=None, cov=0.5, n_samples=N, n_features=2, n_classes=2, shuffle=True, random_state=None)    no_structure = np.random.rand(N, 2), np.random.rand(N, 2)        return noisy_circles, noisy_moons, blobs, gaussian_quantiles, no_structure_�import matplotlib.pyplot as plt
import numpy as np
import sklearn
import sklearn.datasets
import sklearn.linear_model

def plot_decision_boundary(model, X, y):
    # Set min and max values and give it some padding
    x_min, x_max = X[0, :].min() - 1, X[0, :].max() + 1
    y_min, y_max = X[1, :].min() - 1, X[1, :].max() + 1
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid
    Z = model(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.ylabel('x2')
    plt.xlabel('x1')
    plt.scatter(X[0, :], X[1, :], c=y, cmap=plt.cm.Spectral)
    

def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size.

    Return:
    s -- sigmoid(x)
    """
    s = 1/(1+np.exp(-x))
    return s

def load_planar_dataset():
    np.random.seed(1)
    m = 400 # number of examples
    N = int(m/2) # number of points per class
    D = 2 # dimensionality
    X = np.zeros((m,D)) # data matrix where each row is a single example
    Y = np.zeros((m,1), dtype='uint8') # labels vector (0 for red, 1 for blue)
    a = 4 # maximum ray of the flower

    for j in range(2):
        ix = range(N*j,N*(j+1))
        t = np.linspace(j*3.12,(j+1)*3.12,N) + np.random.randn(N)*0.2 # theta
        r = a*np.sin(4*t) + np.random.randn(N)*0.2 # radius
        X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
        Y[ix] = j
        
    X = X.T
    Y = Y.T

    return X, Y

def load_extra_datasets():  
    N = 200
    noisy_circles = sklearn.datasets.make_circles(n_samples=N, factor=.5, noise=.3)
    noisy_moons = sklearn.datasets.make_moons(n_samples=N, noise=.2)
    blobs = sklearn.datasets.make_blobs(n_samples=N, random_state=5, n_features=2, centers=6)
    gaussian_quantiles = sklearn.datasets.make_gaussian_quantiles(mean=None, cov=0.5, n_samples=N, n_features=2, n_classes=2, shuffle=True, random_state=None)
    no_structure = np.random.rand(N, 2), np.random.rand(N, 2)
    
    return noisy_circles, noisy_moons, blobs, gaussian_quantiles, no_structureO�i m p o r t   m a t p l o t l i b . p y p l o t   a s   p l t  i m p o r t   n u m p y   a s   n p  i m p o r t   s k l e a r n  i m p o r t   s k l e a r n . d a t a s e t s  i m p o r t   s k l e a r n . l i n e a r _ m o d e l   d e f   p l o t _ d e c i s i o n _ b o u n d a r y ( m o d e l ,   X ,   y ) :          #   S e t   m i n   a n d   m a x   v a l u e s   a n d   g i v e   i t   s o m e   p a d d i n g          x _ m i n ,   x _ m a x   =   X [ 0 ,   : ] . m i n ( )   -   1 ,   X [ 0 ,   : ] . m a x ( )   +   1          y _ m i n ,   y _ m a x   =   X [ 1 ,   : ] . m i n ( )   -   1 ,   X [ 1 ,   : ] . m a x ( )   +   1          h   =   0 . 0 1          #   G e n e r a t e   a   g r i d   o f   p o i n t s   w i t h   d i s t a n c e   h   b e t w e e n   t h e m          x x ,   y y   =   n p . m e s h g r i d ( n p . a r a n g e ( x _ m i n ,   x _ m a x ,   h ) ,   n p . a r a n g e ( y _ m i n ,   y _ m a x ,   h ) )          #   P r e d i c t   t h e   f u n c t i o n   v a l u e   f o r   t h e   w h o l e   g r i d          Z   =   m o d e l ( n p . c _ [ x x . r a v e l ( ) ,   y y . r a v e l ( ) ] )          Z   =   Z . r e s h a p e ( x x . s h a p e )          #   P l o t   t h e   c o n t o u r   a n d   t r a i n i n g   e x a m p l e s          p l t . c o n t o u r f ( x x ,   y y ,   Z ,   c m a p = p l t . c m . S p e c t r a l )          p l t . y l a b e l ( ' x 2 ' )          p l t . x l a b e l ( ' x 1 ' )          p l t . s c a t t e r ( X [ 0 ,   : ] ,   X [ 1 ,   : ] ,   c = y ,   c m a p = p l t . c m . S p e c t r a l )            d e f   s i g m o i d ( x ) :          " " "          C o m p u t e   t h e   s i g m o i d   o f   x           A r g u m e n t s :          x   - -   A   s c a l a r   o r   n u m p y   a r r a y   o f   a n y   s i z e .           R e t u r n :          s   - -   s i g m o i d ( x )          " " "          s   =   1 / ( 1 + n p . e x p ( - x ) )          r e t u r n   s   d e f   l o a d _ p l a n a r _ d a t a s e t ( ) :          n p . r a n d o m . s e e d ( 1 )          m   =   4 0 0   #   n u m b e r   o f   e x a m p l e s          N   =   i n t ( m / 2 )   #   n u m b e r   o f   p o i n t s   p e r   c l a s s          D   =   2   #   d i m e n s i o n a l i t y          X   =   n p . z e r o s ( ( m , D ) )   #   d a t a   m a t r i x   w h e r e   e a c h   r o w   i s   a   s i n g l e   e x a m p l e          Y   =   n p . z e r o s ( ( m , 1 ) ,   d t y p e = ' u i n t 8 ' )   #   l a b e l s   v e c t o r   ( 0   f o r   r e d ,   1   f o r   b l u e )          a   =   4   #   m a x i m u m   r a y   o f   t h e   f l o w e r           f o r   j   i n   r a n g e ( 2 ) :                  i x   =   r a n g e ( N * j , N * ( j + 1 ) )                  t   =   n p . l i n s p a c e ( j * 3 . 1 2 , ( j + 1 ) * 3 . 1 2 , N )   +   n p . r a n d o m . r a n d n ( N ) * 0 . 2   #   t h e t a                  r   =   a * n p . s i n ( 4 * t )   +   n p . r a n d o m . r a n d n ( N ) * 0 . 2   #   r a d i u s                  X [ i x ]   =   n p . c _ [ r * n p . s i n ( t ) ,   r * n p . c o s ( t ) ]                  Y [ i x ]   =   j                           X   =   X . T          Y   =   Y . T           r e t u r n   X ,   Y   d e f   l o a d _ e x t r a _ d a t a s e t s ( ) :              N   =   2 0 0          n o i s y _ c i r c l e s   =   s k l e a r n . d a t a s e t s . m a k e _ c i r c l e s ( n _ s a m p l e s = N ,   f a c t o r = . 5 ,   n o i s e = . 3 )          n o i s y _ m o o n s   =   s k l e a r n . d a t a s e t s . m a k e _ m o o n s ( n _ s a m p l e s = N ,   n o i s e = . 2 )          b l o b s   =   s k l e a r n . d a t a s e t s . m a k e _ b l o b s ( n _ s a m p l e s = N ,   r a n d o m _ s t a t e = 5 ,   n _ f e a t u r e s = 2 ,   c e n t e r s = 6 )          g a u s s i a n _ q u a n t i l e s   =   s k l e a r n . d a t a s e t s . m a k e _ g a u s s i a n _ q u a n t i l e s ( m e a n = N o n e ,   c o v = 0 . 5 ,   n _ s a m p l e s = N ,   n _ f e a t u r e s = 2 ,   n _ c l a s s e s = 2 ,   s h u f f l e = T r u e ,   r a n d o m _ s t a t e = N o n e )          n o _ s t r u c t u r e   =   n p . r a n d o m . r a n d ( N ,   2 ) ,   n p . r a n d o m . r a n d ( N ,   2 )                   r e t u r n   n o i s y _ c i r c l e s ,   n o i s y _ m o o n s ,   b l o b s ,   g a u s s i a n _ q u a n t i l e s ,   n o _ s t r u c t u r e      B [ u	F             	              #�