# orienteering-system

## 项目简介
基于Vue3、JavaScript、Python构成的前、后端，编写的一套适用于一定范围的定向越野游戏。

## 目录结构
```
database/
    db.sqlite3
    manage.py
    .idea/
        .gitignore
        game.iml
        misc.xml
        modules.xml
        workspace.xml
        inspectionProfiles/
game/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
    __pycache__/
hou/
    __init__.py
    admin.py
    apps.py
    db(2).sqlite3
    models.py
    urls.py
    views.py
    __pycache__/
    migrations/
dingxiangyueye/
    .gitignore
    babel.config.js
    jsconfig.json
    package.json
    README.md
    vue.config.js
    public/
        favicon.ico
        index.html
        2048-master/
        bird/
        ...
src/
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

## 如何运行

### Django 项目
1. 进入 `database/` 目录：
    ```sh
    cd database
    ```
2. 运行数据库迁移：
    ```sh
    python manage.py migrate
    ```
3. 启动开发服务器：
    ```sh
    python manage.py runserver
    ```

### Vue.js 项目
1. 进入 `dingxiangyueye/` 目录：
    ```sh
    cd dingxiangyueye
    ```
2. 安装依赖：
    ```sh
    npm install
    ```
3. 启动开发服务器：
    ```sh
    npm run serve
    ```

## 贡献
欢迎提交问题和拉取请求来改进项目。

## 许可证
此项目使用MIT许可证。
