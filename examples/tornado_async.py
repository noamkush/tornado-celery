from tornado import gen
from tornado import ioloop
from tornado.web import RequestHandler, Application

import tasks

import tcelery
tcelery.setup_nonblocking_producer()


class AsyncHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        response = yield gen.Task(tasks.sleep.apply_async, args=[3])
        self.write(str(response.result))
        self.finish()


class MultipleAsyncHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        r1, r2 = yield [gen.Task(tasks.sleep.apply_async, args=[2]),
                        gen.Task(tasks.add.apply_async, args=[1, 2])]
        self.write(str(r1.result))
        self.write(str(r2.result))
        self.finish()


application = Application([
    (r"/async-sleep", AsyncHandler),
    (r"/async-sleep-add", MultipleAsyncHandler),
])


if __name__ == "__main__":
    application.listen(8887)
    ioloop.IOLoop.instance().start()
