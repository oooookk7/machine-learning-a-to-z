
def split_into_classes(x_data_inverse, y_data):
    cls_0 = {'x': [], 'y': []}
    cls_1 = {'x': [], 'y': []}

    for i, ix in enumerate(x_data_inverse):
        if y_data[i] == 1:
            cls_1['x'].append(ix[0])
            cls_1['y'].append(ix[1])
        else:
            cls_0['x'].append(ix[0])
            cls_0['y'].append(ix[1])

    return cls_0, cls_1
