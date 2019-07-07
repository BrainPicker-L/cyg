import multiprocessing

bind = "0.0.0.0:8000"   #绑定的ip与端口
workers = 2                #核心数
errorlog = './gunicorn/gunicorn.error.log' #发生错误时log的路径
accesslog = './gunicorn/gunicorn.access.log' #正常时的log路径
#loglevel = 'debug'   #日志等级
proc_name = 'gunicorn_cygsite'   #进程名

