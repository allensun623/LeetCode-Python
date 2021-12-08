''''
https://www.1point3acres.com/bbs/thread-825029-1-1.html
Given list of Log, and max number of logs per log file, print log messages
用hashmap存一下每个logfile出现的frequency，一边录一边打印，直到超过frequency。
Followup：Given list of Log, and max number of logs allowed, print log messages fairly
Example: given files with these number of log messages
F1 : 2
F2 : 10
F3 : 9
Max number of log allowed = 12;
Print these number of logs for each file
F1 : 2
F2 : 5
F3 : 5
我的想法是算出来一个initial average，然后数一下有多少少于average的，匀给那些有多余log message的，保证能有12个file打出来。还是用的hashmap存frequency。
'''


def store_log_files(total: int, logs: list) -> list:
    '''
    n = len of logs
    current average size allowed for each file
    sort logs by files in ascending order -> logs : [(files, index)] 
    iterate logs
    for loop to iterate i, (files, index) from enumerate(logs):
        if files <= current average:
            allow to store all files -> res[index] = files
            total -= files
            recalculate the average -> average = total // (n - i - 1)
        else:
            the remaining logs contain files more than average
            assign current average to the remaining

            for j in (i, n):
                res[logs[j][1]]
                res[logs index] = current average
            break
    return res

    Time: O(NlgN)
    Space: O(N)

    '''
    n = len(logs)
    avg = total // n
    res = [0] * n
    logs = sorted(zip(logs, range(n)))
    print(logs)
    for i, (f, idx) in enumerate(logs):
        if f > avg:
            break
        total -= f
        res[idx] = f
        avg = total // (n - i - 1)
        # for j in range(i, n):
        #     res[logs[j][1]] = avg
        # break
    # for i in range(n):
    #     if res[i] == 0:
    #         res[i] = avg

    # return res
    return [res[i] or avg for i in range(n)]


print(store_log_files(12, [2, 10, 9, 12, 1]))
