#todo: Заданы два списка. Необходимо их сериализовать в один файл.
import pickle


list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
list_two = [False, 'Sparse is better than dense.', {'age': 90}]

output_one = pickle.dumps(list_one)
output_two = pickle.dumps(list_two)


with open('data.pkl', 'wb') as f:
    pickle.dump(list_one, f)
    pickle.dump(list_two, f)

with open('data.pkl', 'rb') as f:
    input_one = pickle.load(f)
    input_two = pickle.load(f)

print(list_one, output_one, input_one, end='\n')
print(list_two, output_two, input_two, end='\n')