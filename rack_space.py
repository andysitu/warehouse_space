import random, math
import copy

RACK_X = 100 / 12
RACK_Y = 50 / 12

RACK_SPACE = RACK_X * RACK_Y
PALLET_SPACE = 40 / 12 * 48 / 12

LANE_X = 120 / 12
LANE_Y = 120 / 12

EMPTY_LANE = LANE_X * LANE_Y

MAX_SQ_FT_COST = 1.0
MIN_SQ_FT_COST = 0.95

PROFIT_MARGIN = .2

def sq_ft(x, y):
	return x * y

def prod_rand_dim(sq_ft):
	random_num = random.random()
	x = sq_ft / random_num
	x = math.sqrt(x)
	y = sq_ft / x

	return(x, y)

def get_longer_edge(x, y):
	if x > y:
		return (x, y)
	else:
		return (y, x)

def get_random_dim(sq_ft):
	x, y = prod_rand_dim(sq_ft)
	print(get_longer_edge(x, y))

def get_racks_y(y):
	global RACK_Y
	r_y = RACK_Y

	global LANE_Y
	l_y = LANE_Y

	MARGIN_LANE_SPACE = 10 / 12

	if y <= (r_y + l_y * 2):
		return None

	# def change_lane(lane_tup, rack, lane):
	# 	if rack > 0:
	# 		lane_tup[2] -= r_y * rack
	# 		lane_tup[1] += rack
	# 	if rack < 0:
	# 		lane_tup[2] += r_y * rack
	# 		lane_tup[1] -= rack
	# 	if lane > 0:
	# 		lane_tup[2] -= l_y * lane
	# 		lane_tup[0] += lane
	# 	if lane < 0:
	# 		lane_tup[2] += l_y * lane
	# 		lane_tup[0] -= lane

	#METHOD 1: NO RACKS ON EDGES
	empty_lane_1 = 0
	rack_1 = 0
	lane_left_1 = y
	# put_lane = False, means that last input was not racks (it was lane)
	# SO put_lane = False means PUT RACKS
	put_lane = True
	while(True):
		if put_lane:
			if lane_left_1 < (l_y - MARGIN_LANE_SPACE):
				rack_1 -= 1
				lane_left_1 += r_y
				break
			lane_left_1 -= l_y
			empty_lane_1 += 1
			# print(lane_left_1, "Racks: ", rack_1, "EMPTY LANES ", empty_lane_1)
			put_lane = False
		else:
			if lane_left_1 < r_y * 2 + (l_y - MARGIN_LANE_SPACE):
				break
			lane_left_1 -= r_y * 2
			rack_1 += 2
			# print(lane_left_1, "Racks: ", rack_1, "EMPTY LANES ", empty_lane_1)
			put_lane = True
		# print(empty_lane_1, rack_1, rack_1*r_y + empty_lane_1*l_y)
	# if rack_1 / 2 - 1 != empty_lane_1:
	# 	rack_1 -= 2

	#METHOD 2: RACKS ON BOTH EDGES
	empty_lane_2 = 0
	rack_2 = 0
	lane_left_2 = y
	# put_lane = False, means that last input was not racks (it was lane)
	# SO put_lane = False means PUT RACKS
	put_lane = True

	lane_left_2 -= r_y
	rack_2 += 1

	while(True):
		if put_lane:
			if lane_left_2 < ((l_y - MARGIN_LANE_SPACE) + r_y):
				# print(lane_left_2)
				rack_2 -= 1
				lane_left_2 += r_y
				# print("GO")
				break
			lane_left_2 -= l_y
			empty_lane_2 += 1
			# print(lane_left_2, "Racks: ", rack_2, "EMPTY LANES ", empty_lane_2)
			put_lane = False
		else:
			if lane_left_2 < (r_y + (l_y - MARGIN_LANE_SPACE)):
				if lane_left_2 < r_y:
					lane_left_2 -= (r_y + l_y)
				else:
					lane_left_2 >= r_y
					rack_2 += 1
					lane_left_2 -= r_y
				break
			lane_left_2 -= r_y * 2
			rack_2 += 2
			# print(lane_left_2, "Racks: ", rack_2, "EMPTY LANES ", empty_lane_2)
			put_lane = True


	#METHOD 3: RACK ON ONE EDGE
	empty_lane_3 = 0
	rack_3 = 0
	lane_left_3 = y

	# put_lane = False, means that last input was not racks (it was lane)
	# SO put_lane = False means PUT RACKS
	put_lane = True

	lane_left_3 -= r_y
	rack_3 += 1

	while(True):
		if put_lane:
			if lane_left_3 < (l_y - MARGIN_LANE_SPACE):
				rack_3 -= 2
				lane_left_3 -= r_y * 2
				break
			lane_left_3 -= l_y
			empty_lane_3 += 1
			# print(lane_left_2, "Racks: ", rack_2, "EMPTY LANES ", empty_lane_2)
			put_lane = False
		else:
			if lane_left_3 < r_y * 2 + (l_y - MARGIN_LANE_SPACE):
				break
			lane_left_3 -= r_y * 2
			rack_3 += 2
			# print(lane_left_2, "Racks: ", rack_2, "EMPTY LANES ", empty_lane_2)
			put_lane = True

	# print(rack_1, empty_lane_1, rack_1*r_y + empty_lane_1*l_y, lane_left_1)
	# print(rack_2, empty_lane_2, rack_2*r_y + empty_lane_2*l_y, lane_left_2)
	# print(rack_3, empty_lane_3, rack_3*r_y + empty_lane_3*l_y, lane_left_3)
	return [	{"rack": rack_1, "empty_lane": empty_lane_1, "feet_used": rack_1*r_y + empty_lane_1*l_y},
				{"rack": rack_2, "empty_lane": empty_lane_2, "feet_used": rack_2*r_y + empty_lane_2*l_y},
				{"rack": rack_3, "empty_lane": empty_lane_3, "feet_used": rack_3*r_y + empty_lane_3*l_y},
																											]

