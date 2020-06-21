# Name:Baichuan Chi
# PSID:1938207


class FoodItem:  # Define class to contain nutrition information about a food

    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0, serving=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.serving = serving

    def get_calories(self, num_servings):
        calories = (self.fat * 9 + self.carbs * 4 + self.protein * 4) * num_servings
        return calories

    def print_info(self):  # Set up a method in the class to print
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
        print('Number of calories for {:.2f} serving(s): {:.2f}'.format(self.serving, self.get_calories(self.serving)))


if __name__ == '__main__':
    input_name = input()
    input_fat = float(input())
    input_carbs = float(input())
    input_protein = float(input())
    input_serving = float(input())
    none = FoodItem(serving=input_serving)
    food = FoodItem(input_name, input_fat, input_carbs, input_protein, input_serving)
    none.print_info()
    print()
    food.print_info()

