import numpy as np
import math

def R_dc(T_c, n, n_props, T_0=20):
	"""
	Compute DC Resistance of a stranded conductor cable at a given temperature.
	T_c: Temperature of conductor (C).
	n: Number of layers.
	n_props: Cable properties, given as a dictionary of lists. Must contain the following keys:
		'n_n' : Number of wires in layer n.
		'd_w' : Diameter of wires in layer n (m).
		'A_t' : Cross-sectional area of layer n (m2) -- replaces 'n_n' and 'd_w'.
		'd_n' : Mean diameter of layer n (m).
		'L_n' : Lay length of layer n (m).
		'resistivity_0' : Resistivity of layer material at reference temperature T_0 (ohm-m).
		'alpha_0' : Temperature coefficient of layer material at reference temperature T_0 (1/C)
	T_0 : Reference temperature (typically 20 C).
	
	EXAMPLE USAGE:
	From Example 7.1 in Anders, G.J., "Rating of Electric Power Cables". IEEE Press (1997).
	"Compute the resistance of the parallel combination of the skid wire and tape for model cable No. 3.
	 The cable shield consists of a mylar tape intercalated with a 7/8 in bronze tape--1 in lay, and a
	 single 0.1 in D-shaped bronze skid wire--1.5 in lay. The diameter over the tape is equal to 2.648 in.
	 Operating temperature is 60 C."
	 
	>>> example_props = {
		'A_t' : [0.169e-5, 0.101e-4],
		'd_n' : [0.0672, 0.0651],
		'L_n' : [0.0254, 0.0381],
		'resistivity_0' : [0.35e-7, 0.35e-7],
		'alpha_0' : [0.003, 0.003]
		} 
		
	>>> R_dc(60, 2, example_props)
	0.019107042682762667
	"""
	
	def R_layer(i):
		if 'A_t' in n_props.keys():
			A_t = n_props['A_t'][i]
		else:
			d_w = n_props['d_w'][i]
			n_n = n_props['n_n'][i]
			A_t = (math.pi)*(d_w**2)*(n_n)/4.0
		d_n = n_props['d_n'][i]
		L_n = n_props['L_n'][i]
		resistivity_0 = n_props['resistivity_0'][i]
		alpha_0 = n_props['alpha_0'][i]
		k_n = (1 + (math.pi*d_n/L_n)**2)**0.5
		Rn_0 = (resistivity_0*k_n)/(A_t)
		Rn = Rn_0*(1 + alpha_0*(T_c - T_0))
		return Rn
	
	call_layers = np.vectorize(R_layer)
	R_layers = call_layers(np.arange(n))
	if n > 1:
		R_dc = (R_layers.prod())/(R_layers.sum())
	else:
		R_dc = R_layers.sum()
	return R_dc

