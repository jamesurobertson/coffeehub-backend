def get_list(query_nodes):
    dict_list = []
    for query in query_nodes:
        dict_list.append(query.to_dict())
    return dict_list


def merge(l1, l2):
    i = j = 0
    out = []
    while True:
        if i == len(l1):
            out.extend(l2[j:])
            break
        elif j == len(l2):
            out.extend(l1[i:])
            break
        elif l1[i] <= l2[j]:
            out.append(l1[i])
            i += 1
        else:
            out.append(l2[j])
            j += 1
    return out
