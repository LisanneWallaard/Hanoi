# initial code to set up Python ACT-R
import ccm
from ccm.lib.actr import *
log=ccm.log(html=True)

# class that solves the tower of hanoi game
class Hanoi(ACTR):
    goal=Buffer()

    def step1(goal='pegA:123 pegB:empty pegC:empty'):
        print 'Disk 3 was moved from peg A to peg C'
        print 'Peg A has disks [12], peg B has disks [], peg C has disks [3]'
        goal.modify(pegA='12', pegC='3')    
    def step2(goal='pegA:12 pegB:empty pegC:3'):
        print 'Disk 2 was moved from peg A to peg B'
        print 'Peg A has disks [1], peg B has disks [2], peg C has disks [3]'
        goal.modify(pegA='1', pegB='2', pegC='3') 
    def step3(goal='pegA:1 pegB:2 pegC:3'):
        print 'Disk 3 was moved from peg C to peg B'
        print 'Peg A has disks [1], peg B has disks [23], peg C has disks []'
        goal.modify(pegB='23', pegC='empty') 
    def step4(goal='pegA:1 pegB:23 pegC:empty'):
        print 'Disk 1 was moved from peg A to peg C'
        print 'Peg A has disks [], peg B has disks [23], peg C has disks [1]'
        goal.modify(pegA='empty', pegC='1') 
    def step5(goal='pegA:empty pegB:23 pegC:1'):
        print 'Disk 3 was moved from peg B to peg A'
        print 'Peg A has disks [3], peg B has disks [2], peg C has disks [1]'
        goal.modify(pegA='3', pegB='2') 
    def step6(goal='pegA:3 pegB:2 pegC:1'):
        print 'Disk 2 was moved from peg B to peg C'
        print 'Peg A has disks [3], peg B has disks [], peg C has disks [12]'
        goal.modify(pegB='empty', pegC='12') 
    def step7(goal='pegA:3 pegB:empty pegC:12'):
        print 'Disk 3 was moved from peg A to peg C'
        print 'Peg A has disks [], peg B has disks [], peg C has disks [123]'
        goal.modify(pegA='empty', pegC='123')       
    def finished(goal='pegA:empty pegB:empty pegC:123'):
        print 'Finished moving disks, goal achieved'
        goal.clear()
        
        
# run the model        
model=Hanoi()
ccm.log_everything(model)
model.goal.set('pegA:123 pegB:empty pegC:empty')
model.run()
