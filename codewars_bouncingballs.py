def bouncing_ball(h, bounce, window):

    # Three conditions must be met for a valid experiment:
    # Float parameter "h" in meters must be greater than 0
    # Float parameter "bounce" must be greater than 0 and less than 1
    # Float parameter "window" must be less than h.

    if h > 0 and 0 < bounce < 1  and window < h:
        highest_bounce = bounce * h
        n = 1
        while highest_bounce > window:
            highest_bounce *= bounce
            n += 1

        return n
    else:
        return -1
