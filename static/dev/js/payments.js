const stripe = Stripe(public_key);

function buy_products(element) {
    var product_id = $(element).attr("data-index");
    // Get Checkout Session ID
    fetch("/create-checkout-session/"+ product_id + "/")
    .then((result) => { return result.json(); })
    .then((data) => {
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
        console.log(res);
    });    
}


