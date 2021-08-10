""" ----简介
1、@vue/cli脚手架是一个基于Vue.js进行开发的系统，提供整个前端框架的构建。

2、@vue/cli是一个全局安装的npm包，其提供的vue命令可以快速搭建一个新项目，
以及在项目中也提供了很多易用的工具(vue-cli-service, ESLint集成, 单元测试等)
用于整个项目的开发。
"""

""" ----安装
1、下载node.js安装包，并安装。（Node.js 是一个基于Chrome JavaScript 运行时建立的一个平台。
        可以使Web应用在非浏览器环境下运行？里面包含了npm包管理工具，用来下载@vue/cli包）
    下载地址：https://nodejs.org/zh-cn/download/
    文件夹中：LVuecli/Tools/node-v14.17.4-x64.msi
    安装方式：默认
    1.如果使用npm命令太慢，可以使用npm在全局安装yarn工具
        命令为：npm install -g yarn

2、使用npm命令安装@vue/cli（需开VPN，否则使用npm安装yarn后，使用yarn安装@vue/cli）
    1.使用命令：在cmd中输入 npm install -g @vue/cli,既在全局安装@vue/cli包。
        npm常用命令：
            npm install (-g) (--save) moduleName   
                                1.安装moudleName包，
                                2.有-g参数则表示在全局安装，否则在当前目录下安装
                                3.有--save参数则会将信息写入项目的package.json中，
                                    在删除项目的node_modules文件夹时，使用npm install就可以
                                    安装项目所需的所有依赖包，在项目上传至github时有用（即无需上传node_modules文件夹，
                                    在一个新环境拉取项目后，使用npm install则会生成项目所需的所有依赖包）
            npm uninstall (-g) moudleName   卸载依赖
            npm update (-g) moudleName      更新依赖
            npm list -g                     查看已安装的全局包列表
            npm root -g                     查看全局安装包的位置
    2.或者使用yarn进行安装
        安装命令：yarn global add @vue/cli
        若安装@vue/cli时报错，则修改资源请求地址：
            yarn config set registry https://registry.npm.taobao.org --global
            yarn config set disturl https://npm.taobao.org/dist --global
        安装完毕后，如果输入vue，提示找不到该命令，则输入yarn global bin，并将该命令返回的地址添加到环境变量中。
        yarn常用命令：
            yarn install或者yarn            初始化一个项目，安装package.json中列出的依赖
            yarn build                      编译项目
            yarn add (--dev) (global) moudleName    安装依赖
                                1.有--dev参数则在开发环境中安装依赖，并记录在package.json的dependencies中。
                                2.有global参数则在全局安装依赖
            yarn upgrade (moudleName)       有moudleName则更新指定依赖，否则更新所有依赖
            yarn remove (moudleName)        移除指定依赖
            yarn list (global) (--depth=0)  列出所有依赖
                                1.global为列出所有全局依赖
                                2.--depth为限制依赖的深度

3、创建项目
    1.使用命令vue create cli-demo创建一个名为cli-demo的项目
        ①安装时有多个选项，babel是语法转换，eslint是语法检查。
        ②如果环境中同时存在yarn和npm，则会提示选择使用yarn或者npm安装，如果选择了某个管理工具，
            则在后续的使用中也要使用该工具的命令。
        ③若在上一次create时选择的是自定义配置选项，则下次create时会将上次的配置信息导出，
            如果要重新配置，则在目录C://Users/用户名/.vuerc中删除"myconfig"字段。
        ④如果在创建项目时总是报错，而且不是网络问题，则打开Windows PowerShell，运行yarn --version，
            看是否显示“在此系统上禁止运行脚本”，如果是，则在Windows PowerShell中，运行set-ExecutionPolicy RemoteSigned，
            然后选“全是”。之后（重开cmd或者vscode等命令控制台后）再重新创建项目即可。
        ⑤如果提示缓存文件（cache目录下）出错，则删除该文件后再创建。
    2.使用cd进入cli-demo文件夹后，输入命令npm run serve（yarn serve），即可开启服务

4、常用操作
    1.npm run build（yarn build）
        可以打包项目，打包后的文件在项目中的dist文件夹中，文件为压缩后的格式。
        如果未设置配置文件然后打包，则打包后在dist中的index.html打开无显示，
        是因为路径问题，可以在项目的根目录下新建vue.config.js文件，在文件中
        写入module.exports = {
                publicPath: './'
            }后，重新打包。即可单独运行
    2.vue ui
        可以打开vue的图形化界面，包括插件，配置，依赖等设置，以及项目管理。
    3.

5、安装使用Ant Design of Vue
    1.Ant Design of Vue是基于Vue的美化页面的插件，其中有丰富漂亮简单易用的组件。、
    2.使用命令：npm install ant-design-vue --save即可在当前项目中增加ant-design-vue插件
            或者：yarn add ant-design-vue
    3.
"""

