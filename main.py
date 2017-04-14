import rack_space

# rack_space.sq_ft(50, 50)

# for i in range(0, 100):
# 	rack_space.get_random_dim(20000)

# print(rack_space.RACK_Y, rack_space.LANE_Y)
# print(rack_space.get_racks_y(2000))
# print(rack_space.get_racks_y(400))
# print(rack_space.get_racks_y(20000))
# print(rack_space.get_racks_y(40000))
# print(rack_space.get_racks_y(200))
# print(rack_space.get_racks_y(250))
# print("NONE = ", rack_space.get_racks_y(10))

# print(rack_space.get_racks_y(490))
# print(rack_space.get_racks_y(20000))
# print(rack_space.get_racks_y(40000))
# print(rack_space.get_racks_y(200))
# print("NONE = ", rack_space.get_racks_y(10))
#
racks_dict = rack_space.get_racks(20000)
racks_dict_2 = rack_space.get_racks(52500)
rack_space.print_racks_to_excel(racks_dict, 20000)
rack_space.print_racks_to_excel(racks_dict_2, 52500)
print(rack_space.get_racks(104000))
