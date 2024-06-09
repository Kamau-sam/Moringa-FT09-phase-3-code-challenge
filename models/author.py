from database.connection import CURSOR, CONN

class Author:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int) and value is not None:
            raise TypeError("Id must be of type int")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    def save(self):
        if self.id is None:
            CURSOR.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            CURSOR.execute("UPDATE authors SET name = ? WHERE id = ?", (self.name, self.id))
            CONN.commit()

    def delete(self):
        if self.id is not None:
            CURSOR.execute("DELETE FROM authors WHERE id = ?", (self.id,))
            CONN.commit()
            self.id = None

    @classmethod
    def instance_from_db(cls, row):
        return cls(row[0], row[1])

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM authors")
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]

