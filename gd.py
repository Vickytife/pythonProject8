initial_list = [1, 2, 3, 4, 5]
double_list = []
def make_double(input_list):
     for element in input_list:
        double_list.append(2 * element)
print('The initial_list is:')
print(initial_list)
print('Calling the function make_double() now.')
make_double(initial_list)
print('The double_list is():')
print(double_list)
print('The initial_list at present:')
print(initial_list)