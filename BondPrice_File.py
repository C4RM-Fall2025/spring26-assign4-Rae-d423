def getBondPrice(y, face, couponRate, m, ppy=1):
    # Calculate the coupon payment per period
    coupon_payment = (face * couponRate) / ppy
    
    # Total number of payment periods
    n = m * ppy
    
    # Periodic interest rate (YTM per period)
    r = y / ppy
    
    bondPrice = 0
    
    # Sum the present value of all coupon payments
    for t in range(1, n + 1):
        bondPrice += coupon_payment / (1 + r)**t
        
    # Add the present value of the face value (principal) at maturity
    bondPrice += face / (1 + r)**n
    
    return bondPrice
