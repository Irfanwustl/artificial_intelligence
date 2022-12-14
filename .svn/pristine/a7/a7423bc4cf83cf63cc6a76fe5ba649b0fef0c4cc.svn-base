# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

from util import *

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def coreSearch(strategy,problem):
    frontier = strategy
    frontier.push(problem.getStartState())
    exploredSet = set()
    solutionPath = []
    backtractDict = {}

    while True:
        if frontier.isEmpty():
            print "bfs frontier empty"
            return []
        nextState = frontier.pop()

        if problem.isGoalState(nextState):

            dictstate = nextState

            while dictstate != problem.getStartState():
                solutionPath = [backtractDict[dictstate][1]] + solutionPath
                dictstate = backtractDict[dictstate][0]
            #print "path in bfs===",solutionPath
            return solutionPath

        #if nextState not in exploredSet:
        #because a single item can be pushed multiple times
        exploredSet.add(nextState)
        successorsOfNextState = problem.getSuccessors(nextState)

        for eachSuccessorTupple in successorsOfNextState:
            if (eachSuccessorTupple[0] not in exploredSet) and (eachSuccessorTupple[0] not in frontier.list):
                tempList = list(eachSuccessorTupple)
                tempList[0] = nextState
                backtractDict[eachSuccessorTupple[0]] = tempList
                frontier.push(eachSuccessorTupple[0])




