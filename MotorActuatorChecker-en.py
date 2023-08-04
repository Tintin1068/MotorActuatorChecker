while True:
    g = 9.81
    p = 5 
    m = float(input("Rig weight (kg) : "))
    s = float(input("Desired maximum travel speed (mm/s) : "))
    t = 1
    mu = 0.01
    n = int(input("Number of actuators : "))
    k = 0.8
    
    if n == 1:
        d = 100
    else:
        if n == 2:
            d = 55
        else:
            if n == 3:
                d = 35
            else:
                if n == 4:
                    d = 25
                else:
                    if n == 5:
                        d = 20
                    else:
                        if n == 6:
                            d = 16.6666
                        else:
                            if n == 7:
                                d = 14.2857
                            else:
                                if n == 8:
                                    d = 12.5
                                else:
                                    if n > 8:
                                        print("The number of actuators can't be higher than 8.")
                                        d = 0
    
    a = 2 * s / 1000 / t**2
    F = k * m * a + mu * k * m * g
    C = F * d / 1000
    v = s / t / p 
    RPM = v * 60   
    div = 4 / n
    C = F * d / 1000 * div

    print(f"The recommended minimal torque is of {C:.2f} N.m")
    print(f"The recommended maximal rotation speed is of {RPM:.2f} rpm.")

    answer = input("\nEnter 'R' to restart or another letter to quit : ")
    if answer.lower() == "r" or answer.lower() == "R":
        continue
    else:
        break
