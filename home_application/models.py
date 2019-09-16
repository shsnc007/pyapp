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

from django.db import models

class SncData(models.Model):
    hname = models.CharField(max_length=255)
    hostid = models.IntegerField()
    iname = models.CharField(max_length=255)
    itemid = models.IntegerField()
    key = models.CharField(max_length=255)
    delay = models.CharField(max_length=1024)
    total = models.IntegerField()
    count = models.IntegerField()
    percent = models.FloatField(max_length=10)
    unit = models.CharField(max_length=1)
    remark = models.CharField(max_length=128)