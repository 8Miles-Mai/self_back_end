__author__ = 'miles'
#coding=utf-8
import json
from django.shortcuts import render_to_response
from django.http import HttpResponse

# import env
from back_end.store import store_info


def index(request):
    data = {}
    data["content"] = "#About#  Miles.Mai, fighting force is only 5."
    return render_to_response('back_end/tem.html', {"data": data})


def editor(request):
    return render_to_response('back_end/editor.html', None)


def showup(request):
    data_temp = {}
    data_temp["content"] = '''
#This is a test page.#
> 这里是引用
> 不会自动换行

> <table>
>   <th>sasa</th>
>   <tr><td>lala</td></tr>
> </table>

`lalalala`

> 中间空一行或者在行尾加2个空格才可以换行

'''
    # data = []
    # data.append(data_temp)
    return render_to_response('back_end/showup.html', {"data": data_temp})
    # return HttpResponse(data)


def data(request):
    data_temp = {}
    data_temp["comp_id"] = 123456
    data = []
    data.append(data_temp)
    return render_to_response('back_end/data.html', {"data": data})


def store_info_all(request):
    info = store_info.query_store_info(0)
    # json_result = {}
    # json_result["data"] = info
    json_result = json.dumps(info, indent=4)
    # return HttpResponse(json_result)
    return render_to_response('back_end/data.html', {"data": info})
    # return render_to_response('back_end/data.html', None)


def files(request):
    f = open("/Users/miles/Desktop/excel_files/comp_prod_leafCat_2015-01-25.xls")
    file_data = f.read()
    f.close()
    filename = 'comp_prod_leafCat_2015-01-25.xls'
    response = HttpResponse(file_data, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response