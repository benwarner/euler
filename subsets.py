import copy

def list_sublists(input_list):
    sublists = [[[]]]
    for listsize in range(len(input_list)):
        print 'dude'
        sublist = sublists[listsize]
        newsublist = []
        for subsublist in sublist:
            print 'yo'
            norderlist = []
            for element in input_list:
                print 'finally'
                norderlist.append(subsublist.extend(element))
            print norderlist
            norderset = set(tuple(norderlist))
            print 'still going'
            print norderset
            norderlist = list(norderset)
            newsublist.append(norderlist)
            print sublists
        sublists.append(newsublist)

    return sublists

def subtuples(input_tuple):
    subtuples = ((()))
    for tuplesize in range(len(input_tuple)):
        print 'dude'
        subtuple = subtuples[tuplesize]
        newsubtuple = ()
        for subsubtuple in subtuple:
            print 'yo'
            nordertuple = ()
            for element in input_tuple:
                print 'finally'
                extendedsubsubtuple = subsubtuple
                extendedsubsubtuple += (element,)
                nordertuple += (extendedsubsubtuple,)
            print nordertuple
            norderset = set(nordertuple)
            print 'still going'
            print norderset
            nordertuple = tuple(norderset)
            newsubtuple += (nordertuple,)
            print subtuples
        subtuples += (newsubtuple,)

    return subtuples

def test(testlist):
    sublists = [[]]
    sublist = copy.deepcopy(sublists[0])
    for element in testlist:
        placeholder = sublist
        sublists.append(placeholder.extend(element))
    return sublists
