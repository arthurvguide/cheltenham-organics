$(document).ready(function() {

    $(document).on('click', ".add-wishlist", function(){
        var _pid=$(this).attr('data-product');
        var _vm=$(this);
        
        
        $.ajax({
            url:'../profiles/add_wishlist',
            data: {
                product: _pid
            },
            dataType: 'json',
            success:function(res){
                if(res.bool==true){
                    _vm.addClass('remove-wishlist').removeClass('add-wishlist')
                }
            }

        })

        location.reload();
        
    } )

    $(document).on('click', ".remove-wishlist", function(){
        var _pid=$(this).attr('data-product');
        var _vm=$(this);
        
        
        $.ajax({
            url:'../profiles/remove_wishlist',
            data: {
                product: _pid
            },
            dataType: 'json',
            success:function(res){
                if(res.bool==true){
                    _vm.addClass('add-wishlist').removeClass('add-wishlist')
                }
            }

        })

        location.reload();
        
    } )
});