def R_ac(R_dc, grouping=1, d_c=None, s=None, material='aluminum', shape='round',
         arrangement='stranded', treatment='untreated', f=60, prox_method='IEC_287',
		 pipe_correction=1):
	"""
	Compute AC Resistance of a conductor cable based on DC Resistance, accounting for
	skin and proximity effects.
	
	R_dc : DC Resistance of conductor (ohm/m).
	grouping : Number of parallel cables or cable cores (used for proximity effect).
	d_c : Conductor diameter (m) -- used only for proximity effect.
	s : Spacing between parallel conductor centers (m) -- used only for proximity effect.
	material : conductor material (aluminum or copper).
	shape : conductor cross-sectional shape (round or sector-shaped).
	arrangement : cable arrangement (stranded, compact or segmental).
	treatment : whether cable is dried/impregnated (treated or untreated).
	f : frequency (Hz)
	prox_method : which method to use when calculating proximity effect (IEC_287 or Arnold_1941).
	pipe_correction : For pipe-type cables, this value should be 1.5-1.7.
	
	EXAMPLE USAGE:
	From Example 7.3 in Anders, G.J., "Rating of Electric Power Cables". IEEE Press (1997).
	"Compute the AC Resistance (at 90 C) of model cable No. 1 using the IEC 287 method (assume
	 that the cable is not dried or impregnated. The conductor is stranded copper.
	 The DC resistance at 90 C is 7.663e-5 ohm/m. The conductor diameter is 20.5 mm. Three
	 conductors run parallel and the spacing between conductor centers is 71.6 mm.
	 The frequency is 50 Hz.
	 
	>>> R_ac(7.663e-5, grouping=3, d_c=0.0205,s=0.0716, material='copper', f=50)
	7.805533308599811e-05
	>>> R_ac(7.663e-5, grouping=3, d_c=20.5,s=71.6, material='copper', f=50, prox_method='Arnold_1941')
	7.806147003059088e-05
	
	"""

	constants = {
		'copper' : {
			'round' : {
				'stranded' : {
					'treated' : {'k_s': 1, 'k_p' : 0.8},
					'untreated' : {'k_s': 1, 'k_p' : 1}
					},
				'compact' : {
					'treated' : {'k_s': 1, 'k_p' : 0.8},
					'untreated' : {'k_s': 1, 'k_p' : 1}
					},
				'segmental' : {
					'treated' : {'k_s': 0.435, 'k_p' : 0.37},
					'untreated' : {'k_s': 0.435, 'k_p' : 0.37}
					}
				},
			'sector-shaped' : {
					'treated' : {'k_s': 1, 'k_p' : 0.8},
					'untreated' : {'k_s': 1, 'k_p' : 1}
					},
				},
		'aluminum' : {
			'round' : {
				'stranded' : {
					'treated' : {'k_s': 1, 'k_p' : 0.8},
					'untreated' : {'k_s': 1, 'k_p' : 1}
					},
				'four segment' : {
					'treated' : {'k_s': 0.28, 'k_p' : 0.8},
					'untreated' : {'k_s': 0.28, 'k_p' : 1}
					},
				'five segment' : {
					'treated' : {'k_s': 0.19, 'k_p' : 0.8},
					'untreated' : {'k_s': 0.19, 'k_p' : 1}
					},
				'six segment' : {
					'treated' : {'k_s': 0.12, 'k_p' : 0.8},
					'untreated' : {'k_s': 0.12, 'k_p' : 1}
					},
				}
			}
		}
	
	# Compute skin effects.
	k_s = constants[material][shape][arrangement][treatment]['k_s']
	x_s = (k_s*(10**-7)*8*math.pi*f/R_dc)**0.5
	if x_s <= 2.8:
		y_s = (x_s**4)/(192 + 0.8*x_s**4)
	elif 2.8 < x_s <= 3.8:
		y_s = -0.136 - 0.0177*x_s + 0.0563*x_s**2
	else:
		y_s = (x_s/2*(2**0.5)) - 11.0/15.0
		
	# Compute proximity effects.
	if grouping > 1:
		k_p = constants[material][shape][arrangement][treatment]['k_p']	
		x_p = (k_p*(10**-7)*8*math.pi*f/R_dc)**0.5
		a = (x_p**4)/(192 + 0.8*x_p**4)
		y = d_c/s
		
		if x_p > 2.8:
			prox_method = 'Arnold_1941'
		
		def IEC_287(grouping, a, y):
			if grouping == 2:
				y_p = 2.9*a*y
			elif grouping == 3:
				y_p = a*(y**2)*(0.312*y**2 + 1.18/(a + 0.27))
			else:
				y_p = 0
				print('No valid grouping selected for calculation of proximity effects')
			return y_p
				
		def Arnold_1941(x_p, grouping, y):
			if x_p <= 2.8:
				A = (0.042 + 0.012*x_p**4)/(1 + 0.0236*x_p**4)
				B = 0
				G = (11*x_p**4)/(704 + 20*x_p**4)
				H = (1.0/3.0)*(1 + 0.0283*x_p**4)/(1 + 0.0042*x_p**4)
					
			elif 2.8 < x_p <= 3.8:
				A = -0.223 + 0.237*x_p - 0.0154*x_p**2
				B = 0
				G = -1.04 + 0.72*x_p - 0.08*x_p**2
				H = 0.095 + 0.119*x_p + 0.0384*x_p**2
			else:
				A = 0.75 - 1.128*(1/x_p)
				B = 0.094 - 0.376*(1/x_p)
				G = x_p/(4*(2**0.5)) - (1.0/8.0)
				H = (2*x_p - 4.69)/(x_p - 1.16)
				
			if grouping == 2:
				y_p = (G*y**2)/(1 - A*y**2 - B*y**4)
			elif grouping == 3:
				y_p = (G*3*y**2)/(2 - (5.0/12.0)*H*y**2)
			else:
				y_p = 0
				print('No valid grouping selected for calculation of proximity effects')
			return y_p
			
		if prox_method == 'IEC_287':
			y_p = IEC_287(grouping, a, y)
		elif prox_method == 'Arnold_1941':
			y_p = Arnold_1941(x_p, grouping, y)
		else:
			y_p = 0
			print('No valid method selected for calculation of proximity effects')
	else:
		y_p = 0	
	R_ac = R_dc*(1 + pipe_correction*(y_s + y_p))
	return R_ac

def R_dc_T(R_dc, T_0, T_1, alpha_0):
	"""
	Convert DC Resistance at temperature T_0 to DC Resistance at temperature T_1.
	R_dc : DC Resistance at temperature T_0 (ohm/m).
	T_0 : Temperature to convert from (C).
	T_1: Temperature to convert to (C).
	alpha_0 : Temperature coefficient of layer material at reference temperature T_0 (1/C)
	"""
	R_dc_1 = R_dc*(1 + alpha_0*(T_1 - T_0))
	return R_dc_1
