$(document).ready(function() {

    $(document).on('click', ".like-feedback", function(){
        var _oid=$(this).attr('data-order');
        var _vm=$('this');

        $.ajax({
            url:'../profiles/positive_feedback',
            data: {
                order: _oid
            },
            dataType: 'json',
            success:function(res){
                if(res.bool==true){
                    _vm.addClass('disabled')
                }
            }

        })

    })

    $(document).on('click', ".dislike-feedback", function(){
        var _oid=$(this).attr('data-order');
        var _vm=$(this);

        $.ajax({
            url:'../profiles/negative_feedback',
            data: {
                order: _oid
            },
            dataType: 'json',
            success:function(res){
                if(res.bool==true){
                    _vm.addClass('disabled')
                }
            }

        })

    })
});
