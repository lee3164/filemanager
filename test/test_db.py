from modules import config_db
from modules.file import File, User, Group
from common.session import SessionHelper

db_path = './'
db_name = 'test.db'

def insert():
    with SessionHelper() as session:
        for i in range(10):
            uname = 'user' + str(i)
            u = User(uname=uname, usex='M', uemail=uname + '@qq.com',
                     upassword=uname, ucomment=uname)
            gname = 'group' + str(i)
            g = Group(gname=gname, gcomment=gname)
            session.add(u)
            session.add(g)
        session.commit()

def modify():
    u = User.query.filter(User.uname == 'user1').first()
    g0 = Group.query.filter(Group.gname == 'group0').first()
    g1 = Group.query.filter(Group.gname == 'group1').first()
    g2 = Group.query.filter(Group.gname == 'group2').first()
    g3 = Group.query.filter(Group.gname == 'group3').first()

    u.group = [g0, g1, g2]
    g3.user = [u]

    with SessionHelper() as s:
        s.add(u)
        s.add(g0)
        s.add(g1)
        s.add(g2)
        s.add(g3)
        s.commit()

def search():
    u = User.query.filter(User.uname == 'user1').first()
    for g in u.group:
        print g.gname

def main():
    config_db(db_path, db_name)
    search()

if __name__ == '__main__':
    main()