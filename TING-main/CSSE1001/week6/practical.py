store = {
    'fruits': {
        'apple': 1.5,
        'banana': 0.5,
        'cherry': 2.0
    },
    'drinks': {
        'water': 0.8,
        'soda': 1.2
    }
}
def get_price(category, product):
    category,_ ,item =product.partition('.')
    return store[category][item]
print(get_price(store, 'fruits.apple'))