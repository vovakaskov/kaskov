def pick_peaks(arr):
    pos = []
    peaks = []
    
    peak_pos = -1  
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            peak_pos = i
        elif arr[i] < arr[i - 1]:
            if peak_pos != -1:
                pos.append(peak_pos)
                peaks.append(arr[peak_pos])
                peak_pos = -1
    
    return {"pos": pos, "peaks": peaks}
