import tornado.websocket
import tornado.gen
import tornado.web
import rethinkdb as r
import json

clients = []

r.set_loop_type('tornado')

@tornado.gen.coroutine
def print_changes():
    conn = yield r.connect(host="localhost", port=28015)
    feed = yield r.db("rethinkdb_chat").table('messages').changes(include_states=False).run(conn)
    while (yield feed.fetch_next()):
        change = yield feed.next()
        for client in clients:
            client.write_message(change)

class MessageHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        conn = yield r.connect(host='localhost', port=28015, db='rethinkdb_chat')
        messages = yield r.db('rethinkdb_chat').table('messages').order_by('created').coerce_to('array').run(conn)
        self.write(json.dumps(messages))

class SocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        self.stream.set_nodelay(True)
        if self not in clients:
            clients.append(self)
        print len(clients)

    @tornado.gen.coroutine
    def on_message(self, message):
        new_message_object = json.loads(message)
        conn = yield r.connect(host="localhost", port=28015)
        new_message = yield r.db("rethinkdb_chat").table('messages').insert(new_message_object).run(conn)

    def on_close(self):
        for i, client in enumerate(clients):
            if client is self:
                del clients[i]
                return
