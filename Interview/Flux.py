# '''
# Write a function that takes the logs as input, builds the transition graph and returns it as an adjacency list with probabilities. Add __START__ and __END__ states.

# Specifically, for each resource, we want to compute a list of every possible next step taken by any user, together with the corresponding probabilities. The list of resources should include __START__ but not __END__, since by definition __END__ is a terminal state.

# Expected output for logs1:
# transition_graph(logs1) # => 
# {
#     '__START__': {'resource_1': 0.25, 'resource_2': 0.125, 'resource_3': 0.5, 'resource_6': 0.125},
#     'resource_1': {'resource_6': 0.333, '__END__': 0.667},
#     'resource_2': {'__END__': 1.0},
#     'resource_3': {'__END__': 0.4, 'resource_1': 0.2, 'resource_2': 0.2, 'resource_3': 0.2},
#     'resource_4': {'__END__': 1.0},
#     'resource_5': {'resource_4': 1.0},
#     'resource_6': {'__END__': 0.5, 'resource_5': 0.5}
# }


# For example, of 8 total users, 4 users have resource_3 as a first visit (user_1, user_2, user_3, user_5), 2 users have resource_1 as a first visit (user_6, user_22), 1 user has resource_2 as a first visit (user_7), and 1 user has resource_6 (user_8) so the possible next steps for __START__ are resource_3 with probability 4/8, resource_1 with probability 2/8, and resource_2 and resource_6 with probability 1/8.

# These are the resource paths per user for the first logs example, ordered by access time:
# {
#     'user_1': ['resource_3', 'resource_3', 'resource_1'],
#     'user_2': ['resource_3', 'resource_2'],
#     'user_3': ['resource_3'],
#     'user_5': ['resource_3'],
#     'user_6': ['resource_1', 'resource_6', 'resource_5', 'resource_4'],
#     'user_7': ['resource_2'],
#     'user_8': ['resource_6'],
#     'user_22': ['resource_1'],
# }


# Expected output for logs2:
# transition_graph(logs2) # => 
# {
#   '__START__': {'resource_3': 1.0},
#   'resource_3': {'resource_3: 0.857, '__END__': 0.143}
# }

# Expected output for logs3:
# transition_graph(logs3) # => 
# {
#   '__START__': {'resource_5': 1.0},
#   'resource_5': {'__END__': 1.0}
# }


# Complexity analysis variables:

# n: number of logs in the input



# '''

# logs1 = [
#     ["58523", "user_1", "resource_1"],
#     ["62314", "user_2", "resource_2"],
#     ["54001", "user_1", "resource_3"],
#     ["200", "user_6", "resource_5"],  
#     ["215", "user_6", "resource_4"],
#     ["54060", "user_2", "resource_3"],
#     ["53760", "user_3", "resource_3"],
#     ["58522", "user_22", "resource_1"],
#     ["53651", "user_5", "resource_3"],
#     ["2", "user_6", "resource_1"],
#     ["100", "user_6", "resource_6"],
#     ["400", "user_7", "resource_2"],
#     ["100", "user_8", "resource_6"],
#     [ "54359", "user_1", "resource_3"],
# ]

# logs2 = [
#     ["300", "user_1", "resource_3"],
#     ["599", "user_1", "resource_3"],
#     ["900", "user_1", "resource_3"],
#     ["1199", "user_1", "resource_3"],
#     ["1200", "user_1", "resource_3"],
#     ["1201", "user_1", "resource_3"],
#     ["1202", "user_1", "resource_3"]
# ]

# logs3 = [
#     ["300", "user_10", "resource_5"]
# ]

# from typing import  List

# def process(logs: List[List[str]]) -> dict:
#     '''process logs with {key:val} -> key: user_id; vals: list[min, max]'''
#     users_logs = {}
    
#     for time, user, _ in logs:
#         time = int(time)
#         if user not in users_logs:
#             users_logs[user] = [time, time]
#         else:
#             mi, mx = users_logs[user]
#             users_logs[user] = [min(time, mi), max(time, mx)]
    
#     return users_logs
            

# # print(process(logs1))


# # recourse_id : key , vals: logs times within 5 min
# # recourse within 5 min
# # (resource, num)

# # Time: N + NLlgL = O(N^2lgN) <--  N (store resources), LlnL (L average size of access for each resource), L
# # Space: O(N)

# # 1 : dict to store resources
# # resouce_id: [2, 34, 200, 500]
# from collections import defaultdict

# def resources(logs: List[List[str]]) -> dict:
#     # 1. store resources 
#     res = defaultdict(list)
#     for time, _, res_id in logs:
#         res[res_id].append(int(time))
    
#     # 1. get the max id, max freq
#     max_res_id = None
#     max_res_freq = 0
#     for res_id, times in res.items():
#         times.sort()
#         l = 0
#         for r in range(len(times)):
#             while times[r] - times[l] > 300:
#                 l += 1
            
#             if r - l + 1 > max_res_freq:
#                 max_res_id = res_id
#                 max_res_freq = r - l + 1
        

#     return (max_res_id, max_res_freq)


# # print(resources(logs1))



# # freq / total 
# # Time: O(N)
# # Space: O(N)
# # 

logs = {
    'user_1': ['resource_3', 'resource_3', 'resource_1'],
    'user_2': ['resource_3', 'resource_2'],
    'user_3': ['resource_3'],
    'user_5': ['resource_3'],
    'user_6': ['resource_1', 'resource_6', 'resource_5', 'resource_4'],
    'user_7': ['resource_2'],
    'user_8': ['resource_6'],
    'user_22': ['resource_1'],
}

from collections import defaultdict
def process_resources(logs: dict) -> dict:
    # 1. create resources
    res_dict = defaultdict(lambda: defaultdict(int))
    for resources in logs.values():
        for i in range(len(resources)):
            if i == 0:
                res_dict['__START__'][resources[i]] += 1
            elif i == len(resources) - 1:
                res_dict[resources[i]]['__END__'] += 1
            else:
                res_dict[resources[i-1]][resources[i]] += 1
    
    # 2. convert freq --> probabilities
    for resources in res_dict.values():
        total = sum(resources.values())
        for k, v in resources.items():
            resources[k] = v / total
    

    return res_dict

print(process_resources(logs))