def cakes(recipe, available):
    max_cakes = []
    
    for ingredient, required_amount in recipe.items():
        if ingredient in available:
            max_cakes.append(available[ingredient] // required_amount)
            
        else:
            return 0
        
    return min(max_cakes)

# Efficient solution 
def cakes(recipe, available):
    ''' Take each ingredient from the recipe, see if it is in the available ones
        and calculate how many full cakes you can make with it.
        If an ingredient is missing, we can't bake a cake. Otherwise we have to
        find the lowest possible amount of cakes.'''
    return min([available[i]//recipe[i] if i in available else 0 for i in recipe])