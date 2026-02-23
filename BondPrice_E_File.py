def getBondPrice_E(face, couponRate, yc):
    # Calculate the fixed coupon payment for each period
    coupon = face * couponRate
    
    bondPrice = 0
    
    # Use enumerate to get both the index (i) and the yield (y) for each period
    # i starts from 0, so the time period t = i + 1
    for i, y in enumerate(yc):
        t = i + 1
        
        # Calculate PV of the coupon for this period
        pv_coupon = coupon / (1 + y)**t
        bondPrice += pv_coupon
        
        # If it is the last period, add the PV of the face value
        if t == len(yc):
            bondPrice += face / (1 + y)**t
            
    return bondPrice

