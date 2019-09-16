# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.

用于�?地开发环境的全局配置
"""
from settings import APP_ID


# ===============================================================================
# 数据库�?�置, �?地开发数�?库�?�置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默�?�用mysql
        'NAME': APP_ID,                        # 数据库名 (默�?�与APP_ID相同)
        'USER': 'apps',                        # 你的数据库user
        'PASSWORD': 'apps123',                        # 你的数据库password
        'HOST': '127.0.0.1',                   # 开发的时候，使用localhost
        'PORT': '3306',                        # 默�??3306
    },
}
