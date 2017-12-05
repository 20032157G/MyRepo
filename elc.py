

## COORDENADAS ELIPTICAS AFINES

def neg(P):
    return (x,-y,z)

def doub(P):
    return add(P,P)

def add(P1,P2):
    [x1,y1,z1]=P1
    [x2,y2,z2]=P2
    if(z1==0)return P2
    if(z2==0)return P1
    if(x1==x2)
        if(y1+y2==0)return (0,1,0)
        m=(3*pow(x1,2)+a)*)/(2*y1)
    else
        m=(y2-y1)/(x2-x1)
    x3=pow(m,2)-x1-x2
    return (x3,m(x1-x3)-y1,1)

def sub(P1,P2):
	return add(P1,neg(P2))

#E=EllipticCurve([-5,4])

##COORDENADAS ELIPTICAS PROYECTIVAS MODIFICADAS
def neg(P):
	return (P[0],-P[1],P[2])

def double:
	if(P[1]==0||P[2]==0)
        	return [0,1,0]
	M=(3*pow(P[0],3)+a*pow(P[2],4))
	S=4*P[0]*pow(P[1],2)
	x=pow(M,2)-2*S
	y=M*(S-P2)-8*pow(P[1],3)
	z=2*P[1]*P[2]
    return [x,y,z]

def add(P,Q):
	if(P[2]==0)return Q
	if(Q[2]==0)return P
	u=Q[0]*pow(P[2],2)
	v=P[0]*pow(Q[2],2)
	r=Q[1]*pow(P[2],3)
	s=P[1]*pow(Q[2],3)
	W=u-v
	S=r-s
	if(W==0):
        	if(S==0):
			return double(P)
		return [0,1,0]
	T=u+v
	M=r+s
	R[0]=pow(S,2)-T*pow(W,2))
	R[1]=((T*pow(W,2)-R[0])-M*pow(W,3))
	R[2]=P[2]*Q[2]*W
	return R

def sub(P,Q):
	return add(P,neg(Q))

import numpy as np
def nP(P,Q,m):
	if(m%3==0):
		n=m//3
		if(n==0)return [0,1,0]
			B=np.binary_repr(m)
			b=np.binary_repr(n)
			b0=np.zeros(len(B))
			for(i in range(len(b))):
				b0[i]=b[i]
			for(i in range(1,len(B)-1):
				Q=double(Q)
			if((B[i],b0[i])==(1,0)):
				Q=add(Q,P)
			if((B[i],b0[i])==(0,1)):
				Q=sub(Q,P)
	return Q               










