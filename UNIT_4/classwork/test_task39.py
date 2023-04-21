from package_ser_deser import deserializer, serializer


obj_list = [1, 2, 3, 4, 5]
obj_dict = {'1': 23,
            '2': 45,
            '3': 56}


serializer.to_pickle(obj_list, 'data.pkl')
serializer.to_pickle(obj_dict, 'data_1.pkl')

obj_1 = deserializer.from_pickle('data.pkl')
obj_2 = deserializer.from_pickle('data_1.pkl')

serializer.to_json(obj_list, 'data.js')
serializer.to_json(obj_dict, 'data_1.js')

obj_3 = deserializer.from_json('data.js')
obj_4 = deserializer.from_json('data_1.js')

serializer.to_yaml(obj_list, 'data.yml')
serializer.to_yaml(obj_dict, 'data_1.yml')

obj_5 = deserializer.from_yaml('data.yml')
obj_6 = deserializer.from_yaml('data_1.yml')

print(obj_1, obj_2, obj_3, obj_4, obj_5, obj_6)
