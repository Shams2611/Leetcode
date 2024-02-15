def cakes(recipe, available):
    max_cakes = []
    
    for ingredient, required_amount in recipe.items():
        if ingredient in available:
            max_cakes.append(available[ingredient] // required_amount)
            
        else:
            return 0
        
    return min(max_cakes)