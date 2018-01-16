from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from interface.JsonModel import GenJSONBar, SeriesBar, SeriesPie, GenJSONPie
from collections import namedtuple

# Create your views here.


def interface(request):
    return render(request, "interface.html", locals())


@csrf_exempt
def get_data(request):
    if request.POST:
        option = {
            "title": {
                "text": 'ECharts 入门示例',
            },
            "tooltip": {},
            "legend": {
                "data": ['销量', '销量2']
            },
            "xAxis": {
                "data": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子", "手套"]
            },
            "yAxis": {},
            "series": [{
                "name": '销量',
                "type": 'bar',
                "data": [5, 20, 36, 10, 10, 20, 33]
            },
                {
                    "name": '销量2',
                    "type": 'bar',
                    "data": [7, 11, 20, 9, 11, 25, 11]
                }]
        }
        return HttpResponse(json.dumps(option, ensure_ascii=False))
    return HttpResponse("没有输入")


@csrf_exempt
def test(request):
    if request.POST:
        q = SeriesBar(name="销量", data=[5, 20, 36, 10, 10, 20, 33])
        q1 = SeriesBar(name="销量2", data=[7, 11, 20, 9, 11, 25, 11])
        q2 = SeriesBar(name="销量3", data=[1, 22, 28, 31, 19, 66, 80])
        # datas = namedtuple("数据类型", "values name")
        # q = SeriesPie(data=[datas(235, "视频广告")], radius="80%")
        # q = SeriesPie(data=[(235, "视频广告"), (274, "联盟广告"), (310, "邮件营销")],
        #               radius="80%", roseType="angle")
        p1 = GenJSONBar(title="销量演示", legend=['销量', '销量2', "销量3"],
                        xAxis=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子", "手套"], series=q, series1=q1, series2=q2)

        # p1 = GenJSONPie(series=q,  tooltip=True)
        last_result = p1.gen()
        # last_result.update({"tooltip": {"trigger": "item", "formatter": "{a} <br/>{b} : {c} ({d}%)"}})
        print(last_result)
        return HttpResponse(json.dumps(last_result, ensure_ascii=False))
    return HttpResponse("没有输出")
