def getBondPrice_Z(face, couponRate, times, yc):
    # Calculate the fixed annual coupon payment
    coupon = face * couponRate
    
    bondPrice = 0
    
    # Use zip to pair each time point with its corresponding yield
    for t, y in zip(times, yc):
        # Calculate PV of the coupon for this specific time point
        pv_coupon = coupon / (1 + y)**t
        bondPrice += pv_coupon
        
    # Note: In this specific problem context (as shown in the Excel image), 
    # the last cash flow in the list often includes the face value repayment.
    # We add the discounted face value based on the final time and yield.
    last_t = times[-1]
    last_y = yc[-1]
    bondPrice += face / (1 + last_y)**last_t
            
    return bondPrice
