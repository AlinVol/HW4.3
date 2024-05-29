import random
def generate_random_list():
    random_list = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
    return random_list
def select_elements(lst):
    return [lst[0], lst[2], lst[-2]]

random_list = generate_random_list()
selected_elements = select_elements(random_list)

print("Original list:", random_list)
print("Selected elements:", selected_elements)