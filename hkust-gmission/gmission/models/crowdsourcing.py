__author__ = 'chenzhao'


from base import *


class Task(db.Model, BasicModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))
    brief = db.Column(db.String(500))

    attachment_id = db.Column(db.Integer, db.ForeignKey('attachment.id'))
    attachment = db.relationship('Attachment', foreign_keys=attachment_id)

    credit = db.Column(db.Integer, default=10)
    status = db.Column(db.String(20), default='open')  # or closed
    required_answer_count = db.Column(db.Integer, default=3)
    begin_time = db.Column(db.DateTime, default=datetime.datetime.now)
    end_time = db.Column(db.DateTime, default=lambda:datetime.datetime.now()+datetime.timedelta(days=1))
    created_on = db.Column(db.DateTime, default=datetime.datetime.now)

    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    location = db.relationship('Location', foreign_keys=location_id)

    requester = db.relationship('User')
    requester_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    answers = db.relationship('Answer', lazy='select')
    # answers = db.relationship('Answer', backref=db.backref('task', lazy='select'), lazy='select')

    def __unicode__(self):
        return '<%s,%s>' % (repr(self.id), self.task)


class Answer(db.Model, BasicModelMixin):
    id = db.Column(db.Integer, primary_key=True)

    task = db.relationship('Task', lazy='select')
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))

    brief = db.Column(db.String(100))

    attachment = db.relationship('Attachment', lazy='immediate')
    attachment_id = db.Column(db.Integer, db.ForeignKey('attachment.id'))

    type = db.Column(db.String(20))
    accepted = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now)

    location = db.relationship('Location', lazy='select')
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))

    worker = db.relationship('User', lazy='select')
    worker_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __unicode__(self):
        return '<%d,%s,%s>' % (self.id, self.task, self.option)

