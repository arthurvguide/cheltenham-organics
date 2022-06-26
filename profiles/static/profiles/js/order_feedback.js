$(document).ready(function() {

    $(document).on('click', ".like-feedback", function(){
        var _oid=$(this).attr('data-order');

        $.ajax({
            url:'../profiles/positive_feedback',
            data: {
                order: _oid
            },
            dataType: 'json',
        })

        location.reload();

    })

    $(document).on('click', ".dislike-feedback", function(){
        var _oid=$(this).attr('data-order');

        $.ajax({
            url:'../profiles/negative_feedback',
            data: {
                order: _oid
            },
            dataType: 'json',

        })
        
        location.reload();

    })
});
