transitions = {}
transitions['q00'] = {'0':'q00', '1':'q01'}
transitions['q01'] = {'0':'q10', '1':'q11'}
transitions['q10'] = {'0':'q00', '1':'q01'}
transitions['q11'] = {'0':'q10', '1':'q11'}
start = 'q00'
accept = set(['q11'])

test_cases = ['011', '1101', '1111', '1110', '1010', '10101100011']
for bstr in test_cases:
    state = start
    # Loop through each character in the string
    for c in bstr:
        state = transitions[state][c]
    result = 'reject'
    if state in accept:
        result = 'accept'
    print(bstr, ":", result)