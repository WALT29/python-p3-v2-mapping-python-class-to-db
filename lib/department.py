class Department:
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"
    
    @classmethod
    def create_table(cls):
        from __init__ import CURSOR, CONN
        """creates a new table that persists attributes of the department class"""
        sql="""
            CREATE TABLE IF NOT EXISTS departments(
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT     
            ) 
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        from __init__ import CURSOR, CONN
        sql="""
            DROP TABLE IF EXISTS departments;        
        """
        CURSOR.execute(sql) 
        CONN.commit()
    
    #this instance method stores the instance attributes to the table and gets the id of the object
    def save(self):
        from __init__ import CURSOR, CONN
        sql="""
            INSERT INTO departments (name,location)
            VALUES(?,?)
        """
        CURSOR.execute(sql,(self.name,self.location))
        CONN.commit()
        self.id=CURSOR.lastrowid;
    
    
    #this method creates an object that is an instance of cls
    @classmethod
    def create(cls,name,location):
        department=cls(name,location) #creates an instance of a Department
        department.save()
        return department
    
    def update(self):
        from __init__ import CURSOR, CONN
        sql="""
            UPDATE departments 
            SET name=? ,location=?
            WHERE id=?
        """
        CURSOR.execute(sql,(self.name,self.location,self.id))
        CONN.commit()
    
    def delete(self):
        from __init__ import CURSOR, CONN
        sql="""
            DELETE FROM departments
            WHERE id=?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        