# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html
#import searchAgents

from util import manhattanDistance
from game import Directions
import random, util, sys

from game import Agent

import searchAgents



class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"



    return legalMoves[chosenIndex]

  def evalFood(self,newPos,newFood,currentGameState):

    max = self.posinf
    min = self.posinf

    for fp in newFood:
      #dis = manhattanDistance(newPos, fp)
      dis=searchAgents.mazeDistance(newPos,fp,currentGameState)

      if dis < min:
        min = dis


    if min == self.posinf:
      # print "inif==",min
      result= max
    if min!=0:
      result = 1.0 / min#+random.uniform(0, 5)


    if currentGameState.hasFood(newPos[0],newPos[1]):
      #print "food eval fooddddddddd has fffoooo"
      result=1000
   # print "food result=",result



    return  result

  def evalpacdirection(self,action, currentGameState):
    if action==currentGameState.getPacmanState().configuration.direction:
      return 0.0000001
    return 0

  def evalWall(self,newPos,currentGameState,action):
    x,y=newPos

    walls = currentGameState.getWalls()

    negsum=0
    if walls[x + 1][ y] and action==Directions.EAST:
      negsum=negsum-1
    if walls[x - 1][ y] and action==Directions.WEST:
      negsum = negsum - 1
    if walls[x][ y + 1] and Directions.NORTH:
      negsum = negsum - 1
    if walls[x][y - 1] and action==Directions.SOUTH:
      rnegsum=negsum-1

    return negsum

  def evalGhost(self,newPos,ghostPositions,newScaredTimes):
    """
    if 0 not in newScaredTimes:
      print "eval scared=",newScaredTimes
      return 10
    """
    if newPos in ghostPositions:

      return self.neginf

    x,y=newPos

    #think of last food or pellet
    if (x+1,y) in ghostPositions:
      return -2000
    if (x-1,y) in ghostPositions:
      return -2000
    if (x,y+1) in ghostPositions:
      return -2000
    if (x,y-1) in ghostPositions:
      return -2000

    return 10 # no surrounding ghost



  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (newFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()



    newFood = successorGameState.getFood().asList()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    "*** YOUR CODE HERE ***"
    """
    print "currentpos= ",currentGameState.getPacmanPosition()
    print "action=",action
    print "successorGameState= ",successorGameState
    print "newpos=" ,newPos
    print "newfood=",newFood

    for g in newGhostStates:
      print "newghoststates=",g
    print "newscaredtimes=",newScaredTimes
    """
    self.posinf = 999999
    self.neginf = -self.posinf


    posinf = 999999
    neginf = -posinf

    if action==Directions.STOP:
      return neginf



    ghospos= successorGameState.getGhostPositions()
    #print "gpos=",ghospos

    maxgp=neginf
    for gp in ghospos:
      dispg=manhattanDistance(newPos,gp)
      if maxgp<dispg:
        maxgp=dispg

    if maxgp==neginf:
      maxgp=posinf

    """
    max=posinf
    min=posinf
    for fp in newFood:
      dis=manhattanDistance(newPos,fp)
      if dis<min:
        min=dis

    if min==posinf:
      #print "inif==",min
      return max


    result= 1.0/min

    print "result==",result

    #return result**2+maxgp
    """
    fresult= self.evalFood(newPos,newFood,currentGameState)

    #print "pstate=", currentGameState.getPacmanState(), "vector=",currentGameState.getPacmanState().configuration.direction
    pdresult=self.evalpacdirection(action,currentGameState)
    gposresult=self.evalGhost(newPos,successorGameState.getGhostPositions(),newScaredTimes)

    wallresult=self.evalWall(newPos,currentGameState,action)


    result=pdresult+fresult+gposresult+wallresult
    #print "result==", result
    #print "posss==",newPos
    return result






    return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"
    action = self.max_value(gameState, 0)
    # print action
    return action[1]

  def value(self, gameState, currentDepth, agentIndex):

    if agentIndex >= gameState.getNumAgents():
      currentDepth += 1

    if currentDepth == self.depth or gameState.isLose() or gameState.isWin():
      return self.evaluationFunction(gameState)

    if agentIndex == self.index or agentIndex >= gameState.getNumAgents():
      return self.max_value(gameState, currentDepth)[0]

    if agentIndex != self.index and agentIndex <= gameState.getNumAgents():
      return self.min_value(gameState, currentDepth, agentIndex)[0]

  def min_value(self, gameState, currentDepth, agentIndex):
    # return (min([[self.value(gameState.generateSuccessor(agentIndex, action), currentDepth, agentIndex + 1)] for action in gameState.getLegalActions(agentIndex)]))
    # sys.exit()
    ghostList = []
    for action in gameState.getLegalActions(agentIndex):
      temp = [self.value(gameState.generateSuccessor(agentIndex, action), currentDepth, agentIndex + 1), action]
      if (temp not in ghostList):
        ghostList.append(temp)

    return min(ghostList)

  def max_value(self, gameState, currentDepth):
    # return (min([[self.value(gameState.generateSuccessor(agentIndex, action), currentDepth, agentIndex + 1), action] for action in gameState.getLegalActions(agentIndex)]))
    # sys.exit()
    pacmanList = []
    for action in gameState.getLegalActions(0):
      if (action == 'Stop'):
        continue
      else:
        temp = [self.value(gameState.generateSuccessor(0, action), currentDepth, 1), action]
        if (temp not in pacmanList):
          pacmanList.append(temp)

    return max(pacmanList)

    # util.raiseNotDefined()
    #util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"

    #util.raiseNotDefined()
    action = self.max_value(gameState, 0, float("-inf"), float("inf"))
    # print action
    return action[1]

  def value(self, gameState, currentDepth, agentIndex, alpha, beta):

    if agentIndex >= gameState.getNumAgents():
      currentDepth += 1

    if currentDepth == self.depth or gameState.isLose() or gameState.isWin():
      return self.evaluationFunction(gameState)

    if agentIndex == self.index or agentIndex >= gameState.getNumAgents():
      return self.max_value(gameState, currentDepth, alpha, beta)[0]

    if agentIndex != self.index and agentIndex <= gameState.getNumAgents():
      return self.min_value(gameState, currentDepth, agentIndex, alpha, beta)[0]

  def min_value(self, gameState, currentDepth, agentIndex, alpha, beta):

    v = [float("inf"), ""]

    for action in gameState.getLegalActions(agentIndex):
      temp = [self.value(gameState.generateSuccessor(agentIndex, action), currentDepth, agentIndex + 1, alpha, beta),
              action]

      if (temp[0] < v[0]):
        v = [temp[0], action]

      if (v[0] < alpha):
        return v
      else:
        beta = min(v[0], beta)

    return v

  def max_value(self, gameState, currentDepth, alpha, beta):

    v = [float("-inf"), ""]

    for action in gameState.getLegalActions(0):
      if (action == 'Stop'):
        continue
      else:
        temp = [self.value(gameState.generateSuccessor(0, action), currentDepth, 1, alpha, beta), action]

        if (temp[0] > v[0]):
          v = [temp[0], action]

        if (v[0] > beta):
          return v
        else:
          alpha = max(v[0], alpha)

    return v

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """


  def irpacValue(self,gameState,expectDepth):
    v = self.neginf
    actions= gameState.getLegalActions(0)
    walls = gameState.getWalls()


    for action in actions:



      #print "in pac", " exp depth==",expectDepth
      if action!= Directions.STOP: #is it required
        #print "bef pac gen succ"
        succ=gameState.generateSuccessor(0, action)

        #print "after pac gen succ"
        temp=self.irexpVal(succ,1,expectDepth)

        if v<temp:
          v=temp
          if expectDepth==0:
            self.irfaction=action


    return v








  def irghostValue(self,gameState,nextAgentindex,expectdepth):

    v=0
    actions = gameState.getLegalActions(nextAgentindex)

    if actions:
      p=1.0/len(actions)
    else:
      p=0
    #print "in ghost",nextAgentindex," exp depth", expectdepth
    for action in actions:
      #print "bef ghost gen succ"
      successor=gameState.generateSuccessor(nextAgentindex, action)
      #print "after ghost gen succ"

      if gameState.getNumAgents()-1>nextAgentindex:
     #   print "from ghost",nextAgentindex, " to ghost",nextAgentindex+1
        v = v+ self.irexpVal( successor, nextAgentindex+1,expectdepth)*p
        #return v
      else:
      #  print "from ghost",nextAgentindex," to pac"
        #expectdepth = expectdepth + 1
        v = v + self.irexpVal(successor, 0,expectdepth+1)

        #return v

    #print " v==",v

    return v






  def irexpVal(self, gameState,nextAgentIndex,expectDepth):
    #print "in ireval nextagentindex=",nextAgentIndex, " exp depth==",expectDepth




    if gameState.isLose() or gameState.isWin():# something to add?
      nextAgentIndex = 0
      return self.evaluationFunction(gameState)


    if self.depth == expectDepth:
      expectDepth=0
      nextAgentIndex=0
      #print "....................\n\n"
      return self.evaluationFunction(gameState)

    if nextAgentIndex==0:
      return self.irpacValue(gameState,expectDepth)
    else:
      return self.irghostValue(gameState,nextAgentIndex,expectDepth)


  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction


      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"

    self.neginf=-99999
    self.irfaction='Stop'

    result=self.irexpVal(gameState,0,0)



    return self.irfaction




    util.raiseNotDefined()




def evalFood(currentGameState):
  posinf=999999
  newPos=currentGameState.getPacmanPosition()
  newFood=currentGameState.getFood().asList()


  min=posinf
  for fp in newFood:
    dis = manhattanDistance(newPos, fp)
    #dis=searchAgents.mazeDistance(newPos,fp,currentGameState)
    #print "Hi"
    #sys.exit()
    if dis < min:
      min = dis


  if min != 0:
    result = 1.0 / min
    #result=min

  newGhostStates = currentGameState.getGhostStates()
  newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]





  return (posinf-currentGameState.getNumFood()+result/(.0000001+currentGameState.getNumFood()*1.0))/(.0000001+len(currentGameState.getCapsules()))

def evalNumofAction(currentGameState):
  la=len(currentGameState.getLegalPacmanActions())
  return (la+random.uniform(0,1))/(.0000001+currentGameState.getNumFood())

def evalghoseavoid(currentGameState):
  neginf=-10
  if currentGameState.isLose():
   # print "working"
    return neginf
  return 1




def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
  """
  "*** YOUR CODE HERE ***"
  return (evalFood(currentGameState)+0.5*evalNumofAction(currentGameState))*evalghoseavoid(currentGameState)
  util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """

  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.
      just me
      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)
    """
    "*** YOUR CODE HERE ***"



    return  AlphaBetaAgent(evalFn='better',depth='5').getAction(gameState)
    #return ExpectimaxAgent(evalFn='better',depth='4').getAction(gameState)
    """
    self.evaluationFunction=better
    self.depth=5
    action = self.max_value(gameState, 0, float("-inf"), float("inf"))
    # print action
    return action[1]

  def value(self, gameState, currentDepth, agentIndex, alpha, beta):

    if agentIndex >= gameState.getNumAgents():
      currentDepth += 1

    if currentDepth == self.depth or gameState.isLose() or gameState.isWin():
      return self.evaluationFunction(gameState)

    if agentIndex == self.index or agentIndex >= gameState.getNumAgents():
      return self.max_value(gameState, currentDepth, alpha, beta)[0]

    if agentIndex != self.index and agentIndex <= gameState.getNumAgents():
      return self.min_value(gameState, currentDepth, agentIndex, alpha, beta)[0]

  def min_value(self, gameState, currentDepth, agentIndex, alpha, beta):

    v = [float("inf"), ""]

    for action in gameState.getLegalActions(agentIndex):
      temp = [self.value(gameState.generateSuccessor(agentIndex, action), currentDepth, agentIndex + 1, alpha, beta),
              action]

      if (temp[0] < v[0]):
        v = [temp[0], action]

      if (v[0] < alpha):
        return v
      else:
        beta = min(v[0], beta)

    return v

  def max_value(self, gameState, currentDepth, alpha, beta):

    v = [float("-inf"), ""]

    for action in gameState.getLegalActions(0):
      if (action == 'Stop'):
        continue
      else:
        temp = [self.value(gameState.generateSuccessor(0, action), currentDepth, 1, alpha, beta), action]

        if (temp[0] > v[0]):
          v = [temp[0], action]

        if (v[0] > beta):
          return v
        else:
          alpha = max(v[0], alpha)

    return v

    #util.raiseNotDefined()
    """