def get_racks_x(x):
	global RACK_X
	r_x = RACK_X

	global LANE_X
	l_x = LANE_X

	MARGIN_LANE_SPACE = 10 / 12

	if x <= l_x * 2 + r_x:
		return None

	empty_lane = 0
	rack = 0
	lane_left = x

	empty_lane += 1
	lane_left -= l_x

	while(True):
		if lane_left < l_x:
			# print(lane_left, l_x)
			rack -= 1
			lane_left += r_x
			empty_lane += 1
			lane_left -= l_x
			# print(lane_left)
			break
		rack += 1
		lane_left -= r_x

	# print(rack, empty_lane, rack*r_x + empty_lane*l_x, lane_left)
	return {"rack": rack, "empty_lane": empty_lane, "feet_used": rack*r_x + empty_lane*l_x, "rack_ft": rack*r_x, "lane_ft": empty_lane*l_x}

def get_best_racks(x, y):
	racks_x_dict = get_racks_x(x)
	racks_y_list = get_racks_y(y)

	def get_best_racks_y(y_list):
		num_methods = 3
		max_racks = 0
		best_method = 0
		for i in range(3):
			if y_list[i]["rack"] > max_racks:
				best_method = i + 1
				max_racks = y_list[i]["rack"]
		best_y = copy.deepcopy(y_list[best_method - 1])
		best_y["method"] = best_method
		return best_y

	racks_y = get_best_racks_y(racks_y_list)

	# total_racks = racks_x * racks_y

	# print("")
	# print("RACKS X ", racks_x_dict)
	# print("RACKS Y ", racks_y_list)
	# print("RACKS BEST Y", racks_y)
	return{"x_racks_dict": racks_x_dict, "y_racks_dict": racks_y}

def get_dimensions(percentage, total_sq_ft):
	y = math.sqrt((total_sq_ft * (1 - percentage)) / percentage)
	x = total_sq_ft / y
	return {"x": x, "y": y, "calculated sq ft": x * y, "total_sq_ft": total_sq_ft}

def get_max_min_x(total_sq_ft):
	min_x_percentage = 0.2
	max_x_percentage = 0.80
	#Returns the max and min dimensions by x ranging from 20% to 50%
	min_x = get_dimensions(min_x_percentage, total_sq_ft)["x"]
	max_x = get_dimensions(max_x_percentage, total_sq_ft)["x"]
	# print(min_y, max_y)
	# print(get_dimensions(min_y_percentage, total_sq_ft), get_dimensions(max_y_percentage, total_sq_ft))
	return {"min_x": min_x, "max_x": max_x}

