def getBondDuration(y, face, couponRate, m, ppy=1):
    # Calculate coupon per period and interest rate per period
    coupon = (face * couponRate) / ppy
    r = y / ppy
    n = m * ppy
    
    bond_price = 0
    weighted_time_pv = 0
    
    # Calculate PV for each period and the weighted time
    for t in range(1, n + 1):
        # Present value of the current coupon
        pv_cash_flow = coupon / (1 + r)**t
        
        # If it's the last period, add the PV of the face value
        if t == n:
            pv_cash_flow += face / (1 + r)**n
            
        # Total bond price (denominator)
        bond_price += pv_cash_flow
        
        # Sum of (time * PV of cash flow) (numerator)
        weighted_time_pv += t * pv_cash_flow
        
    # Macaulay Duration formula (in periods, then divide by ppy for years)
    macaulay_duration = (weighted_time_pv / bond_price) / ppy
    
    return macaulay_duration


