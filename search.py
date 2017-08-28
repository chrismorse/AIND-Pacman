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
  print "*" * 15

  initial_state = problem.getStartState();  
  print initial_state
  frontier = util.Stack()   # use a Stack
  explored_set = set()
  frontier_set = set()
  frontier_set.add(initial_state)

  frontier.push((initial_state,[]))

  while not frontier.isEmpty():
    (node, path) = frontier.pop()

    print "node is ", node
    print "path is ", path
    print "my successors are ", problem.getSuccessors(node)

    if problem.isGoalState(node):
      return path

    explored_set.add(node)

    successors = problem.getSuccessors(node)

    for nextNode, nextNode_direction, cost in successors:
      print "nextNode is ", nextNode
      print "nextNode_direction is ", nextNode_direction
    
      if nextNode not in explored_set and nextNode not in frontier_set:
          frontier.push((nextNode, path + [nextNode_direction]))
          frontier_set.add(nextNode)

  return []
  
  
  print "*" * 15



  


def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"

  initial_state = problem.getStartState();  
  frontier = util.Queue()  # use a Queue
  explored_set = set()
  frontier_set = set()
  frontier_set.add(initial_state)


  frontier.push((initial_state, []))

  while not frontier.isEmpty():
    (node, path) = frontier.pop()

    if problem.isGoalState(node):
      return path

    explored_set.add(node)

    successors = problem.getSuccessors(node)

    for nextNode, nextNode_direction, cost in successors:
    
      if nextNode not in explored_set and nextNode not in frontier_set:
          frontier.push((nextNode, path + [nextNode_direction]))
          frontier_set.add(nextNode)


  return []
  
  






def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"

  print "*" * 15

  initial_state = problem.getStartState();  
  frontier = util.PriorityQueue()  # use a Priority Queue
  explored_set = set()
  frontier_set = set()

  frontier.push((initial_state, []), 0)
  frontier_set.add(initial_state)

  while not frontier.isEmpty():
    (node, path) = frontier.pop()
    print "node is ", node

    if problem.isGoalState(node):
      return path

    cost = problem.getCostOfActions(path)
    explored_set.add(node)

    successors = problem.getSuccessors(node)
    for nextNode, nextNode_direction, nextNode_cost in successors:
      print " -" * 15
      print " nextNode is ", nextNode
      print " nextNode_direction is ", nextNode_direction
      print " nextNode_cost is ", nextNode_cost
      
      totalCost = cost + nextNode_cost
      print " totalCost is ", totalCost
      
      print " -" * 15
      print " "

      if nextNode not in explored_set and nextNode not in frontier_set:
          frontier.push((nextNode, path + [nextNode_direction]), totalCost)
          frontier_set.add(nextNode)
          print "nextNode not in explored", nextNode

    
  return []
  
  print "*" * 15


def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0


def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  
  
  initial_state = problem.getStartState();  
  print "initial_state = ", initial_state
  frontier = util.PriorityQueue()  # use a Priority Queue
  explored_set = set()
  frontier_set = set()

  frontier.push((initial_state, []), 0)
  frontier_set.add(initial_state)

  while not frontier.isEmpty():
    print "*" * 15

    
    (node, path) = frontier.pop()
    print "node is ", node

    #print "path ", path
    

    if problem.isGoalState(node):
      return path

    cost = problem.getCostOfActions(path)
    explored_set.add(node)

    successors = problem.getSuccessors(node)
    for nextNode, nextNode_direction, nextNode_cost in successors:
      print " -" * 15
      print " nextNode is ", nextNode
      print " nextNode_direction is ", nextNode_direction
      #print " nextNode_cost is ", nextNode_cost
      
      totalCost = cost + nextNode_cost
      print " totalCost is ", totalCost
      
      h = heuristic(nextNode, problem)
      print " h is ", h
    
      totalPriority = totalCost + h
      print " totalPriority ", totalPriority
  

      if nextNode not in explored_set and nextNode not in frontier_set: 
          frontier.push((nextNode, path + [nextNode_direction]), totalPriority)
          print "  >> adding to frontier - nextNode", nextNode, " - Priority: ", totalPriority

      print " "

  return []
  
  print "*" * 15
  
  

  
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
