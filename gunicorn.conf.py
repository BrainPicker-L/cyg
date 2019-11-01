import multiprocessing

bind = "0.0.0.0:8082"   #绑定的ip与端口
workers = 3                #核心数
errorlog = '/home/cyg/gunicorn/gunicorn.error.log' #发生错误时log的路径
accesslog = '/home/cyg/gunicorn/gunicorn.access.log' #正常时的log路径
#loglevel = 'debug'   #日志等级
proc_name = 'gunicorn_cygsite'   #进程名

