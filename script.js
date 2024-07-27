let cart = [];

function addToCart(product, size) {
    const item = {
        name: product,
        size: size
    };
    cart.push(item);
    updateCart();
}

function updateCart() {
    const cartItems = document.getElementById('cart-items');
    cartItems.innerHTML = '';
    cart.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - Size: ${item.size}`;
        cartItems.appendChild(li);
    });
}

function checkout() {
    alert('Order placed successfully!');
    cart = [];
    updateCart();
}

