import random, math
import copy

RACK_X = 100 / 12
RACK_Y = 50 / 12

RACK_SPACE = RACK_X * RACK_Y
PALLET_SPACE = 40 / 12 * 48 / 12

LANE_X = 120 / 12
LANE_Y = 120 / 12

EMPTY_LANE = LANE_X * LANE_Y

print(RACK_X, RACK_Y, LANE_X, LANE_Y)

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
				lane_left_1 += r_y * 2
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
	max_x_percentage = 0.75
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

	for x in range(min_x, max_x+1):

		# Testing if rounding x up or down will give sq ft closer
		# to total sq ft
		y1 = int(total_sq_ft / x)
		y2 = math.ceil(total_sq_ft / x)
		dif1 = total_sq_ft - y1 * x
		dif2 = total_sq_ft - y2 * x
		if dif1 > dif2:
			y = y2
		else:
			y = y1

		racks = get_best_racks(x, y)
		y_racks_dict = racks["y_racks_dict"]
		x_racks_dict = racks["x_racks_dict"]
		total_racks_ground = y_racks_dict["rack"] * x_racks_dict["rack"]
		total_racks = total_racks_ground * level_racks
		total_pallets = 2 * total_racks
		total_pallet_sq_ft = total_pallets * PALLET_SPACE

		print(x, y, x* y, "Total pallet sq ft", total_pallet_sq_ft, total_racks, x_racks_dict, y_racks_dict)