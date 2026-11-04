logs = [
    ('alice',True),
    ('bob',False),
    ('alice',True),
    ('alice',False),
    ('bob',True),
    ('charlie',False)
]

def analyze_logins(logs):
    
    dict_log = {}
    
    for name, status in logs:
        if name not in dict_log:
            dict_log[name] = {'success':0,'failed':0}
        if status == True:
            dict_log[name]['success'] += 1
        else:
            dict_log[name]['failed'] += 1
    return dict_log

a = analyze_logins(logs)
print(a)