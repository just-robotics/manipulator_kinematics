import numpy as np
    
    
def parse(tf_array_path : str, base_frame_path : str, tool_frame_path : str, flage_frame_path : str):
    def tf(R, t):
        return np.vstack([np.hstack([R, t]),
                          np.hstack([np.zeros((1, 3)), np.ones((1, 1))])])
    
    file = open(tf_array_path, 'r')

    lines = file.readlines()[:-1]

    idx = 0

    tf_array = []

    while idx <= len(lines):
        slice = lines[idx:idx+8]
        # print(slice, end='\n\n')
        t_str = slice[3].strip().split(',')
        t = np.array([[float(t_str[1]), float(t_str[2]), float(t_str[3])]]).reshape(-1, 1) / 1000.0
        R = np.eye(3)
        for i, e in enumerate([slice[5], slice[6], slice[7]]):
            e_str = e.strip().split(',')
            R[:, i] = np.array([[float(e_str[1]), float(e_str[2]), float(e_str[3])]])
        # print(R)
        tf_array.append(tf(R, t))
        idx += 9
        
    file.close()
    
    # BASE FRAME
    
    file = open(base_frame_path, 'r')
    
    lines = file.readlines()
    
    slice = lines[0:8]
    # print(slice, end='\n\n')
    t_str = slice[3].strip().split(',')
    t = np.array([[float(t_str[1]), float(t_str[2]), float(t_str[3])]]).reshape(-1, 1) / 1000.0
    R = np.eye(3)
    for i, e in enumerate([slice[5], slice[6], slice[7]]):
        e_str = e.strip().split(',')
        R[:, i] = np.array([[float(e_str[1]), float(e_str[2]), float(e_str[3])]])
    base_frame = tf(R, t)
    
    # print(base_frame)
    
    file.close()
    
    # TOOL FRAME
    
    file = open(tool_frame_path, 'r')
    
    lines = file.readlines()
    
    slice = lines[0:8]
    # print(slice, end='\n\n')
    t_str = slice[3].strip().split(',')
    t = np.array([[float(t_str[1]), float(t_str[2]), float(t_str[3])]]).reshape(-1, 1) / 1000.0
    R = np.eye(3)
    for i, e in enumerate([slice[5], slice[6], slice[7]]):
        e_str = e.strip().split(',')
        R[:, i] = np.array([[float(e_str[1]), float(e_str[2]), float(e_str[3])]])
    tool_frame = tf(R, t)
    
    # print(tool_frame)
    
    file.close()
    
    # FLAGE FRAME
    
    file = open(flage_frame_path, 'r')
    
    lines = file.readlines()
    
    slice = lines[0:8]
    # print(slice, end='\n\n')
    t_str = slice[3].strip().split(',')
    t = np.array([[float(t_str[1]), float(t_str[2]), float(t_str[3])]]).reshape(-1, 1) / 1000.0
    R = np.eye(3)
    for i, e in enumerate([slice[5], slice[6], slice[7]]):
        e_str = e.strip().split(',')
        R[:, i] = np.array([[float(e_str[1]), float(e_str[2]), float(e_str[3])]])
    flage_frame = tf(R, t)
    
    # print(flage_frame)
    
    file.close()
        
    return base_frame, tool_frame, tf_array


if __name__ == '__main__':
    parse('./tf_array_from_sensor.xls', './base_frame.xls', './tool_frame.xls', './flage_frame.xls')
    