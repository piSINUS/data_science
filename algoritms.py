# бинарный поиск
# def binary_search(list, item):
#     low = 0
#     high = len(list)-1

#     while low <= high:
#         mid = int((low + high)/2)
#         guess = list[mid]
        
#         if guess == item:
#             return mid
        
#         if guess > item:
#             high = mid - 1

#         else:
#             low = mid + 1
#     return None

# my_list = [1,  3,  5,  7, 9]

# print (binary_search(my_list,3))
# print (binary_search(my_list,-1))

# def sumArr(arr):
#     if arr ==[]:
#         return 0
#     return arr[0]+ sum(arr[1:])

# print(sumArr([1,2,3]))

# def kolElArr(arr):
#     if arr == []:
#         return 0
#     return 1 + count(arr[1:])

# def maxarr(list):
#     if len(list)==2:
#         return list[0] if list[0]> list[1] else list[1]
#     sub_max = max(list[1:])
#     return list[0] if list[0] > sub_max else sub_max

# print(maxarr([5,4,3,2,1]))

# book = dict()
# book["milk"] = 1 
# book["av"] = 4
# book['ap'] = 2
# print (book)

# book = { 'milk':['m','i','k']}
# book['m'] = ['zxc']

# print(book['milk'])

# реализация стека

# from collections import deque
# graf = {'you':['alice','bob','claire']}
# graf['bob'] = ['anuj','peggy']
# graf['alice'] = ['peggy']
# graf['claire'] = ['thom','jonny']
# graf['anuj'] = []
# graf['peggy'] = []
# graf['thom'] = []
# graf['jonny'] = []


# def person_is_seller(name):
#     return name[-1] =='m'

# while serch_queue:
#     person = serch_queue.popleft()
#     if person_is_seller(person):

#         print (person + " is a mango saller")
        
#     else:
#         serch_queue += graf[person]

# def person_is_seller(name):
#     return name[-1] =='m'

# def search(name):
#     serch_queue = deque()
#     serch_queue +=graf[name]
#     searched = []
#     while serch_queue:
#         person = serch_queue.popleft()
#         if person_is_seller(person):

#             print (person + " is a mango saller")
            
#         else:
#             serch_queue += graf[person]
#             searched.append(person)
#     return False
# search("you")
# 
# Алгоритм Дейкстры 

# graph = {}
# costs = {}
# parents = {}

# graph["start"] ={}
# graph["start"]['a'] = 6
# graph['start']['b'] = 2
# graph['a'] = {}
# graph['a']['fin'] = 1
# graph['b'] = {}
# graph['b']['a'] = 3
# graph['b']['fin'] = 5
# graph[ 'fin'] ={}

# infinity = float('inf')

# costs = {}
# costs['a'] =6
# costs['b'] = 2
# costs['fin'] = infinity

# parents = {}
# parents['a'] = 'start'
# parents['b'] = 'start'
# parents['in'] = None

# processed = []

# def find_loest_code_node(cost):
#     lowest_code = float("inf")
#     lowest_code_node = None
#     for node in costs:
#         cost = costs(node)
#         if cost < lowest_code and node not in processed:
#             lowest_code = cost 
#             lowest_code_node = node 
#     return lowest_code_node

# print(graph['start'].keys())

#  Жадный алгоритм Задача о покрытии множества

states_needed = set(['mt','wa','or','id','nv','ut','ca','az'])

stations = {}
stations['kone'] = set(['id','nv','ut'])
stations['ktwo'] = set(['wa','id','mt'])
stations['kthree'] = set(['or','nv','ca'])
stations['kfour'] = set(['nv','ut'])
stations['kfive'] = set(['ca','az'])

final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    final_stations.add(best_station)

    states_needed -= states_covered

print (final_stations)