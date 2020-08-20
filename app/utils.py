def get_list(query_nodes):
    dict_list = []
    for query in query_nodes:
        dict_list.append(query.to_dict())
    return dict_list
