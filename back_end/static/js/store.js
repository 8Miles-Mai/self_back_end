
function query_info(selectValue) {
    if(selectValue === 'None') {
        var queryInfo = $('#queryInfo');
        queryInfo.html("");
        return;
    }
    var htmlUrl = '/back_end/' + selectValue;
    var user_id, start, end, item_id;
    $.ajax({
        url: htmlUrl,
        type: 'GET',
        success: function(data) {
            var tpl_store_info = $('#ng-view');
            tpl_store_info.html("");
            if(data == null) {
                tpl_store_info.html("找不到该html页面");
            } else {
                tpl_store_info.append(data);
            }
        },
        async: true
    });
}

//$.ajax({
//    url: '/back_end/store_info_all',
//    type: 'GET',
//    success: function(data) {
//        var tpl_store_info = $('#ng-view');
//        tpl_store_info.html("");
//        if(data == null) {
//            tpl_store_info.html("找不到该html页面");
//        } else {
//            tpl_store_info.append(data);
//        }
//    },
//    async: true
//});