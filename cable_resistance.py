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
	>>> example_props = {
		'A_t' : [0.169e-5, 0.101e-4],
		'd_n' : [0.0672, 0.0651],
		'L_n' : [0.0254, 0.0381],
		'resistivity_0' : [0.35e-7, 0.35e-7],
		'alpha_0' : [0.003, 0.003]
		} 
		
	>>> R_dc_stranded(60, 2, example_props)
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
