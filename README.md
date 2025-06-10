# 项目名称

## 项目简介
作为一门科目的结课作业，使用前端(Vue3、JavaScript)、后端(Python)进行开发的全栈项目；包含Django和Vue.js框架的定向越野项目，包括了四个小游戏；使用`leaflet`作为地图的基础功能：地图显示、地图交互、标记点、路径绘制、定位等；
## 主要的界面展示

1. 登录界面

<img width="1163" alt="image" src="https://github.com/user-attachments/assets/974c69bf-cfd3-46e9-9b2d-8eacf5421e11" />

2. 主界面

<img width="1307" alt="image" src="https://github.com/user-attachments/assets/f05b6548-0807-4698-8177-dcf17bb3f0a5" />

3. 任务界面

<img width="1289" alt="image" src="https://github.com/user-attachments/assets/d395bdef-6c56-4a1f-b4d6-4fded96f169c" />


## 目录结构
```
orienteering-system/
├── README.md                           # 项目说明文档
├── .gitignore                         # Git忽略文件配置
│
├── backend/                           # Django后端项目
│   ├── database/                      # 数据库相关
│   │   ├── db.sqlite3                # SQLite数据库文件
│   │   └── manage.py                 # Django管理脚本
│   │
│   ├── game/                         # Django主应用
│   │   ├── __init__.py
│   │   ├── asgi.py                   # ASGI配置
│   │   ├── settings.py               # Django配置文件
│   │   ├── urls.py                   # 主URL路由
│   │   ├── wsgi.py                   # WSGI配置
│   │   └── __pycache__/              # Python缓存文件
│   │
│   └── hou/                          # 业务逻辑应用
│       ├── __init__.py
│       ├── admin.py                  # 管理后台配置
│       ├── apps.py                   # 应用配置
│       ├── models.py                 # 数据模型
│       ├── views.py                  # 视图函数
│       ├── urls.py                   # 应用URL路由
│       ├── db(2).sqlite3             # 备用数据库文件
│       ├── migrations/               # 数据库迁移文件
│       └── __pycache__/              # Python缓存文件
│
├── frontend/                         # Vue.js前端项目
│   └── dingxiangyueye/              # 定向越野游戏前端
│       ├── package.json              # npm依赖配置
│       ├── babel.config.js           # Babel编译配置
│       ├── jsconfig.json             # JavaScript配置
│       ├── vue.config.js             # Vue CLI配置
│       ├── README.md                 # 前端项目说明
│       │
│       ├── public/                   # 静态资源
│       │   ├── index.html            # 入口HTML文件
│       │   ├── favicon.ico           # 网站图标
│       │   ├── 2048-master/          # 2048游戏资源
│       │   ├── bird/                 # 飞鸟游戏资源
│       │   └── [其他游戏资源]/
│       │
│       ├── src/                      # 源代码
│       │   ├── main.js               # Vue应用入口
│       │   ├── App.vue               # 根组件
│       │   ├── store/                # Vuex状态管理
│       │   ├── router/               # Vue Router路由
│       │   ├── components/           # Vue组件
│       │   │   ├── GameMap.vue       # 地图组件
│       │   │   ├── TaskList.vue      # 任务列表组件
│       │   │   ├── PlayerInfo.vue    # 玩家信息组件
│       │   │   ├── GameGuide.vue     # 游戏指导组件
│       │   │   ├── ActivateGame.vue  # 游戏激活组件
│       │   │   ├── GameOne.vue       # 游戏一
│       │   │   ├── GameTwo.vue       # 游戏二
│       │   │   ├── GameThree.vue     # 游戏三
│       │   │   └── GameFour.vue      # 游戏四
│       │   ├── assets/               # 资源文件
│       │   └── utils/                # 工具函数
│       │
│       ├── node_modules/             # npm依赖包
│       └── dist/                     # 构建输出目录
│
└── docs/                            # 项目文档目录
    ├── api.md                       # API文档
    ├── deployment.md                # 部署文档
    └── screenshots/                 # 项目截图
        ├── login.png
        ├── main-interface.png
        └── task-interface.png
```

## 主要文件说明

### Django 部分
- `database/`: 包含Django项目的数据库文件和管理脚本。
  - `db.sqlite3`: 数据库文件。
  - `manage.py`: Django管理脚本。
  - `.idea/`: IDE配置文件。
- `game/`: Django项目的主要应用。
  - `settings.py`: Django项目的配置文件。
  - `urls.py`: URL路由配置。
  - `wsgi.py`: WSGI入口文件。
- `hou/`: 另一个Django应用。
  - `models.py`: 数据模型定义。
  - `views.py`: 视图函数定义。
  - `urls.py`: URL路由配置。

### Vue.js 部分
- `dingxiangyueye/`: 包含Vue.js项目的配置和源代码。
  - `package.json`: 项目依赖和脚本。
  - `vue.config.js`: Vue.js项目配置文件。
  - `public/`: 静态资源文件。
    - `index.html`: 入口HTML文件。

## 环境依赖

### 全局依赖
- Python 3.10（建议）
- Node.js 最新版本
- npm 最新版本

### Django 项目依赖
- Django 最新版即可

### Vue.js 项目依赖
- Vue CLI 最新版本

## 安装步骤

### 克隆项目
```sh
git clone <仓库地址>
cd <项目目录>
```

### 安装Django项目依赖
1. 进入 `database/` 目录：
    ```sh
    cd database
    ```
2. 创建并激活虚拟环境：
    ```sh
    python -m venv venv
    source venv/bin/activate  # 对于Windows用户，使用 `venv\Scripts\activate`
    ```
    测试过程中建议采用`conda`进行环境隔离

### 安装Vue.js项目依赖
1. 进入 `dingxiangyueye/` 目录：
    ```sh
    cd dingxiangyueye
    ```
2. 安装依赖：
    ```sh
    npm install
    ```
    > 如果是Mac用户，上述命令失效时，采用`sudo npm install`，给予文件权限

## 运行项目

### 运行Django开发服务器
1. 进入 `database/` 目录并激活虚拟环境（如果尚未激活）：
    ```sh
    cd database
    source venv/bin/activate
    ```
2. 运行数据库迁移：
    ```sh
    python manage.py migrate
    ```
3. 启动开发服务器：
    ```sh
    python manage.py runserver
    ```
4. (可选) 创建超级管理员
    ```sh
    python manage.py createsuperuser
    ```
完成上述步骤后可对数据库进行可视化管理

<img width="651" alt="image" src="https://github.com/user-attachments/assets/bbaccda2-c7e2-48fd-95c9-2bafdbfab5cd" />


### 运行Vue.js开发服务器
1. 进入 `dingxiangyueye/` 目录：
    ```sh
    cd dingxiangyueye
    ```
2. 启动开发服务器：
    ```sh
    npm run serve
    ```



## 贡献
欢迎提交问题和拉取请求来改进项目。

## 许可证
此项目使用MIT许可证。
