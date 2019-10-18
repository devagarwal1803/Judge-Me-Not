import subprocess
def work(solutions):
    fo=open('abc1.c','w')
    fo.write(solutions)
    fo.close()
    r=subprocess.call('gcc abc1.c',shell=True)
    return r
