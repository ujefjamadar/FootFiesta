
from footapp.models import Cart  # Adjust this import based on your actual model path

def cart_items_count(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(uid=request.user.id)
        cart_count = cart_items.count()

    return {'cart_items_count': cart_count}