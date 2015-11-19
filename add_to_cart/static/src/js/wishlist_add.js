

function is_product_in_cart(ele) {
    //console.log("Loading...: " + ele);
    
};

/*
    console.log("DOC-: " + document);
    console.log("1-: " + document.getElementsByName("product_id"));
    console.log("2-: " + document.getElementsByName("product_id").value);
    console.log("30-: " + document.getElementsByName("product_id")[0].value);
    console.log("31-: " + document.getElementsByName("product_id")[1].value);
    console.log("32-: " + document.getElementsByName("product_id")[2].value);
    console.log("33-: " + document.getElementsByName("product_id")[3].value);
    //var product_id = document.getElementsByName("product_id")[0].value;
    //console.log("Product Id: " + product_id);
    //alert(product_id);
    $.ajax({
        url : "/shop/is_product_in_cart", 
		data: { },
        success : function(data) {
        	//alert('Successfully added to wishlist');
        },
        error : function() {
           //alert('Product is already added to wishlist');
        }
    });
    
*/










function add_product_to_wishlist() {
    console.log("create post is working!");
    var product_id = document.getElementsByName("product_id")[0].value;
    //console.log("Product Id: " + product_id);
    //alert(product_id);
    $.ajax({
        url : "/shop/add_product_to_wishlist", 
		data: { product_id: product_id},
        success : function(data) {
        	alert('Successfully added to wishlist');
        },
        error : function() {
           alert('Product is already added to wishlist');
        }
    });
};

function remove_product_from_wishlist(ele) {

	/* TO DELETE PRODUCT FROM MENULIST */
    var tab_parent = ele.parentElement.parentElement.parentElement;
    var tr_parent = ele.parentElement.parentElement;
    var product_id = ele.parentElement.childNodes[1].value;
    //console.log(ele.parentElement.childNodes[1].value);
    tab_parent.removeChild(tr_parent);
    //console.log("Product Id: " + product_id);
    $.ajax({
        url : "/shop/remove_product_from_wishlist/product_id", 
		data: { product_id: product_id},
        success : function() {
        },
        error : function() {
        }
    });
};


function remove_product_from_wishlist_form() {
    console.log("create post is working!");
    var product_id = document.getElementsByName("product_id")[0].value;
    //console.log("Product Id: " + product_id);
    $.ajax({
        url : "/shop/remove_product_from_wishlist_form", 
		data: { product_id: product_id},
        success : function(data) {
        //alert('Product is removed from wishlist')
        },
        /*
        error : function() {
           alert('error');
        }
       */
    });
};

function view_my_wishlist() {
    console.log("create post is working!");
    var product_id = document.getElementsByName("product_id")[0].value;
    //console.log("Product Id: " + product_id);
    $.ajax({
        url : "shop/view_my_wishlist", 
		data: { product_id: product_id},
        success : function() {
        },
        /*
        error : function() {
           alert('error');
        }
       */
    });
};

function add_product_to_wishlist_from_cart(ele) {
    var tab_parent = ele.parentElement.parentElement.parentElement;
    var tr_parent = ele.parentElement.parentElement;
    var product_id = ele.parentElement.childNodes[2].value;
    $.ajax({
        url : "/shop/add_product_to_wishlist_from_cart/product_id", 
		data: { product_id: product_id},
        success : function() {
        	alert('Successfully added to wishlist');
        },
        error : function() {
           alert('Product is already added to wishlist');
        }
    });
};

function add_product_to_wishlist_from_shop(ele) {
    var tab_parent = ele.parentElement.parentElement.parentElement;
    var tr_parent = ele.parentElement.parentElement;
    var product_id = ele.parentElement.childNodes[3].value;
    $.ajax({
        url : "/shop/add_product_to_wishlist_from_shop/product_id", 
		data: { product_id: product_id},
        success : function() {
        	alert('Successfully added to wishlist');
        },
        error : function() {
           alert('Product is already added to wishlist');
        }
    });
};

