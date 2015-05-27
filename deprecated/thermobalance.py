import math
import numpy as np

def T_c(I, T_amb, V, D, R_list, N_cond=1, T_range=[298,323,348], a_s=0.9, e_s=0.9, I_sun=900.0, temp_factor=1, wind_factor=1, n_iter=10):
    """
    %% TO BE ASSIGNED

        T_line          % line temperature (C)
        T_surf          % line surface temperature (C)
        T_film          % line film temperature (C)
        L               % line length (m)

    %% INDEPENDENT VARIABLES

        T_amb           % ambient temperature (C)
        I               % electrical current (A)
        D               % line diameter (m)
        V               % wind velocity (m / s)

    %% CONSTANTS AND PARAMETERS

        R               % line resistance (ohm)
        R_0             % line resistivity at temperature T_0 (ohm)
        a_T             % temperature coefficient of resistance (K^-1)
        T_0             % reference temperature (C)
        k               % air thermal conductivity (W / mK)
        a_s             % absorptivity of the line surface (unitless)
        e_s             % emissivity of the line surface (unitless)
        v               % dynamic viscosity of air (m^2 / s)
        Pr              % Prandtl number (unitless)
        sigma           % Stefan-Boltzmann constant

    %% DEPENDENT VARIABLES

        q_gen           % heat generated in the line by electrical resistive losses (W)
        q_cond          % conductive heat transfer within the line (W)
        q_conv          % convective heat transfer from the line (W)
        q_rad_in        % radiative heat added to the line from the sun (W)
        q_rad_out       % radiative heat lost from the line to the surroundings (W)
        I_sun           % incident solar radiation (W / m^2)
        A_s             % line surface area (m^2)
        A_c             % line cross-sectional area (m^2)
        Nu              % Nusselt number
        Re              % Reynolds number

    """

    # def Q_gen(I, R):
    #     w = I * I * R
    #     return w

    # def Q_rad_in(I_sun, A_s, a_s):
    #     w = I_sun * D * a_s
    #     return w

    # def Q_conv(htcoeff, A_s, T_lin, T_amb):
    #     w = htcoeff * A_s * (T_line - T_amb)
    #     return w

    # def Q_rad_out(e_s, A_s, sigma, T_line, T_amb):
    #     w = e_s * D * sigma * (T_line**4 - T_amb**4)
    #     return w

    def reynolds(V, D, v, Mair=1.103):
        r = V * D / v
        return r

    def nusselt(Re, Pr):
        a = 0.62 * ( (Re) ** (1.0/2.0) ) * ( Pr ** (1.0/3.0) )
        b = (1 + (0.4/(Pr**(2.0/3.0) ) ) ) ** (1.0/4.0)
        c = (Re / 282000) ** (5.0/8.0)
        n = 0.3 + (a/b) * ( (1 + c) ** (4.0/5.0) )
        return n

    def air_prop(T_amb):
                          #   temp    v         k       Pr
        air_prop = np.array([[200,  7.59e-6, 18.1e-3, 0.737],
                             [250, 11.44e-6, 22.3e-3, 0.720],
                             [300, 15.89e-6, 26.3e-3, 0.707],
                             [350, 20.92e-6, 30.0e-3, 0.700],
                             [400, 26.41e-6, 33.8e-3, 0.690],
                             [450, 32.39e-6, 37.3e-3, 0.686],
                             [500, 38.79e-6, 40.7e-3, 0.684],
                             [550, 45.57e-6, 43.9e-3, 0.683],
                             [600, 52.69e-6, 46.9e-3, 0.685]])

        v, k, Pr = np.apply_along_axis(lambda x: np.interp(T_amb, air_prop[:,0], x),
                                                        0, air_prop[:,1:])
        return v, k, Pr

    def R_T(R_lo, R_mid, R_hi, T_line, N_cond, T_range=T_range):
        if 273 <= T_line <= 323:
            R =   ((R_lo + 
                  ((R_lo - R_mid)/(T_range[0] - T_range[1]))
                  *(T_line - T_range[0]))/N_cond)
        elif T_line > 323:
            R =   ((R_mid + 
                  ((R_mid - R_hi)/(T_range[1] - T_range[2]))
                  *(T_line - T_range[1]))/N_cond)
        else:
            R = R_lo
            print('Out of bounds')
        return R

    R_lo, R_mid, R_hi = R_list[0], R_list[1], R_list[2]
    temp_factor = 1
    wind_factor = 1
    sigma = 5.6703e-8  # Stefan-Boltzmann constant

    T_amb = T_amb*temp_factor
    V = V*wind_factor

    v, k, Pr = air_prop(T_amb)
    Re = reynolds(V, D, v)
    htcoeff = nusselt(Re, Pr) * k / D

    def T_line(T_init):
        
        R = R_T(R_lo, R_mid, R_hi, T_init, N_cond)
        print R

        C4 = e_s * sigma * D * math.pi
        C3 = 0.0
        C2 = 0.0
        C1 = htcoeff * D * math.pi
        C0 = - (   I ** 2 * R
                 + I_sun * a_s * D
                 + htcoeff * D * math.pi * T_amb
                 + e_s * D * math.pi * sigma * (T_amb ** 4))

        return np.roots([C4, C3, C2, C1, C0])

    T_c = T_amb
   
    for i in range(n_iter):
        T_arr = T_line(T_c)
        T_c = np.real(T_arr[np.where((np.real(T_arr) > 0) & ~(np.iscomplex(T_arr)))]).mean()
        print T_c

    return T_c

R_1000ft = np.array([0.0186, 0.0205, 0.0222])
R_list = R_1000ft*(3.28084/1000)
RT = T_c(1220.0, 293.0, 1.0, 30.39e-3, R_list, 1, I_sun=1000.0, e_s = 0.5, a_s = 0.5)
