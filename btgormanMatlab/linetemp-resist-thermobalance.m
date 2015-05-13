function [ DIMENSIONS ] = main( Din, R25in, R75in )
%% MAIN Summary of this function goes here
%   ?E = q_gen + q_cond - q_conv + q_rad_in - q_rad_out
%
%   ?E = 0 
%   q_cond = 0
%
%   q_gen + q_rad_in = q_conv + q_rad_out

% aluminum normal = 105 C
% aluminum 24 hr = 130 C
% aluminum 01 hr = 140 C


%% TO BE ASSIGNED
T_line = 0.0;   % line temperature (C)
T_surf = 0.0;   % line surface temperature (C)
T_film = 0.0;   % line film temperature (C)
L = 1.0;        % line lenth (m)

htcoeff = 0.0;
rho = 0.0;
AIRprop = zeros(9,4);
AIRpropmake();

%% INDEPENDENT VARIABLES
T_amb = 0.0;    % ambient temperature (C)
I = 0.0;        % electrical current (A)
D = 0.0;        % line diameter (m)
V = 0.0;        % wind velocity (m / s)

%% CONSTANTS AND PARAMETERS
R = 0.0;        % line resistance (ohm)
R_0 = 0.0;      % line resistivity at temperature T_0 (ohm)
a_T = 0.0;      % temperature coefficient of resistence (K^-1)
T_0 = 0.0;      % reference temperature (C)
k = 0.0;        % air thermal conductivity (W / mK)
a_s = 0.0;      % absorptivity of the line surface (unitless)
e_s = 0.0;      % emissivity of the line surface (unitless)
v = 0.0;        % dynamic viscosity of air (m^2 / s)
Pr = 0.0;       % Prandtl number (unitless)

sigma = 5.6703 * (10 ^ (-8)); % Stefan-Boltzmann constant
pi = 3.14159;

%% DEPENDENT VARIABLES
q_gen = 0.0;    % heat generated in the line by electrical resistive losses (W)
q_cond = 0.0;   % conductive heat transfer within the line (W)
q_conv = 0.0;   % convective heat transfer from the line (W)
q_rad_in = 0.0; % radiative heat added to the line from the sun (W)
q_rad_out= 0.0; % radiative heat lost from the line to the surroundings (W)
I_sun = 0.0;    % incident solar radiation (W / m^2)
A_s = 0.0;      % line surface area (m^2)
A_c = 0.0;      % line cross-sectional area (m^2)
Nu = 0.0;       % Nusselt number;
Ren = 0.0;

%% DECLARATIONS
% All-Aluminum Conductor (AAC)
D = Din * 0.0254; % convert inches to meters
T_0 = 25 + 273; % reference temperature is 25 C
a_T = (R75in/304.8 - R25in/304.8) / 50; % ohms per meter
R_0 = R25in/304.8; % ohms per meter at 25 C

A_c = pi * (0.5 * D) * (0.5 * D);
A_s = pi * D * L;

I_sun = 900.0;
a_s = 0.9;
e_s = 0.9;
I = 1000.0;

%% MAIN

NUMTEMP = 1;
NUMWIND = 1;
tempfact = 1;
windfact = 0.2;

%% MAIN 1

while T_line <= 166.0 + 273.0
    T_amb = 273 + (NUMTEMP-1)*tempfact;
    V = 0.0 + NUMWIND*windfact;

    setAIRprop();

    htcoeff = nusselt() * k / D;

    R4 = e_s * sigma * pi * D;
    R3 = 0.0;
    R2 = 0.0;
    R1 = htcoeff * pi * D - I * I * R_0 * a_T;
    R0 = - (I * I * R_0 - I * I * R_0 * a_T * T_0 + I_sun * a_s * 0.5 * pi * D + htcoeff * pi * D * T_amb + e_s * sigma * pi * D * ( T_amb ^ 4));

    quartroots = roots ( [R4 R3 R2 R1 R0] );

    T_line = quartroots(4);

    NUMTEMP = NUMTEMP + 1;
end

