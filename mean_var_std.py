import numpy as np

def calculate(list):
    
    keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    calculations = {key : [] for key in keys}
    my_arr = np.array(list, dtype=np.float64)
    try:
        my_arr = my_arr.reshape(3,3)
    except ValueError:
        raise ValueError("List must contain nine numbers.")
    trigger = False

    for i in range(0, 3):
        ax = None if trigger is True else i
        calculations['mean'].append(np.mean(my_arr, axis=ax).tolist() if ax is not None else float(np.mean(my_arr, axis=ax)))
        calculations['variance'].append(np.var(my_arr, axis=ax).tolist() if ax is not None else float(np.var(my_arr, axis=ax)))
        calculations['standard deviation'].append(np.std(my_arr, axis=ax).tolist() if ax is not None else float(np.std(my_arr, axis=ax)))
        calculations['max'].append(np.max(my_arr, axis=ax).tolist() if ax is not None else float(np.max(my_arr, axis=ax)))
        calculations['min'].append(np.min(my_arr, axis=ax).tolist() if ax is not None else float(np.min(my_arr, axis=ax)))
        calculations['sum'].append(np.sum(my_arr, axis=ax).tolist() if ax is not None else float(np.sum(my_arr, axis=ax)))
        
        if i == 1: # make the axis None for the flattened calculations
            trigger = True

    return calculations