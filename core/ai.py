def suggest(stress):
    if stress > 200:
        return "Increase thickness"
    elif stress < 50:
        return "Reduce material"
    return "Design is optimal"
