class Queue:
#Здесь очередь реализована при помощи списка, поэтому она достаточно медленная,
#Временная сложность O(n) для удаления и вставки элемента с одного из концов
#Однако это простая очередь, которую легко реализовать без подключения доп. файлов
    def __init__(self):
        self.students = []
    def add(self, st):
        self.students.insert(0, st)
    def remove(self):
        return self.students.pop()
    def size(self):
        return len(self.students)
    def see(self):
        return self.students

from collections import deque
#Эта очередь позволяет вставлять и удалять объекты со сложностью O(1) с
#обоих концов, при этом сложность O(n) в середине очереди.
#(хотя если это действительно очередь, то какая разница, что там посередине...)
class Q():

    def __init__(self ):
        self.students = deque()
    def add(self, st):
        self.students.appendleft(st)
    def remove(self):
        return self.students.pop()
    def size(self):
        return len(self.students)
    def see(self):
        return self.students
