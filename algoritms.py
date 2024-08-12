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

graph = {}
costs = {}
parents = {}

graph["start"] ={}
graph["start"]['a'] = 6
graph['start']['b'] = 2

print(graph['start'].keys())