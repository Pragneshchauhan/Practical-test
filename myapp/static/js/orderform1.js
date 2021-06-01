function proprice(price){
    let showPrice = document.getElementById('showPrice');
    showPrice.value = price;
}

function calculateAmount(val){
    let price = document.getElementById('showPrice').value;
    let totalprice = price * val;
    let total = document.getElementById('total');
    total.value = totalprice;
}







