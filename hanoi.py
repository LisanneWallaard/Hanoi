# initial code to set up Python ACT-R
import ccm
from ccm.lib.actr import *
log=ccm.log()

# define the model
class Hanoi(ACTR):
    def stop(goal='n:?disks source:?a destination:?c auxiliary:?b current:1 random:?blub'):
        print 'Move disk 1 from peg',a ,'to peg',c

    def TowerOfHanoi1(goal='n:?disks source:?a destination:?c auxiliary:?b current:!1 random:1'):
        goal.modify(n = disks-1)
        goal.modify(source = a)
        goal.modify(destination = b)
        goal.modify(auxiliary = c)
        goal.modify(current = disks-1)
        goal.modify(random ='2')
        print 'Move disk',disks,'from source',a,'to destination',c

    def TowerOfHanoi2(goal='n:?disks source:?a destination:?c auxiliary:?b current:!1 random:1'):    
        goal.modify(n = disks-1)
        goal.modify(source = b)
        goal.modify(destination = c)
        goal.modify(auxiliary = a)
        goal.modify(current = disks-1)
        goal.modify(random ='1')

        
# run the model        
model=Hanoi()
ccm.log_everything(model)
model.goal.set('n:3 source:A destination:C auxiliary:B current:3 random:1')
model.run()
