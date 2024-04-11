import sqlite3
import hashlib
import utility
# Create or connect to a database
conn = sqlite3.connect('cars.db')
c = conn.cursor()

while True:
    slave = input("enter command...")

#ask what everything dose
    if slave == "/?":
        print("Commands list:\n/add_car\n/add_engine\n/com\n/view_cars\n/view_engines\n/del\n/quit")

    if slave == "/-_-":
        userpass = input("input password").encode('utf-8')
        hash_object = hashlib.sha256(userpass)
        hex_dig = hash_object.hexdigest()
        #print(hex_dig)
        if hex_dig == "ce9036a66131c62790eeb5f07d68a21776dd03c2f3ab302e51c62e8ce96ebecb":
            print("pass")
        else:
            print("fail")
# Insert car data into the car table 
    if slave == "/add_car":
        print("select make acquardingly")
        c.execute("SELECT * FROM make")
        for row in c.fetchall():
             print(row)
        make = input("Make: ")
        model = input("Model: ")
        while True:
            print("Is Your Engine On The Below List")
            c.execute("SELECT * FROM engine")
            for row in c.fetchall():
                 print(row)
            answer = input("(y) or (n)")
            if answer == "y":
                 engine = input("Engine: ")
                 break
            if answer == "n":
                name = input("name")
                c.execute("INSERT INTO engine (engine_name ) VALUES (?)", (name,))

        stockhp = input("Stock Horse Power: ")
        stocktorque = input("Stock Torque: ")
        image = input("Image(leave null):")
        print("select drive acquardingly")
        c.execute("SELECT * FROM drive")
        for row in c.fetchall():
             print(row)
        drive = input(":")

        c.execute("INSERT INTO car (make, model, engine, stockhp, stocktorque, image, drive) VALUES (?, ?, ?, ?, ?, ?, ?)", (make, model, engine, stockhp, stocktorque, image, drive))




# Insert engine data into the car table 
    if slave == "/add_engine":
        name = input("name")
        c.execute("INSERT INTO engine (engine_name ) VALUES (?)", (name,))




# Commit changes
    if slave == "/com":
        conn.commit()
        print("saved")



# Fetch and print car table
    if slave == "/view_cars":
        c.execute("select make.whatmake, car.model, car.engine, car.stockhp, car.stocktorque from car join make on car.make = make.id")
        print("All car:")
        for row in c.fetchall():
            print(row)


# Fetch and print all rows
    if slave == "/view_engines":
        c.execute("SELECT * FROM engine")
        print("All car:")
        for row in c.fetchall():
            print(row)

# Mr Rodkiss easteregg
    if slave == "/fish":
        print("🙄")

# Delete data from the table
    if slave == "/del":
        table = input("what would you like to delete (car=1) (engine=2)")
        if table == "1":
            c.execute("SELECT * FROM car")
            for row in c.fetchall():
                print(row)
            what = input()
            c.execute("DELETE FROM car WHERE car_id = ?", (what,))
        if table == "2":
            c.execute("SELECT * FROM engine")
            for row in c.fetchall():
                print(row)
            what = input()
            c.execute("DELETE FROM engine WHERE engine_id = ?", (what,))


# Update data in the table
#c.execute("UPDATE users SET age = ? WHERE name = ?", (35, 'Alice'))

# Delete data from the table
#c.execute("DELETE FROM car WHERE id = ?", ('Bob',))

# Fetch and print all rows again
#c.execute("SELECT * FROM users")
#print("Updated users:")
#for row in c.fetchall():
#    print(row)

# Close the connection
    if slave == "/quit":
        conn.close()
        break

print("you did good")