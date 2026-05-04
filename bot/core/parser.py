def parse_input(text):
    params = {}
    words = text.split() # Splits into ["force", "2500"]
    
    # This jumps through the words two at a time
    for i in range(0, len(words), 2): 
        k = words[i]       # "force"
        v = words[i+1]     # "2500"
        params[k] = float(v)
        
    return params