while T_line >= 100.0 + 273.0
    T_amb = 273 + (NUMTEMP-1)*tempfact;
    V = 0.0 + NUMWIND*windfact;

    setAIRprop();

    htcoeff = nusselt() * k / D;

    R4 = e_s * sigma * pi * D;
    R3 = 0.0;
    R2 = 0.0;
    R1 = htcoeff * pi * D - I * I * R_0 * a_T;
    R0 = - (I * I * R_0 - I * I * R_0 * a_T * T_0 + I_sun * a_s * 0.5 * pi * D + htcoeff * pi * D * T_amb + e_s * sigma * pi * D * ( T_amb ^ 4));

    quartroots = roots ( [R4 R3 R2 R1 R0] );

    T_line = quartroots(4);
    NUMWIND = NUMWIND + 1;
end

%% MAIN 2

DIMENSIONS = zeros(NUMWIND,NUMTEMP);
for winditer = 1:NUMWIND
    for tempiter = 1:NUMTEMP
        T_amb = 273 + (tempiter-1)*tempfact;
        V = 0.0 + winditer*windfact;

        setAIRprop();

        htcoeff = nusselt() * k / D;

        R4 = e_s * sigma * pi * D;
        R3 = 0.0;
        R2 = 0.0;
        R1 = htcoeff * pi * D - I * I * R_0 * a_T;
        R0 = - (I * I * R_0 - I * I * R_0 * a_T * T_0 + I_sun * a_s * 0.5 * pi * D + htcoeff * pi * D * T_amb + e_s * sigma * pi * D * ( T_amb ^ 4));

        quartroots = roots ( [R4 R3 R2 R1 R0] );

        T_line = quartroots(4);
        DIMENSIONS(winditer,tempiter) = T_line;
    end
end


%% POST-ANALYSIS

R = R_0 * (1 + a_T * (T_line - T_0)); %ohms per meter at T_line C

%% SUB-FUNCTIONS
    function [ w ] = Q_gen()
        w = I * I * R;
    end

    function [ w ] = Q_rad_in()
        w = I_sun * 0.5 * A_s * a_s;
    end

    function [ w ] = Q_conv()
        w = htcoeff * A_s * (T_line - T_amb);
    end

    function [ w ] = Q_rad_out()
        w = e_s * A_s * sigma * (T_line^4 - T_amb^4);
    end

    function [ r ] = reynolds()
        r = V * D / v;
    end

    function [ n ] = nusselt()
        Ren = reynolds();
        a = 0.62 * ( (Ren) ^ (1/2) ) * ( Pr ^ (1/3) );
        b = (1 + (0.4/(Pr^(2/3) ) ) ) ^ (1/4);
        c = (Ren / 282000) ^ (5/8);
        n = 0.3 + (a/b) * ( (1 + c) ^ (4/5) );
    end

    function [ ] = AIRpropmake()
                       %temp     v             k         Pr
        AIRprop(1,:) = [200 07.59*10^(-6) 18.1*10^(-3) 0.737];
        AIRprop(2,:) = [250 11.44*10^(-6) 22.3*10^(-3) 0.720];
        AIRprop(3,:) = [300 15.89*10^(-6) 26.3*10^(-3) 0.707];
        AIRprop(4,:) = [350 20.92*10^(-6) 30.0*10^(-3) 0.700];
        AIRprop(5,:) = [400 26.41*10^(-6) 33.8*10^(-3) 0.690];
        AIRprop(6,:) = [450 32.39*10^(-6) 37.3*10^(-3) 0.686];
        AIRprop(7,:) = [500 38.79*10^(-6) 40.7*10^(-3) 0.684];
        AIRprop(8,:) = [550 45.57*10^(-6) 43.9*10^(-3) 0.683];
        AIRprop(9,:) = [600 52.69*10^(-6) 46.9*10^(-3) 0.685];
    end

    function [ ] = setAIRprop()
        airIndex = 1;
        
        if T_amb > 600
            disp('YOUGOOF')
        end
        
        for airIter = 1:numel(AIRprop(:,1))-1
            if T_amb <= AIRprop(airIter+1,1)
                airIndex = airIter;
                break;
            end
        end
        
        v = AIRprop(airIndex,2) + ( (T_amb-AIRprop(airIndex,1)) / 50) * (AIRprop(airIndex+1,2) - AIRprop(airIndex,2));
        k = AIRprop(airIndex,3) + ( (T_amb-AIRprop(airIndex,1)) / 50) * (AIRprop(airIndex+1,3) - AIRprop(airIndex,3));
        Pr= AIRprop(airIndex,4) + ( (T_amb-AIRprop(airIndex,1)) / 50) * (AIRprop(airIndex+1,4) - AIRprop(airIndex,4));
    end
            

end

