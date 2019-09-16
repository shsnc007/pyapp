# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context
from settings import STATICFILES_DIRS
from models import SncData
import json


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指�?
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def sncapp(request):
    res = SncData.objects.all()
    res_dicts = {"data":[]}
    for row in res:
        res_dict = {}
        res_dict["hname"] = row.hname
        res_dict["iname"] = row.iname
        res_dict["key"] = row.key
        res_dict["delay"] = row.delay
        res_dict["total"] = row.total
        res_dict["count"] = row.count
        res_dict["percent"] = row.percent
        res_dicts["data"].append(res_dict)
    
    with open(STATICFILES_DIRS[0] + '/data.json', 'wb') as f:
        json.dump(res_dicts, f)

    return render_mako_context(request, '/home_application/sncapp.html')