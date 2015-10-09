import numpy as np

def status(sol,d):
    x=sol.x
    y=sol.y
    pi=sol.pi
    
    def objective():
        f=0
        for i in range(d.m):
            for j in range (1,d.n+1):
                f=f+d.happiness[j]*y[j,i]
        return f

    def constraint7():
        boolean=True
        for k in range(d.m):
            sum1=0
            for i in range(0,d.n+1):
                sum2=0
                for j in range(1,d.n+2):
                    sum2=sum2+d.t[i,j]*x[i,j,k]
                sum1=sum1+d.T[i]*y[i,k]+sum2
            boolean=(boolean and (sum1<=d.Tmax))
        if boolean:
            return [boolean,objective()]
        else:
            return [False,7]

    def constraint6():
        boolean=True
        for i in range(d.n+2):
            for j in range(d.n+2):
                for k in range (d.m):
                    boolean=(boolean and (pi[i,k]+d.T[i]+d.t[i,j]-pi[j,k]<=d.M*(1-x[i,j,k])))
        if boolean:
            return constraint7()
        else:
            return [False,6]
            
    def constraint5():
        boolean=True
        for i in range(1,d.n+1):
            for k in range(d.m):
                sum1=np.sum(x[0:d.n+1,i,k])
                sum2=np.sum(x[i,1:d.n+2,k])
                boolean=(boolean and ((sum1==sum2) and (sum1==y[i,k])))
        if boolean:
            return constraint6()
        else:
            return [False,5]

    def constraint4():
        boolean=True
        sum1=0
        for k in range(d.m):
            for i in range(1,d.n+1):
                sum1=sum1+d.cost[i]*y[i,k]
        boolean=(boolean and (sum1<=d.Q))
        if boolean:
            return constraint5()
        else:
            return [False,4]

    def constraint3():
        boolean=True
        for h in range(1,d.n+1):
            boolean=(boolean and (np.sum(y[h,:])<=1))
        if boolean:
            return constraint4()
        else:
            return [False,3]

        
    def constraint2():
        sum1=np.sum(x[0,1:d.n+2,:])
        sum2=np.sum(x[0:d.n+1,d.n+1,:])
        if (((sum1==sum2) and (sum1==d.m))):
            return constraint3()
        else:
            return [False,2]

    def constraint1():
        boolean=True
        for k in range(d.m):
            for i in range (d.n+2):
                boolean=(boolean and (pi[i,k]<=d.end_time[i]))
        if boolean:
            return constraint2()
        else:
            return [False,1]

    
    return (constraint1()) 
    