def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    return coreSearch(Stack(), problem)

    """

    print "isinstance(problem,SearchProblem)", isinstance(problem,SearchProblem)
    print "type of state ", type(problem.getStartState())
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "type of succs ",type(problem.getSuccessors(problem.getStartState())[0][0])
    print "state", problem.getSuccessors(problem.getStartState())[0][0]
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    """

    frontier = Stack()
    frontier.push(problem.getStartState())
    exploredSet=set()
    solutionPath=[]
    backtractDict={}

    while True:
        if frontier.isEmpty():
            return False
        nextState=frontier.pop()

        if problem.isGoalState(nextState):

            dictstate=nextState

            while dictstate != problem.getStartState():
                solutionPath=[backtractDict[dictstate][1]]+solutionPath
                dictstate=backtractDict[dictstate][0]
       #     print solutionPath
            return solutionPath
        exploredSet.add(nextState)

        successorsOfNextState = problem.getSuccessors(nextState)

        for eachSuccessorTupple in successorsOfNextState:
            if eachSuccessorTupple[0] not in exploredSet:
                tempList = list(eachSuccessorTupple)
                tempList[0]=nextState
                backtractDict[eachSuccessorTupple[0]]=tempList
                frontier.push(eachSuccessorTupple[0])

    """
    """
    print "next state=", nextState
    print "succes of next state ", successorsOfNextState
    while frontier.isEmpty()== False:
        print "frontier=", frontier.pop()

    print "Dict ", backtractDict
    """

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    return coreSearch(Queue(), problem)


class statewithinf:
    def __init__(self, state, parentstatecost,dircetion, backWardcost):
        self.state=state
        self.parentstatecost=parentstatecost
        self.direction=dircetion
        self.backWardcost=backWardcost


def testgeneralCostSearch(strategy,problem):
    frontier = strategy
    nextState = problem.getStartState()

    frontier.push(statewithinf(nextState,0,"noneed",0),0)
    #frontier.push(statewithinf((9,9), 0, "noneed", 0), 99)
    exploredSet = set()
    solutionPath = []
    backtractDict = {}

    #while True:
    if frontier.isEmpty():
        return False
    #x=[nestedf for nestedf in frontier.heap]

    nextStateinf = frontier.pop()
    nextState=nextStateinf.state

    if problem.isGoalState(nextState):

        dictstate = nextState

        while dictstate != problem.getStartState():
            solutionPath = [backtractDict[dictstate][1]] + solutionPath
            dictstate = backtractDict[dictstate][0]
            print "solveeeeeeeee=", solutionPath
        return solutionPath
    exploredSet.add(nextState)
    successorsOfNextState = problem.getSuccessors(nextState)

    for eachSuccessorTupple in successorsOfNextState:

        #print "heap element", [x for nestedf in frontier.heap]

     #   print "in if last check heap element 0==", (9, 9) in [nestedf[1].state for nestedf in frontier.heap], " total==", x

        if (eachSuccessorTupple[0] not in exploredSet) and (eachSuccessorTupple[0] not in [nestedf[1].state for nestedf in frontier.heap]):
      #      print "entereeeeeed"
            tempList = list(eachSuccessorTupple)
            tempList[0] = nextState
            backtractDict[eachSuccessorTupple[0]] = tempList
            frontier.push(statewithinf(eachSuccessorTupple[0],nextStateinf.backWardcost,eachSuccessorTupple[1],nextStateinf.backWardcost+eachSuccessorTupple[2]),nextStateinf.backWardcost+eachSuccessorTupple[2])# state e to cost nai

        elif (eachSuccessorTupple[0] not in exploredSet) and (eachSuccessorTupple[0] in [nestedf[1].state for nestedf in frontier.heap]): #security
            if(nestedf.backWardcost<nextStateinf.backWardcost+eachSuccessorTupple[2]):

                #index=frontier.list.index(nestedf)
                frontier.heap.remove(nestedf)
               # frontier.push(eachSuccessorTupple[0], nextStateinf.backWardcost+eachSuccessorTupple[2])
                frontier.push(statewithinf(eachSuccessorTupple[0], nextStateinf.backWardcost, eachSuccessorTupple[1],
                                           nextStateinf.backWardcost + eachSuccessorTupple[2]),
                              nextStateinf.backWardcost + eachSuccessorTupple[2])

                del backtractDict[eachSuccessorTupple[0]]
                tempList = list(eachSuccessorTupple)
                tempList[0] = nextState
                backtractDict[eachSuccessorTupple[0]] = tempList







def generalCostSearchversion2(strategy,problem):
    frontier = strategy
    nextState = problem.getStartState()

    #print "ucsheap check=", strategy.heap

    frontier.push(statewithinf(nextState,0,"noneed",0),0)
    exploredSet = set()
    solutionPath = []
    backtractDict = {}




    while True:
        #print "a"
        if frontier.isEmpty():
            #print "heap empty"
            return False
       # print "testtttttttttt", frontier.heap.pop()
        nextStateinf = frontier.pop()
        nextState=nextStateinf.state

        if problem.isGoalState(nextState):

            dictstate = nextState

            while dictstate != problem.getStartState():
                solutionPath = [backtractDict[dictstate][1]] + solutionPath
                dictstate = backtractDict[dictstate][0]
            #     print solutionPath
            return solutionPath
        #if nextState not in exploredSet:
        exploredSet.add(nextState)
        successorsOfNextState = problem.getSuccessors(nextState)

        for eachSuccessorTupple in successorsOfNextState:
            if (eachSuccessorTupple[0] not in exploredSet):

                if (eachSuccessorTupple[0] not in exploredSet) and (eachSuccessorTupple[0] not in [nestedf[1].state for nestedf in frontier.heap]):
                #if eachSuccessorTupple[0] not in backtractDict:

                    tempList = list(eachSuccessorTupple)
                    tempList[0] = nextState
                    backtractDict[eachSuccessorTupple[0]] = tempList
                   # frontier.push(statewithinf(eachSuccessorTupple[0]),nextStateinf.backWardcost+eachSuccessorTupple[2])
                    frontier.push(statewithinf(eachSuccessorTupple[0], nextStateinf.backWardcost , eachSuccessorTupple[1],
                                               nextStateinf.backWardcost + eachSuccessorTupple[2]),
                                  nextStateinf.backWardcost + eachSuccessorTupple[2])
                elif (eachSuccessorTupple[0] not in exploredSet) and (eachSuccessorTupple[0] in [nestedf[1].state for nestedf in frontier.heap]): #security
                    if(nestedf[1].backWardcost>nextStateinf.backWardcost+eachSuccessorTupple[2]):
                #else:

                    #index=frontier.list.index(nestedf)
                    #frontier.heap.remove(nestedf)
                    #frontier.push(eachSuccessorTupple[0], nextStateinf.backWardcost+eachSuccessorTupple[2])
                        frontier.push(
                            statewithinf(eachSuccessorTupple[0], nextStateinf.backWardcost, eachSuccessorTupple[1],
                                         nextStateinf.backWardcost + eachSuccessorTupple[2]),
                            nextStateinf.backWardcost + eachSuccessorTupple[2])
                        del backtractDict[eachSuccessorTupple[0]]
                        tempList = list(eachSuccessorTupple)
                        tempList[0] = nextState
                        backtractDict[eachSuccessorTupple[0]] = tempList

def generalCostSearch(strategy,problem):
    frontier = strategy
    nextState = problem.getStartState()

    #print "ucsheap check=", strategy.heap

    frontier.push(statewithinf(nextState,0,"noneed",0),0)
    exploredSet = set()
    solutionPath = []
    backtractDict = {}




    while True:
        #print "a"
        if frontier.isEmpty():
            print "heap empty"
            return False
       # print "testtttttttttt", frontier.heap.pop()
        nextStateinf = frontier.pop()
        nextState=nextStateinf.state

        if problem.isGoalState(nextState):

            dictstate = nextState

            while dictstate != problem.getStartState():
                solutionPath = [backtractDict[dictstate][1]] + solutionPath
                dictstate = backtractDict[dictstate][0]
            #     print solutionPath
            return solutionPath
        if nextState not in exploredSet:
            exploredSet.add(nextState)
            successorsOfNextState = problem.getSuccessors(nextState)

            for eachSuccessorTupple in successorsOfNextState:
                if (eachSuccessorTupple[0] not in exploredSet):

                    #if (eachSuccessorTupple[0] not in exploredSet) and (eachSuccessorTupple[0] not in [nestedf[1].state for nestedf in frontier.heap]):
                    if eachSuccessorTupple[0] not in backtractDict:

                        tempList = list(eachSuccessorTupple)
                        tempList[0] = nextState
                        backtractDict[eachSuccessorTupple[0]] = tempList
                       # frontier.push(statewithinf(eachSuccessorTupple[0]),nextStateinf.backWardcost+eachSuccessorTupple[2])
                        frontier.push(statewithinf(eachSuccessorTupple[0], nextStateinf.backWardcost, eachSuccessorTupple[1],
                                                   nextStateinf.backWardcost + eachSuccessorTupple[2]),
                                      nextStateinf.backWardcost + eachSuccessorTupple[2])
                   # elif (eachSuccessorTupple[0] not in exploredSet) and (eachSuccessorTupple[0] in [nestedf[1].state for nestedf in frontier.heap]): #security
                        #if(nestedf[1].backWardcost>nextStateinf.backWardcost+eachSuccessorTupple[2]):
                    else:

                        #index=frontier.list.index(nestedf)
                        #frontier.heap.remove(nestedf)
                        #frontier.push(eachSuccessorTupple[0], nextStateinf.backWardcost+eachSuccessorTupple[2])
                        frontier.push(
                            statewithinf(eachSuccessorTupple[0], nextStateinf.backWardcost, eachSuccessorTupple[1],
                                         nextStateinf.backWardcost + eachSuccessorTupple[2]),
                            nextStateinf.backWardcost + eachSuccessorTupple[2])
                        del backtractDict[eachSuccessorTupple[0]]
                        tempList = list(eachSuccessorTupple)
                        tempList[0] = nextState
                        backtractDict[eachSuccessorTupple[0]] = tempList








def generalCostSearchv3(strategy,problem):
    frontier = strategy
    nextState = problem.getStartState()

    print "ucsheap check  version3 =", strategy.heap

    frontier.push(statewithinf(nextState,0,"noneed",0),0)
    exploredSet = set()
    solutionPath = []
    backtractDict = {}




    while True:
        #print "a"
        if frontier.isEmpty():
            print "heap empty"
            return False
       # print "testtttttttttt", frontier.heap.pop()

        #heapq.heapify(frontier.heap)  # the change
        nextStateinf = frontier.pop()
        nextState=nextStateinf.state

        if problem.isGoalState(nextState):

            dictstate = nextState

            while dictstate != problem.getStartState():
                solutionPath = [backtractDict[dictstate][1]] + solutionPath
                dictstate = backtractDict[dictstate][0]
            #     print solutionPath
            return solutionPath
        if nextState not in exploredSet:
            exploredSet.add(nextState)
            successorsOfNextState = problem.getSuccessors(nextState)

            for eachSuccessorTupple in successorsOfNextState:
                if (eachSuccessorTupple[0] not in exploredSet):

                    if (eachSuccessorTupple[0] not in [nestedf[1].state for nestedf in frontier.heap]):
                    #if eachSuccessorTupple[0] not in backtractDict:

                        tempList = list(eachSuccessorTupple)
                        tempList[0] = nextState
                        backtractDict[eachSuccessorTupple[0]] = tempList
                       # frontier.push(statewithinf(eachSuccessorTupple[0]),nextStateinf.backWardcost+eachSuccessorTupple[2])
                        frontier.push(statewithinf(eachSuccessorTupple[0], nextStateinf.backWardcost, eachSuccessorTupple[1],
                                                   nextStateinf.backWardcost + eachSuccessorTupple[2]),
                                      nextStateinf.backWardcost + eachSuccessorTupple[2])
                    elif (eachSuccessorTupple[0] in [nestedf[1].state for nestedf in frontier.heap]): #security
                        if(nestedf[1].backWardcost>nextStateinf.backWardcost+eachSuccessorTupple[2]):


                            #index=frontier.list.index(nestedf)
                            frontier.heap.remove(nestedf)
                            #heapq.heapify(frontier.heap)

                            #frontier.push(eachSuccessorTupple[0], nextStateinf.backWardcost+eachSuccessorTupple[2])
                            frontier.push(
                                statewithinf(eachSuccessorTupple[0], nextStateinf.backWardcost, eachSuccessorTupple[1],
                                             nextStateinf.backWardcost + eachSuccessorTupple[2]),
                                nextStateinf.backWardcost + eachSuccessorTupple[2])
                            heapq.heapify(frontier.heap)  # the change
                            del backtractDict[eachSuccessorTupple[0]]
                            tempList = list(eachSuccessorTupple)
                            tempList[0] = nextState
                            backtractDict[eachSuccessorTupple[0]] = tempList











def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    unip=PriorityQueue()
    return generalCostSearch(unip, problem)
    #return generalCostSearchv3(unip, problem)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0



def AstarCostSearch(strategy,problem,heuristic):
    frontier = strategy
    nextState = problem.getStartState()

    #print "A star changed=",strategy.heap

    frontier.push(statewithinf(nextState,0,"noneed",0),heuristic(nextState,problem))
    exploredSet = set()
    solutionPath = []
    backtractDict = {}

    while True:
        if frontier.isEmpty():
            return []
       # print "testtttttttttt", frontier.heap.pop()
        nextStateinf = frontier.pop()
        nextState=nextStateinf.state

        if problem.isGoalState(nextState):#  whatttttttttt

            dictstate = nextState

            while dictstate != problem.getStartState():
                solutionPath = [backtractDict[dictstate][1]] + solutionPath
                dictstate = backtractDict[dictstate][0]
            #     print solutionPath
            return solutionPath
        if nextState not in exploredSet:
            exploredSet.add(nextState)
            successorsOfNextState = problem.getSuccessors(nextState)

            for eachSuccessorTupple in successorsOfNextState:
                #if (eachSuccessorTupple[0] not in exploredSet):

                if (eachSuccessorTupple[0] not in exploredSet) and (eachSuccessorTupple[0] not in [nestedf[1].state for nestedf in frontier.heap]):
                    #if eachSuccessorTupple[0] not in backtractDict:

                    tempList = list(eachSuccessorTupple)
                    tempList[0] = nextState
                    backtractDict[eachSuccessorTupple[0]] = tempList
                   # frontier.push(statewithinf(eachSuccessorTupple[0]),nextStateinf.backWardcost+eachSuccessorTupple[2])
                    frontier.push(statewithinf(eachSuccessorTupple[0], nextStateinf.backWardcost, eachSuccessorTupple[1],nextStateinf.backWardcost + eachSuccessorTupple[2]), nextStateinf.backWardcost + eachSuccessorTupple[2]+heuristic(eachSuccessorTupple[0],problem))
                elif (eachSuccessorTupple[0] not in exploredSet) and (eachSuccessorTupple[0] in [nestedf[1].state for nestedf in frontier.heap]): #security
                    if(nestedf[1].backWardcost+heuristic(eachSuccessorTupple[0],problem)>nextStateinf.backWardcost+eachSuccessorTupple[2]+heuristic(eachSuccessorTupple[0],problem)):  #redundancy
                    #else:
                        #index=frontier.list.index(nestedf)
                        frontier.heap.remove(nestedf)
                        #frontier.push(eachSuccessorTupple[0], nextStateinf.backWardcost+eachSuccessorTupple[2])
                        frontier.push(
                            statewithinf(eachSuccessorTupple[0], nextStateinf.backWardcost, eachSuccessorTupple[1],
                                         nextStateinf.backWardcost + eachSuccessorTupple[2]),
                            nextStateinf.backWardcost + eachSuccessorTupple[2]+heuristic(eachSuccessorTupple[0],problem))
                        heapq.heapify(frontier.heap) #the change
                        del backtractDict[eachSuccessorTupple[0]]
                        tempList = list(eachSuccessorTupple)
                        tempList[0] = nextState
                        backtractDict[eachSuccessorTupple[0]] = tempList







def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"

    #print "in aaaaaaaaaaaaaaaa"

    astap=PriorityQueue()
    return  AstarCostSearch(astap,problem,heuristic)

    #print "in aaaaaaaaaaaaaaaa"
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