def get_racks(total_sq_ft):
	level_racks = 3
	racks_dict = {}
	max_min_x = get_max_min_x(total_sq_ft)
	max_x = math.ceil(max_min_x["max_x"])
	min_x =int(max_min_x["min_x"])

	# x & y are the varying dimensinos of the simulated warehouse in ft
	for x in range(min_x, max_x+1):
		y = total_sq_ft / x
		rack_dict = {}

		# Testing if rounding x up or down will give sq ft closer
		# to total sq ft
		# y1 = int(total_sq_ft / x)
		# y2 = math.ceil(total_sq_ft / x)
		# dif1 = total_sq_ft - y1 * x
		# dif2 = total_sq_ft - y2 * x
		# if dif1 > dif2:
		# 	y = y2
		# else:
		# 	y = y1

		racks = get_best_racks(x, y)
		y_racks_dict = copy.deepcopy(racks["y_racks_dict"])
		x_racks_dict = copy.deepcopy(racks["x_racks_dict"])
		# rack_dict["y_racks_dict"] = y_racks_dict
		# rack_dict["x_racks_dict"] = x_racks_dict
		rack_dict["num of racks"] = x_racks_dict["rack"]
		rack_dict["num of racks aisles"] = y_racks_dict["rack"]
		rack_dict["warehouse width_ft"] = x
		rack_dict["warehouse length_ft"] = y
		rack_dict["total_racks_ground"] = y_racks_dict["rack"] * x_racks_dict["rack"]
		rack_dict["total_racks"] = rack_dict["total_racks_ground"] * level_racks
		rack_dict["total_pallets"] = 2 * rack_dict["total_racks"]
		rack_dict["total_pallet_sq_ft"] = rack_dict["total_pallets"] * PALLET_SPACE
		rack_dict["total_sq_ft"] = total_sq_ft

		min_warehouse_cost = total_sq_ft * MIN_SQ_FT_COST
		max_warehouse_cost = total_sq_ft * MAX_SQ_FT_COST
		rack_dict["min_warehouse_total_cost"] = min_warehouse_cost
		rack_dict["max_warehouse_total_cost"] = max_warehouse_cost

		min_profit_total = (min_warehouse_cost * (1 + PROFIT_MARGIN))
		max_profit_total = (max_warehouse_cost * (1 + PROFIT_MARGIN))

		rack_dict["min_sq_ft_charge"] = min_profit_total / rack_dict["total_pallet_sq_ft"]
		rack_dict["max_sq_ft_charge"] = max_profit_total / rack_dict["total_pallet_sq_ft"]
		rack_dict["min cost per pallet"] = min_profit_total / rack_dict["total_pallets"]
		rack_dict["max cost per pallet"] = max_profit_total / rack_dict["total_pallets"]
		pallet_cubic_meter = rack_dict["total_racks"] * 40 * 48 * 72 / 1728 / 35.3147
		rack_dict["total pallet cubic meter"] = pallet_cubic_meter
		rack_dict["min cost by cubic meter"] = min_profit_total / pallet_cubic_meter
		rack_dict["max cost by cubic meter"] = max_profit_total / pallet_cubic_meter
		racks_dict[x] = rack_dict

		# print(rack_dict)
	return racks_dict

def calculate_warehouse_space(rack_aisles, rack_rows, empty_lane_aisles):
	rack_space = rack_aisles * rack_rows * RACK_SPACE
	lanes_space = empty_lane_aisles * rack_rows * LANE_X * RACK_X
	side_lanes_space = empty_lane_aisles * LANE_X * LANE_Y + rack_aisles * RACK_Y * LANE_X 

	total_sq_ft = rack_space + lanes_space + side_lanes_space * 2
	return total_sq_ft

import openpyxl	

alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def print_racks_to_excel(racks_dict, name):
	wb = openpyxl.Workbook()
	sheet = wb.active
	key_added = False
	rack_key = None
	num_racks = len(racks_dict)
	keys_list  = []

	for k, rack_dict in racks_dict.items():
		for rack_k, rack_v in rack_dict.items():
			keys_list.append(rack_k)
		break

	for i, key in enumerate(keys_list):
		sheet[alphabet_list[i] + "1"] = key

	for num_rack, width in enumerate(racks_dict):
		rack_dict = racks_dict[width]
		for i, key in enumerate(keys_list):
			sheet[alphabet_list[i] + str(num_rack + 2)] = rack_dict[key]

	# for k, rack_dict in racks_dict.items():
	# 	for rack_k, rack_v in rack_dict.items():
	# 		if not key_added:
	# 			rack_key = rack_dict.keys()
	# 			key_added = True
	# 			rack_keys_len = len(rack_key)
	# 			for i in range(0, rack_keys_len):
	# 				letter = alphabet_list[i]
	# 				sheet[letter + '1'] = rack_k
		# rack_key = rack_dict.keys()
		# print(rack_key)

	wb.save(str(name) + ".xlsx")