class shopping:
    def calculate_price(cart_items):
        if not cart_items:
            return "empty"
        total_price=sum(cart_items.values())
        if len(cart_items)>5:
            total_price*=0.9
        return total_price
obj=shopping
cart_items=eval(input("Enter keys and items"))
print("Total Price: ",obj.calculate_price(cart_items))